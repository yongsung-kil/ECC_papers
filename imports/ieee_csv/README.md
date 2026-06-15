# IEEE Xplore CSV import 폴더

IEEE 크롤링(REST)이 봇 차단(HTTP 418)되므로, IEEE 논문은 **웹에서 CSV로 직접 내보내** 여기에 넣고 import 한다.

## 내보내는 법 (IEEE Xplore 웹)

1. https://ieeexplore.ieee.org 에서 `LDPC` (또는 `low-density parity-check`) 검색
2. (선택) 좌측 필터에서 **Year**로 연도를 좁혀 한도 회피 — 연도별로 나눠 내보내면 안전
3. 결과 상단 **Export** → **Citations** 탭 → 포맷 **CSV** → **Citation and Abstract** 선택
   - ⚠️ 반드시 **Abstract 포함** 옵션을 선택해야 초록이 들어옴(없으면 빈 초록)
4. 내려받은 `*.csv` 를 이 폴더(`imports/ieee_csv/`)에 저장 (파일명 자유, 예: `ldpc_2024.csv`)

## import

```bash
python -m src.import_ieee_csv            # 이 폴더의 모든 *.csv 병합 import
python -m src.import_ieee_csv some.csv   # 특정 파일만
```

- 여러 파일을 모아 한 번에 병합되며, **같은 article number/DOI는 자동 중복 제외**.
- import 후 카탈로그(`papers/ieee/...`)가 자동 갱신됨.
- 한도에 걸리면 연도/페이지로 쪼개 여러 번 내보내 전부 이 폴더에 넣으면 됨.

> CSV 컬럼명이 예상과 다르면 import 시 무효(bad)로 집계됨 — 그 경우 헤더를 알려주면 매핑을 보완함.
