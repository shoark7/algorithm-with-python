"""Get least sum of distances to dispatch firetrucks to houses on fire

:input:
1
8 12 3 2
1 2 3
1 6 9
2 3 6
3 4 4
3 5 2
4 5 7
6 5 5
8 6 5
6 7 3
8 7 3
7 5 1
2 8 3
2 3 5
4 6

:return:
16
"""
from heapq import heappush, heappop
from math import inf
from sys import stdin

get_input = stdin.readline

def min_dist(g, dest, src):
    V = len(g)

    # Add a new trasparent vertex connecting fire stations into one sinlge station
    for s in src:
        g[0].append((0, s))
        g[s].append((0, 0))

    # 1. priority queue version
    # pq = [(0, 0)]
    # dist = [inf] * V
    # dist[0] = 0

    # while pq:
        # cost, here = heappop(pq)

        # if cost > dist[here]:
            # continue

        # for dc, there in g[here]:
            # nxt_dist = cost + dc
            # if nxt_dist < dist[there]:
                # dist[there] = nxt_dist
                # heappush(pq, (nxt_dist, there))

    # return sum(dist[d] for d in dest)


    # 2. Non-priority queue version
    dist = [inf] * V
    dist[0] = 0
    visited = [False] * V

    while True:
        min_dist = inf
        here = None

        for v in range(V):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                here = v

        if min_dist == inf:
            break

        visited[here] = True
        for dc, there in g[here]:
            nxt_dist = dist[here] + dc
            if not visited[there] and nxt_dist < dist[there]:
                dist[there] = nxt_dist

    return sum(dist[d] for d in dest)


if __name__ == '__main__':
    C = int(get_input().strip())
    ans = []

    for _ in range(C):
        V, E, DEST, SRC = (int(n) for n in get_input().strip().split())
        g = [[] for _ in range(V+1)]

        for _ in range(E):
            a, b, d = (int(n) for n in get_input().strip().split())
            g[a].append((d, b))
            g[b].append((d, a))

        dest = [int(n) for n in get_input().strip().split()]
        src = [int(n) for n in get_input().strip().split()]
        ans.append(min_dist(g, dest, src))

    for n in ans:
        print(n)
