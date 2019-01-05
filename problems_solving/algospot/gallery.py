"""Return number of cameras to cover all area of the gallery

:input:
3
6 5
0 1
1 2
1 3
2 5
0 4
4 2
0 1
2 3
1000 1
0 1

:return:
3
2
999

url: https://algospot.com/judge/problem/read/GALLERY
ID : GALLERY
"""
def number_of_cameras(graph):
    V = len(graph)
    visited = [0] * V
    UNWATCHED = 0
    WATCHED = 1
    INSTALLED = 2
    total_installed = 0

    def dfs(here):
        nonlocal total_installed
        visited[here] = True
        children = [0, 0, 0]
        for there in graph[here]:
            if not visited[there]:
                children[dfs(there)] += 1

        if children[UNWATCHED]:
            total_installed += 1
            return INSTALLED

        if children[INSTALLED]:
            return WATCHED
        return UNWATCHED

    for u in range(V):
        if not visited[u] and dfs(u) == UNWATCHED:
            total_installed += 1

    return total_installed


if __name__ == '__main__':
    C = int(input())
    ans = []

    for _ in range(C):
        V, E = (int(n) for n in input().split())
        graph = [[] for _ in range(V)]
        for _ in range(E):
            a, b = (int(n) for n in input().split())
            graph[a].append(b)
            graph[b].append(a)

        ans.append(number_of_cameras(graph))

    for n in ans:
        print(n)
