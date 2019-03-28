"""Get minimal cost to tie in Nthlon match

:input:
3
5
1 2
3 4
5 6
7 8
7 3
3
1 100
21 20
10 1
3
10 81
63 71
16 51

:return:
11
111
IMPOSSIBLE

url: https://algospot.com/judge/problem/read/NTHLON
ID : NTHLON
"""
from math import inf
import sys

MAX_T = 200

get_input = sys.stdin.readline


def dijkstra(g, src):
    V = len(g)
    dist = [inf] * V
    visited = [False] * V
    dist[src] = 0

    while True:
        min_dist = inf
        here = None

        for v in range(V):
            if dist[v] < min_dist and not visited[v]:
                here = v
                min_dist = dist[v]

        if min_dist == inf:
            break

        visited[here] = 1

        for there, cost in g[here]:
            if visited[there]:
                continue
            nxt = dist[here] + cost
            if nxt < dist[there]:
                dist[there] = nxt

    return dist


def min_tie_time(a, b):
    error_message = "IMPOSSIBLE"

    N = len(a)
    START = 401
    g = [[] for _ in range(MAX_T * 2 + 10)]

    def normalize(delta):
        return delta + MAX_T

    def solve(a, b):
        # We can add any match from the empty route
        for i in range(N):
            delta = a[i] - b[i]
            g[START].append((normalize(delta), a[i]))

        for d in range(-MAX_T, MAX_T+1):
            for i in range(N):
                nxt = d + a[i] - b[i]
                if abs(nxt) > MAX_T:
                    continue
                g[normalize(d)].append((normalize(nxt), a[i]))

        shortest = dijkstra(g, START)
        ret = shortest[normalize(0)]

        return ret if ret != inf else error_message

    return solve(a, b)


if __name__ == '__main__':
    C = int(get_input().strip())
    ans = []

    for _ in range(C):
        N = int(get_input().strip())
        a, b = [], []
        for _ in range(N):
            t1, t2 = (int(n) for n in get_input().strip().split())
            a.append(t1)
            b.append(t2)
        ans.append(min_tie_time(a, b))

    for n in ans:
        print(n)
