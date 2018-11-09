"""Get minimum cost of playing DDR game

:input:
1 2 2 4 0

:return:
8

url: https://www.acmicpc.net/problem/2342
"""
import sys


INF = 987654321


def move_cost(prev, nxt):
    diff = abs(prev - nxt)
    if diff == 0:
        return 1
    elif prev == 0 and nxt != 0:
        return 2
    elif prev != 0 and nxt == 0:
        return 0
    elif diff == 1 or diff == 3:
        return 3
    else:
        return 4


def count(l, r, n):
    if l == r and n != 0:
        return INF
    elif n == N:
        return 0
    elif cache[l][r][n] != -1:
        return cache[l][r][n]
    ret = INF
    ret = min(ret,
              count(arr[n+1], r, n+1) + move_cost(l, arr[n+1]),
              count(l, arr[n+1], n+1) + move_cost(r, arr[n+1])
             )
    cache[l][r][n] = ret
    return ret


if __name__ == '__main__':
    sys.setrecursionlimit(10**8)

    arr = [0] + [int(n) for n in input().split()][:-1]
    N = len(arr)
    arr.append(0)
    cache = [[[-1 for _ in range(N+1)] for _ in range(5)] \
          for _ in range(5)]

    print(count(0, 0, 0))
