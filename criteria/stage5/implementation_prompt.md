# Stage 5 구현 프롬프트 (1편 / SKELETON)

> 위치: `criteria/stage5/implementation_prompt.md`
> stage3 [analysis_prompt.md](../stage3/analysis_prompt.md) 대응 — 한 agent당 논문 1편.
> **상태: 뼈대.** 구현 언어·깊이 확정 후 고정.

---

## 역할

너는 NAND 플래시 LDPC ECC 엔지니어다. 입력으로 논문 1편에 대해:

1. **stage3 분석 결과**: `criteria/stage3/results/{연도}/{id_underscore}.md`
   - 특히 **B. 알고리즘 요약**(10줄) 과 **C. Prime ECC 모듈 핀포인트** 가 구현 출발점.
2. **(필요 시) 논문 본문**: `data/pdfs/{ieee|arxiv}/{연도}/**/{id}.txt`
   - 의사코드에 필요한 정확한 수식/파라미터는 여기서 확인 (그림·표 손상 가능은 stage3와 동일 주의).
3. **Prime ECC 프로파일**: [paper_screening_profile.md](../stage3/Prime_ECC_3.1_Claude/paper_screening_profile.md)
   - §6 모듈 지도 = 통합 지점.

## 목표

논문 핵심 기법을 **저쪽 src에 바로 얹고 검증할 수 있는 이식 패키지**로 떨군다.
전체 시스템이 아니라 **논문이 새로 제안한 부분(delta)** 에 집중한다.

> 운영 전제: 이 PC엔 Prime ECC src 없음 → 여기서 L0~L3 준비, **L4(성능 실측)는 src에서만**.
> **완전 독립 디코더 재구현 금지**(Prime ECC가 이미 min-sum 보유). **성능 검증을 여기서 하지 말 것**(float toy는 오도). 상세: [README.md](README.md) 깊이 사다리.

## 산출물 (논문 1편 = 폴더 하나)

저장 위치: `criteria/stage5/results/{id_underscore}/`
필수 5종: `pseudocode.md`(L0) · `impl.py`(L1) · `integration_patch.md`(L2) · `verification_plan.md`(L3) · `notes.md`(인덱스).
완성 예시: [results/ieee_9496601/](results/ieee_9496601/).

### 1. `pseudocode.md`

```
# {id} — {제목} : Pseudo-code

## 스펙
- 입력 / 출력 / 자료구조
- 파라미터 (논문 값, 없으면 미상)

## 알고리즘 (핵심 delta)
FUNCTION Name(inputs):
    ...            # 언어 중립, 논문 식 번호 인라인 주석
    RETURN outputs

## 참고
- 논문 근거: (식/그림 번호)
- 기존 기법 대비 바뀐 부분: (한 줄)
```

### 2. `impl.py` — delta-only 정확성 레퍼런스 (언어 = **Python**)

- 목적: **mechanics smoke test** — delta가 의사코드대로 돌고 의도한 국소 효과(예: 진폭 상한)를 내는지만 확인.
- **성능/우수성 주장 금지.** self-check가 항진명제면 "성능 아님"으로 명시. 성능은 verification_plan.md/src.
- 디코더 본체가 이미 Prime ECC에 있으면 **delta 함수에 집중**(전체 재구현 지양).

### 3. `integration_patch.md` — 이식 패치 플랜 (L2)

- 삽입 지점 **diff 스켈레톤**(실 변수명은 `<...>` 플레이스홀더), toy↔Prime ECC **매핑표**, **파라미터 도메인 명세**(값이 어느 스케일/테이블 인덱스인지), src 접근 시 TODO.

### 4. `verification_plan.md` — 검증 설계 (L3, 저쪽 실행)

- 부호·채널·bit-width, **비교군(baseline / delta / 대조군)**, 지표, 파라미터 스캔 그리드, **pass/fail 정량 기준**, 통계·비용 예산. 저쪽이 빈칸 채우고 실행만.

### 5. `notes.md`

```
# {id} — 통합 노트 (위 문서 인덱스)
- Prime ECC 대응 모듈: (profile §6 파일·함수명)   ← stage3 C섹션 재사용
- 이식 난이도: 낮음|중|높음 + 이유
- 검증: mechanics 확인 결과 + 성능은 verification_plan.md(src)로 위임 명시
- 한계·리스크: (한 줄)
```

## 규칙

- **stage3 결과를 1차 소스로** 삼되, 수식/파라미터가 애매하면 논문 `.txt`로 보강.
- 의사코드는 언어 중립, 구현은 **delta 최소·검증가능**. 과설계·독립 디코더 재구현 금지.
- 파일 참조는 markdown link `[파일명](상대경로)`. 절대경로·백틱·HTML 금지 (stage3 규칙 동일).
- 모르면 `미상`. 추측 금지. profile에 없는 함수명 지어내지 말 것(플레이스홀더로).

## 재발 방지 주의 (라이트리뷰 2026-07-09)

- **파라미터 도메인**: 스캔·상한이 *입력* bit-width가 아니라 *내부* 값 도메인일 수 있음 — 어느 스케일인지 명세.
- **baseline 이중정의**: 기존 코드가 이미 유사 포화/클램프 중이면 순수 delta가 달라짐 — baseline을 실코드에 맞춰 고정.
- **지원 범위**: 논문 헤드라인 조건(예: 4bit)이 src 미지원일 수 있음 — 목표를 src 지원 범위로 축소.
- **성능은 src에서**: 여기 toy 결과로 "이득 있음" 결론 금지.
