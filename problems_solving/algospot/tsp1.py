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
def tsp1(dist):
    N = len(dist)
    visited = [False for _ in range(N)]
    VISITED_ALL = (1 << N) - 1
    cache = [[-1 for _ in range(1 << N)] for _ in range(N)]
    path = []

    def min_dist(last, visited):
        if visited == VISITED_ALL:
            return 0
        if cache[last][visited] != -1:
            return cache[last][visited]

        ret = 987654321
        for nxt in range(N):
            if visited & (1 << nxt) == 0:
                ret = min(ret, min_dist(nxt, visited+(1<<nxt)) + dist[last][nxt])
        cache[last][visited] = ret
        return ret

    # def generate(visited):
        # if visited == VISITED_ALL:
            # return path

        # if not path:
            # for nxt in range(N):
                # tmp = 987654321
                # if min_dist(nxt, 1 << nxt) < tmp:
                    # best = nxt
                    # tmp = min_dist(nxt, 1 << nxt)
            # path.append(best)
            # return generate(1<<best)

        # last = path[-1]
        # for nxt in range(N):
            # if min_dist(last, visited-(1<<last)) == min_dist(nxt, visited+(1<<nxt)) + dist[last][nxt]:
                # path.append(nxt)
                # return generate(visited+(1<<nxt))


    ans = 987654321
    for city in range(N):
        ans = min(ans, min_dist(city, 1 << city))
    # path = generate(0)
    return ans


if __name__ == '__main__':
    C = int(input())
    ans = []
    for _ in range(C):
        N = int(input())
        dist = []
        for _ in range(N):
            new_row = [float(n) for n in input().split()]
            dist.append(new_row)
        ans.append(tsp1(dist))
    for n in ans:
        print(n)
