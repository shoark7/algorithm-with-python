"""Return minimum multiplication counts of series of matrices

:input:
3
5 3
3 2
2 6

:return:
90

url: https://www.acmicpc.net/problem/11049
ID : 11049
"""
# 참고로 이 풀이는 pypy3에서만 돌아감...
ANS_LIMIT = 2 ** 32


class Matrix:
    def __init__(self, r, c):
        self.r = r
        self.c = c


def minimal_counts(dimensions):
    N = len(dimensions)
    cache = [[None] * N for _ in range(N)]

    def count(a, b):
        if b == a:
            return 0
        elif cache[a][b] is not None:
            return cache[a][b]

        tmp_ans = ANS_LIMIT
        for k in range(a, b):
            tmp_ans = min(tmp_ans, count(a, k) + count(k+1, b) \
                              + dimensions[a].r * dimensions[k].c * dimensions[b].c)
        cache[a][b] = tmp_ans
        return tmp_ans
    return count(0, N-1)


if __name__ == '__main__':
    C = int(input())
    dimensions = []
    for i in range(C):
        r, c = (int(n) for n in input().split())
        dimensions.append(Matrix(r, c))
    print(minimal_counts(dimensions))
