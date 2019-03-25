"""Get minimal amplified noise in the route

:input:
    1
    7 14
    0 1 1.3
    0 2 1.1
    0 3 1.24
    3 4 1.17
    3 5 1.24
    3 1 2
    1 2 1.31
    1 2 1.26
    1 4 1.11
    1 5 1.37
    5 4 1.24
    4 6 1.77
    5 6 1.11
    2 6 1.2

:return:
    1.3200000000

url: https://algospot.com/judge/problem/read/ROUTING
ID : ROUTING
"""
from heapq import heappop, heappush
from math import inf, log10
from sys import stdin

get_input = stdin.readline


def minimal_noise(g):
    V = len(g)
    dist = [inf] * V
    dist[0] = log10(1)
    visited = [False] * V

    while True:
        min_dist = inf
        here = None

        for v in range(V):
            if dist[v] < min_dist and not visited[v]:
                here = v
                min_dist = dist[v]

        if min_dist == inf:
            break

        visited[here] = True

        for cost, there in g[here]:
            if visited[there]:
                continue
            nxt_dist = dist[here] + cost
            dist[there] = min(dist[there], nxt_dist)

    return 10 ** dist[V-1]


if __name__ == '__main__':
    C = int(get_input().strip())
    ans = []

    for _ in range(C):
        V, E = (int(n) for n in get_input().strip().split())
        g = [[] for _ in range(V)]
        for _ in range(E):
            line = get_input().strip().split()
            f, t, n = int(line[0]), int(line[1]), log10(float(line[2]))
            g[f].append((n, t))
            g[t].append((n, f))
        ans.append(minimal_noise(g))

    for noise in ans:
        print(noise)
