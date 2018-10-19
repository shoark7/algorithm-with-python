"""Return the number of monotonic polynomios when number of squares are given

If answer is bigger than 1e7, return the modulo by 1e7.

:input:
    3
    2
    4
    92

:return:
    2
    19
    4841817

ID : POLY
url: https://algospot.com/judge/problem/read/POLY
"""
MOD = int(1e7)
cache = [[-1 for _ in range(100+1)] for _ in range(100+1)]


def mono_polynomios(n):
    def poly(n, this):
        global cache
        if n == this:
            return 1
        elif cache[n][this] != -1:
            return cache[n][this]
        else:
            cache[n][this] = sum((this+second-1) * poly(n-this, second) for second in range(1, n-this+1))

            cache[n][this] %= MOD
            return cache[n][this]

    ans = 0
    for i in range(1, n+1):
        ans += poly(n, i)

    return ans % MOD


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        ans.append(mono_polynomios(int(input())))

    for n in ans:
        print(n)
