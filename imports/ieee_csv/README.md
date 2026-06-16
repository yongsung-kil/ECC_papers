# IEEE Xplore CSV import 폴더

IEEE 검색 API의 abstract는 ~400자로 잘린다. **전체 초록**은 IEEE Xplore 웹의
CSV 내보내기에 들어 있으므로, 여기에 CSV를 넣고 import 해서 초록을 덧입힌다(UPSERT).

## 내보내는 법 (IEEE Xplore 웹)

1. https://ieeexplore.ieee.org 에서 `LDPC` 검색
2. 좌측 **Year** 필터로 연도를 좁힘 (한 번에 받을 양 ↓, 보통 연도당 ~900건)
3. 결과 상단 **Export** → **Citations** → 포맷 **CSV** → **Citation and Abstract** 선택
   - ⚠️ 반드시 **Abstract 포함** 옵션이어야 전체 초록이 들어옴
4. 받은 `*.csv` 를 이 폴더에 저장 (파일명 자유, 예: `ldpc_2024.csv`)

## import

```bash
python -m src.import_ieee_csv            # 이 폴더의 모든 *.csv (UPSERT)
python -m src.import_ieee_csv some.csv   # 특정 파일만
```

- 기존 논문(같은 article number) → **전체 초록으로 갱신**, 새 논문 → 추가
- import 후 카탈로그가 자동 갱신됨
- 한도에 걸리면 연도/페이지로 쪼개 여러 파일로 받아 모두 이 폴더에 넣으면 됨
