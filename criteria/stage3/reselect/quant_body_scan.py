#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
quant_body_scan.py

논문 본문 txt에서 '디코더 내부 양자화' 서술 여부(유무)를 판정하기 위한
양자화 관련 키워드 스니펫을 추출한다.

- 대상: criteria/stage3/reselect/reselect.json 의 sid 전체
- 제외: quant_tags.json 에서 quant=="O" (이미 '핵심 기여'로 분류된 208편)
- txt 경로: data/pdfs 하위에서 {sid}.txt 파일명 글롭으로 매핑
- 출력: criteria/stage3/reselect/body_candidates.jsonl + stdout 통계

표준 라이브러리만 사용.
"""

import json
import re
import sys
from pathlib import Path

# Windows 콘솔에서 한글이 깨지지 않도록 stdout을 utf-8로 재설정
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ----------------------------------------------------------------------------
# 경로 설정 (프로젝트 루트 기준 상대경로로 기록)
# ----------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent          # criteria/stage3/reselect
ROOT = SCRIPT_DIR.parents[2]                           # 프로젝트 루트
RESELECT_JSON = SCRIPT_DIR / "reselect.json"
QUANT_TAGS_JSON = SCRIPT_DIR / "quant_tags.json"
PDFS_DIR = ROOT / "data" / "pdfs"
OUT_JSONL = SCRIPT_DIR / "body_candidates.jsonl"

# 스니펫 파라미터
BEFORE = 300      # 매칭 앞 글자 수
AFTER = 400       # 매칭 뒤 글자 수
MAX_SNIPPETS = 6  # 논문당 최대 스니펫 수

# ----------------------------------------------------------------------------
# 키워드 정의 (대소문자 무시). 라벨 -> 정규식
#   [\s-]* : PDF 추출본에서 공백/개행/하이픈으로 분리된 복합어까지 포착
# ----------------------------------------------------------------------------
KEYWORD_PATTERNS = {
    "quanti": r"quanti",                       # quantize/quantization/quantized ...
    "fixed-point": r"fixed[\s-]+point",        # fixed-point / fixed point
    "bit-width": r"bit[\s-]*width",            # bit-width / bit width / bitwidth
    "word-length": r"word[\s-]*length",        # word-length / word length / wordlength
    "finite precision": r"finite[\s-]+precision",
    "low precision": r"low[\s-]+precision",
}

# 매칭된 실제 문자열을 라벨로 분류
def classify(matched_text):
    t = matched_text.lower()
    if t.startswith("quanti"):
        return "quanti"
    if "fixed" in t:
        return "fixed-point"
    if "bit" in t and "width" in t:
        return "bit-width"
    if "word" in t and "length" in t:
        return "word-length"
    if "finite" in t:
        return "finite precision"
    if "low" in t:
        return "low precision"
    return "quanti"  # fallback (도달 불가)

COMBINED_RE = re.compile(
    "(" + "|".join(KEYWORD_PATTERNS.values()) + ")",
    re.IGNORECASE,
)
WS_RE = re.compile(r"\s+")


def normalize_ws(s):
    return WS_RE.sub(" ", s).strip()


def merge_intervals(intervals):
    """[ (a,b), ... ] 정렬 후 겹치거나 맞닿은 구간 병합."""
    if not intervals:
        return []
    intervals = sorted(intervals)
    merged = [list(intervals[0])]
    for a, b in intervals[1:]:
        if a <= merged[-1][1]:      # 겹침 또는 인접
            if b > merged[-1][1]:
                merged[-1][1] = b
        else:
            merged.append([a, b])
    return merged


def build_sid_map():
    """data/pdfs/**/{sid}.txt -> 상대경로 문자열 매핑.

    주의: arxiv 논문은 reselect.json의 sid가 'arxiv_' 접두를 갖지만
    실제 파일명 stem에는 접두가 없다(예: sid=arxiv_cond-mat_0310177v1,
    파일=cond-mat_0310177v1.txt). 그런 경우 'arxiv_'+stem 별칭도 등록한다.
    """
    sid_map = {}
    for p in PDFS_DIR.rglob("*.txt"):
        stem = p.stem
        rel = p.relative_to(ROOT).as_posix()          # posix 상대경로
        parts = p.relative_to(PDFS_DIR).parts
        venue = parts[0] if parts else ""
        sid_map[stem] = rel
        if venue == "arxiv" and not stem.startswith("arxiv_"):
            sid_map["arxiv_" + stem] = rel
    return sid_map


def scan_text(text):
    """본문 텍스트에서 매칭 span 목록과 라벨별 카운트 산출."""
    spans = []
    label_counts = {}
    for m in COMBINED_RE.finditer(text):
        spans.append((m.start(), m.end()))
        lab = classify(m.group(0))
        label_counts[lab] = label_counts.get(lab, 0) + 1
    return spans, label_counts


def make_snippets(text, spans):
    """각 매칭 span을 앞뒤로 확장 후 병합, 정규화한 스니펫 리스트 반환."""
    n = len(text)
    regions = []
    for s, e in spans:
        a = max(0, s - BEFORE)
        b = min(n, e + AFTER)
        regions.append((a, b))
    merged = merge_intervals(regions)
    snippets = [normalize_ws(text[a:b]) for a, b in merged]
    return snippets


def main():
    # --- 입력 로드 ---
    reselect = json.load(open(RESELECT_JSON, encoding="utf-8"))
    quant_tags = json.load(open(QUANT_TAGS_JSON, encoding="utf-8"))

    core_o = {sid for sid, v in quant_tags.items() if v.get("quant") == "O"}
    target_sids = [row["sid"] for row in reselect if row["sid"] not in core_o]

    sid_map = build_sid_map()

    # --- 스캔 ---
    missing_txt = []          # txt 파일 없는 sid
    matched_papers = 0
    no_match_papers = 0
    keyword_paper_counts = {k: 0 for k in KEYWORD_PATTERNS}  # 라벨별 매칭 '편수'
    total_snippet_chars = 0
    total_snippet_count = 0
    total_snippet_bytes = 0
    examples = []             # 대표 예시 후보

    with open(OUT_JSONL, "w", encoding="utf-8") as fout:
        for sid in target_sids:
            rel = sid_map.get(sid)
            if rel is None:
                missing_txt.append(sid)
                continue
            fpath = ROOT / rel
            try:
                text = fpath.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                missing_txt.append(sid)
                continue

            spans, label_counts = scan_text(text)
            if not spans:
                no_match_papers += 1
                continue

            matched_papers += 1
            for lab in label_counts:
                keyword_paper_counts[lab] += 1

            all_snips = make_snippets(text, spans)
            n_snip_total = len(all_snips)
            snippets = all_snips[:MAX_SNIPPETS]

            for sn in snippets:
                total_snippet_chars += len(sn)
                total_snippet_bytes += len(sn.encode("utf-8"))
            total_snippet_count += len(snippets)

            rec = {
                "sid": sid,
                "txt": rel,
                "n_match": len(spans),
                "n_snippet_total": n_snip_total,   # 초과분 포함 병합 스니펫 총개수
                "snippets": snippets,
            }
            fout.write(json.dumps(rec, ensure_ascii=False) + "\n")

            if len(examples) < 3 and snippets:
                examples.append((sid, snippets[0][:150]))

    # --- 통계 ---
    avg_len = (total_snippet_chars / total_snippet_count) if total_snippet_count else 0.0
    total_mb = total_snippet_bytes / (1024 * 1024)

    print("=" * 70)
    print("quant_body_scan 결과")
    print("=" * 70)
    print(f"스캔 대상 편수          : {len(target_sids)}  "
          f"(reselect {len(reselect)} - core_O {len(core_o)})")
    print(f"txt 없는 편수           : {len(missing_txt)}")
    if missing_txt:
        print(f"  예시(최대5) : {missing_txt[:5]}")
    print(f"매칭 있는 편수          : {matched_papers}")
    print(f"매칭 없는 편수          : {no_match_papers}")
    print("-" * 70)
    print("키워드별 분포 (매칭 편수 기준):")
    for k in KEYWORD_PATTERNS:
        print(f"  {k:<18}: {keyword_paper_counts[k]}")
    print("-" * 70)
    print(f"스니펫 평균 길이(문자)  : {avg_len:.1f}")
    print(f"스니펫 총 용량          : {total_mb:.2f} MB "
          f"(스니펫 {total_snippet_count}개, {total_snippet_chars} chars)")
    print("-" * 70)
    print("대표 예시 3편:")
    for sid, head in examples:
        print(f"  [{sid}] {head}")
    print("-" * 70)
    print(f"출력 파일: {OUT_JSONL.relative_to(ROOT).as_posix()}")
    print("=" * 70)


if __name__ == "__main__":
    main()
