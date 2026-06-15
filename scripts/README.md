# 수집 스케줄러 (Windows 작업 스케줄러)

LDPC 논문을 주기적으로 자동 수집하는 스케줄러입니다.

## 동작 방식

1. **이어받기(커서)** — 쿼리마다 "어디까지 받았는지(offset)"를 DB(`collect_state`)에 저장합니다.
   제출일 **오름차순**으로 받기 때문에 새 논문이 나와도 순서가 꼬이지 않고, 누락 없이
   과거분을 채운 뒤 이후 신규분까지 계속 수집합니다. 한 번에 `-n`건씩(기본 100) 받습니다.
2. **중복 제외** — 논문 ID(`arxiv:…` / `ieee:…`) 기준으로 이미 있는 건은 건너뜁니다.
3. **카탈로그 재생성 + 교차 중복 제거** — 소스별/월별 `papers/**/catalog.md|csv` 갱신.
4. **GitHub 업로드** — 신규 수집이 있을 때만 `data/papers.db`와 `papers/`를 commit & push.
5. **로그** — `logs/collect_YYYY-MM.log` 파일 + DB `run_log` 테이블.

## 수동 실행

```bash
python -m src.runner              # 쿼리당 100건씩 수집 + git push
python -m src.runner -n 200       # 한 번에 200건씩
python -m src.runner --no-push    # 수집만, git 업로드 생략
python -m src.runner --sources arxiv   # arXiv만
```

## 스케줄 등록 (6시간마다)

```powershell
powershell -ExecutionPolicy Bypass -File scripts\register_task.ps1
# 간격 조정: -IntervalHours 3
```

- 즉시 1회 실행(테스트): `schtasks /Run /TN "LDPC_Paper_Collector"`
- 등록 해제: `schtasks /Delete /TN "LDPC_Paper_Collector" /F`

> 주의: 작업 스케줄러는 **PC가 켜져 있을 때만** 실행됩니다. git push가 동작하려면
> 원격(origin)에 인증이 설정돼 있어야 합니다(자격증명 관리자 또는 SSH 키).
