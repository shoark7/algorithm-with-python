"""Get min amount of scoops to make up right bottle of potion

:input:
3
4
4 6 2 4
6 4 2 4
4
4 6 2 4
7 4 2 4
3
4 5 6
1 2 3

:return:
0 5 1 2
1 8 2 4
3 3 3

url: https://algospot.com/judge/problem/read/POTION
ID : POTION
"""
import math


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def min_scoop(reci, put):
    N = len(reci)
    ret = [0 for _ in range(N)]
    b = reci[0]

    for i in range(1, N):
        b = gcd(b, reci[i])

    max_ratio = 0
    for i in range(N):
        max_ratio = max(max_ratio, put[i] / reci[i])
    a = math.ceil(b * max_ratio)

    for i in range(N):
        ret[i] += int(reci[i] * a / b - put[i])
    return ret



if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        input()
        reci = [int(n) for n in input().split()]
        put = [int(n) for n in input().split()]
        ans.append(min_scoop(reci, put))

    for n in ans:
        print(' '.join(str(c) for c in n))
