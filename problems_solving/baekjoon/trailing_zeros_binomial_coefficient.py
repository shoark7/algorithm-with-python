"""Return number of trailing zeros of given binomial coefficient

:input:
25 12

:return:
2

For information of trailing zeros of factorial N(N!),
visit my place and behold how it shall be:
    https://shoark7.github.io/programming/algorithm/number-of-trailing-zeros-in-factorial


URL: https://www.acmicpc.net/problem/2004
ID : 2004
"""
def g(n, f):
    counts = 0
    tmp_f = f
    while n >= tmp_f:
        counts += (n // tmp_f)
        tmp_f *= f
    return counts

def trailing_zeros_combi(n, m):
    return min(g(n, 5) - g(m, 5) - g(n - m, 5),
               g(n, 2) - g(m, 2) - g(n - m, 2))


if __name__ == '__main__':
    n, m = (int(x) for x in input().split())
    print(trailing_zeros_combi(n, m))
