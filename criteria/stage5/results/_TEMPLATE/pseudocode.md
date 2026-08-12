# {id} — {제목} : Pseudo-code (TEMPLATE)

> 이 폴더는 stage5 산출물 **템플릿**이다. 실제 논문 처리 시 `results/{id_underscore}/` 로 복사해 채운다.

## 스펙
- 입력: (예: LLR 배열, H-matrix / PCM)
- 출력: (예: 복호 코드워드, syndrome)
- 자료구조: (예: CN/VN 메시지 배열)
- 파라미터: (논문 값 — scaling factor, max_iter 등 / 없으면 미상)

## 알고리즘 (핵심 delta)

```
FUNCTION Name(inputs):
    # 논문 식 (n) 인라인 주석
    FOR ...:
        ...
    RETURN outputs
```

## 참고
- 논문 근거: (식/그림 번호)
- 기존(min-sum 등) 대비 바뀐 부분: (한 줄)
- stage3 결과: [../../stage3/results/{연도}/{id_underscore}.md](#)
