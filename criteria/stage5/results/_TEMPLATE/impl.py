"""
{id} — {제목} : 간단 구현 (TEMPLATE)

stage5 산출물 템플릿. 실제 처리 시 results/{id_underscore}/impl.py 로 복사해 채운다.
언어는 미정(Python vs C++). 이 파일은 Python 슬롯 예시.

목적: 논문 핵심 알고리즘(delta)의 동작하는 최소 예제. 전체 시스템 X.
실행: python impl.py   (toy input 으로 self-check)
"""


def algorithm(*args, **kwargs):
    """논문 핵심 기법. pseudocode.md 와 1:1 대응."""
    raise NotImplementedError("TODO: 논문 알고리즘 구현")


def _selfcheck():
    """toy input (작은 H-matrix / 몇 비트) 으로 동작 확인."""
    # TODO: 최소 예제로 algorithm() 호출 후 기대값 대조
    pass


if __name__ == "__main__":
    _selfcheck()
