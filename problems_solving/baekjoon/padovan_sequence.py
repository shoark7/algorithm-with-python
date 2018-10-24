"""Return the nth Padovan Sequence

:input:
2
6
12

:return:
3
16

url: https://www.acmicpc.net/problem/9461
"""
arr = []
ans = []
max_v = -1
C = int(input())

for _ in range(C):
    n = int(input())
    arr.append(n)
    max_v = max(max_v, n)

cache = [-1 for _ in range(max_v+1)]


def padovan(n):
    if n < 4:
        return 1
    elif cache[n] != -1:
        return cache[n]
    else:
        cache[n] = padovan(n-2) + padovan(n-3)
        return cache[n]


for n in arr:
    ans.append(padovan(n))

for n in ans:
    print(n)
