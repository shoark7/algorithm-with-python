"""Return shortest sum of distances cars moved and print each move

:input:
6
3
3 5
5 5
2 3

:return:
9
2
2
1

url: https://www.acmicpc.net/problem/2618
"""
import sys
sys.setrecursionlimit(10 ** 12)


def func(N, cases):
    cases = [(1, 1), (N, N)] + cases
    cache = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    routes = []

    def dist(x, y):
        pos1, pos2 = cases[x], cases[y]
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def calc(x, y):
        if max(x, y) >= len(cases) - 1:
            return 0
        elif cache[x][y] != -1:
            return cache[x][y]

        nxt = max(x, y) + 1
        cache[x][y] = min(calc(nxt, y) + dist(nxt, x),
                          calc(x, nxt) + dist(y, nxt))
        return cache[x][y]

    def generate_route(x, y, nth):
        if nth == len(cases):
            return

        if calc(nth, y) + dist(nth, x) < calc(x, nth) + dist(y, nth):
            routes.append(1)
            generate_route(nth, y, nth+1)
        else:
            routes.append(2)
            generate_route(x, nth, nth+1)


    generate_route(0, 1, 2)
    return calc(0, 1), routes


if __name__ == '__main__':
    N = int(input())
    C = int(input())
    cases = []
    for _ in range(C):
        x, y = (int(n) for n in input().split())
        cases.append((x, y))

    min_dist, routes = func(N, cases)
    print(min_dist)

    for i in range(len(routes)):
        if i != len(routes) - 1:
            print(routes[i])
        else:
            print(routes[i], end='')
