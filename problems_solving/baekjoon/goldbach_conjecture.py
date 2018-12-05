"""Return a tuple of 2 prime numbers which consist of given N

:input:
3
8
10
16

:return:
3 5
5 5
5 11

url: https://www.acmicpc.net/problem/9020
"""
SIZE = 10000
sieves = [1 for _ in range(SIZE + 1)]
sieves[0] = sieves[1] = 0

for i in range(2, int(SIZE ** (1/2))):
    if sieves[i] == 1:
        for j in range(i*i, SIZE+1, i):
            sieves[j] = 0


def prime_pair(n):
    if n == 4:
        return 2, 2

    half = n // 2
    lo, hi = (half - 1, half + 1) if half % 2 == 0 else (half, half)
    while lo > 1:
        if sieves[lo] == 1 and sieves[hi] == 1:
            return lo, hi
        lo -= 2
        hi += 2


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        n = int(input())
        ans.append(prime_pair(n))

    for n in ans:
        print(' '.join(str(i) for i in n))
