"""Change a number to 1 and get process of it too

https://www.acmicpc.net/problem/12852
"""
import sys

sys.setrecursionlimit(10 ** 6)


def make_it_to_1(N):
    INF = float('inf')
    cache = {1: 0}
    routes = []

    def min_cost(n):
        nonlocal cache
        if n in cache:
            return cache[n]

        ret = INF
        if not n % 2:
            ret = min(ret, min_cost(n // 2) + 1)
        if not n % 3:
            ret = min(ret, min_cost(n // 3) + 1)
        if n % 6:
            ret = min(ret, min_cost(n-1) + 1)

        cache[n] = ret
        return ret

    def trace_route(N):
        nonlocal routes
        routes.append(N)
        if N == 1:
            return

        if not N % 3 and min_cost(N) - 1 == min_cost(N // 3):
            trace_route(N // 3)
        elif not N % 2 and min_cost(N) - 1 == min_cost(N // 2):
            trace_route(N // 2)
        else:
            trace_route(N - 1)

    trace_route(N)

    return min_cost(N), routes


if __name__ == '__main__':
    N = int(input())
    costs, routes = make_it_to_1(N)

    print(costs)
    print(*routes)
