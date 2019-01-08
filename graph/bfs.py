def shortest_path(g, a, b):
    N = len(g)
    parent = [-1] * N
    parent[a] = a
    distance = [-1] * N
    distance[a] = 0
    path = [b]

    q = [a]
    while q:
        here = q.pop(0)
        for there in range(N):
            if g[here][there] and distance[there] == -1:
                q.append(there)
                distance[there] = distance[here] + 1
                parent[there] = here

    while parent[b] != b:
        b = parent[b]
        path.append(b)

    path.reverse()
    return path


def bfs(g, start):
    N = len(g)
    discovered = [0] * N
    q = [start]
    discovered[start] = 1

    while q:
        now = q.pop(0)
        print(now)
        for i in range(N):
            if g[now][i] and not discovered[i]:
                q.append(i)
                discovered[i] = 1


def connect(a, b, g):
    g[a][b] = 1
    g[b][a] = 1


if __name__ == '__main__':
    N = 9
    g = [[0] * N for _ in range(N)]
    connect(0, 1, g)
    connect(0, 4, g)
    connect(0, 3, g)
    connect(0, 7, g)
    connect(5, 4, g)
    connect(1, 2, g)
    connect(1, 3, g)
    connect(2, 5, g)
    connect(2, 6, g)
    connect(3, 6, g)
    connect(8, 6, g)

    print(shortest_path(g, 0, 6))
