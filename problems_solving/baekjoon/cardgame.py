"""Return Geun-u's maximum score

:input:
2
4
1 2 5 2
9
1 1 1 1 2 2 2 2 2

:return:
6
8

ID : 11062
url: https://www.acmicpc.net/problem/11062
"""
import sys
sys.setrecursionlimit(10 ** 8)


def get_score(l):
    N = len(l)
    cache = [[-1 for _ in range(N)] for _ in range(N)]

    def get(lo, hi, turn):
        if lo > hi:
            return 0
        elif cache[lo][hi] != -1:
            return cache[lo][hi]

        if turn == 1:
            ret = max(get(lo+1, hi, 1-turn) + l[lo],
                      get(lo, hi-1, 1-turn) + l[hi])
        else:
            ret = min(get(lo+1, hi, 1-turn),
                      get(lo, hi-1, 1-turn))
        cache[lo][hi] = ret
        return ret
    return get(0, N-1, 1)


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        input()
        l = [int(n) for n in input().split()]
        ans.append(get_score(l))
    for n in ans:
        print(n)
