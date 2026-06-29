# IEEE Xplore 수집기 완성

## 목적
IEEE Xplore에서 LDPC 관련 논문을 크롤링하여 DB에 저장

## 현재 상태
- 뼈대 구현 완료 (`src/ieee_collector.py`)
- 라이센스 네트워크에서 테스트 필요

## 구현 방식
- IEEE Xplore REST endpoint (`/rest/search`)로 검색
- 개별 논문 페이지에서 abstract 크롤링 (meta 태그 → JSON-LD → JS 변수 순서로 시도)
- 같은 `papers` 테이블에 `source='ieee'`로 저장

## 수정 대상 파일
- `src/ieee_collector.py` — 크롤링 로직 보완
- `src/arxiv_collector.py` — catalog 출력에 IEEE 포함 (완료)

## TODO
- [ ] 라이센스 네트워크에서 REST endpoint 응답 확인
- [ ] abstract 추출 로직 실제 페이지로 검증
- [ ] 검색 키워드 튜닝
- [ ] rate limiting / 에러 핸들링 보완

## 안전성 체크리스트
- [x] 기존 arXiv 수집 로직에 영향 없음
- [x] DB 스키마 변경 없음 (source 컬럼으로 구분)
- [ ] IEEE 이용약관 준수 확인
