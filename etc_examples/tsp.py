"""Get minimum distance of paths visiting all the cities only once

:input:
2
3
0.0000000000  611.6157225201  648.7500617289
611.6157225201  0.0000000000  743.8557967501
648.7500617289  743.8557967501  0.0000000000
4
0.0000000000  326.0008994586  503.1066076077  290.0250922998
326.0008994586  0.0000000000  225.1785728436  395.4019367384
503.1066076077  225.1785728436  0.0000000000  620.3945520632
290.0250922998  395.4019367384  620.3945520632  0.0000000000

:return:
1260.3657842490
841.2045646020

url: https://algospot.com/judge/problem/read/TSP1
ID : TSP1
"""
import time


### 1. Pure exhaustive tsp
def tsp_pure_exhaustive(dist):
    stime = time.time()
    best = 987654321
    N = len(dist)
    visited = [0 for _ in range(N)]
    visited[0] = 1

    def search(path, visited, curr_dist):
        nonlocal best
        here = path[-1]
        if best <= curr_dist:
            return
        if len(path) == N:
            best = min(best, curr_dist + dist[here][0])
            return

        for nxt in range(N):
            if visited[nxt]:
                continue
            path.append(nxt)
            visited[nxt] = 1
            search(path, visited, curr_dist+dist[here][nxt])
            path.pop()
            visited[nxt] = 0

    search([0], visited, 0)
    etime = time.time()
    print("I'm tsp_pure_exhaustive and my execution time is ", etime-stime)
    print('-' * 30)
    return best


### 2. Simple heuristic used
def tsp_pruning_1(dist):
    # Connect closiest cities
    stime = time.time()
    INF = 987654321
    best = INF
    N = len(dist)
    visited = [0 for _ in range(N)]
    min_edge = [0 for _ in range(N)]

    def simple_heuristic(visited):
        ret = min_edge[0]
        for i in range(N):
            if not visited[i]:
                ret += min_edge[i]
        return ret

    def initialize(min_edge):
        for i in range(N):
            for j in range(N):
                if i != j:
                    min_edge[i] = min(min_edge[i], dist[i][j])

    def search(path, visited, curr_dist):
        nonlocal best
        here = path[-1]
        if best <= curr_dist + simple_heuristic(visited):
            return
        if len(path) == N:
            best = min(best, curr_dist + dist[here][0])
            return

        for nxt in range(N):
            if visited[nxt]:
                continue
            path.append(nxt)
            visited[nxt] = 1
            search(path, visited, curr_dist+dist[here][nxt])
            path.pop()
            visited[nxt] = 0

    visited[0] = 1
    search([0], visited, 0)
    etime = time.time()
    print("I'm simple heuristic and my execution time is ", etime-stime)
    print('-' * 30)
    return best



if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        dist = []
        for _ in range(N):
            new_row = [float(n) for n in input().split()]
            dist.append(new_row)
        ans.append(tsp_pure_exhaustive(dist))
        ans.append(tsp_pruning_1(dist))
    # for n in ans:
        # print(n)
