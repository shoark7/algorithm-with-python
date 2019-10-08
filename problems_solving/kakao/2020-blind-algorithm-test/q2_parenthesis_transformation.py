"""2020 카카오 신입 개발자 블라인드 테스트 2: 괄호 변환

* 핵심 아이디어:
    1. 재귀함수를 짜는 게 핵심이다. 천천히, 정의되어 있는 대로 함수를 만들어나간다.
    2. 파이썬의 기본 재귀 한계는 1000이다. 입력 괄호의 길이의 상한 또한 1000이므로,
       별다른 수정이 필요없다.


문제 URL: https://programmers.co.kr/learn/courses/30/lessons/60058
"""
def solution(p):
    OPENER, CLOSER = '()'

    def is_balanced(p):
        return p.count(OPENER) == p.count(CLOSER)

    def is_correct(parens):
        count = 0
        for p in parens:
            count += 1 if p == OPENER else -1
            if count < 0:
                return  False
        return count == 0

    def process_parens(p):
        if not p:
            return p

        for i in range(2, len(p)+1, 2):
            if is_balanced(p[:i]):
                A, B = p[:i], p[i:]
                break

        if is_correct(A):
            return A + process_parens(B)
        else:
            B = OPENER + process_parens(B) + CLOSER
            A = A[1:-1]
            A = ''.join(CLOSER if a == OPENER else OPENER for a in A)
            return B + A

    return process_parens(p)
