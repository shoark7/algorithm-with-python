from copy import deepcopy

NO_EDGE = 987654321


# Connect two vetcies in a graph with value 'v'. Undirected is default.
def connnect(graph, a, b, v, undirected=True):
    graph[a][b] = v
    if undirected:
        graph[b][a] = v


def floyd_prototype(g, src, dest):
    V = len(g)
    dist = [[[NO_EDGE] * V for _ in range(V)] for _ in range(V)]

    for i in range(V):
        for j in range(V):
            if i == j:
                dist[0][i][j] = 0
            else:
                dist[0][i][j] = min(g[i][j], g[i][0] + g[0][j])

    for k in range(1, V):
        for i in range(V):
            for j in range(V):
                dist[k][i][j] = min(dist[k-1][i][j],
                                    dist[k-1][i][k] + dist[k-1][k][j])

    return dist[V-1][src][dest]


def floyd(g, src, dest):
    dist = deepcopy(g)
    V = len(g)
    for i in range(V):
        dist[i][i] = 0

    for k in range(V):
        for i in range(V):
            if dist[i][k] != NO_EDGE:
                for j in range(V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist[src][dest]


def floyd2(g, src, dest):
    V = len(g)
    via = [[-1] * V for _ in range(V)]

    def calc(g):
        dist = deepcopy(g)
        for v in range(V):
            dist[v][v] = 0

        for k in range(V):
            for i in range(V):
                if dist[i][k] != NO_EDGE:
                    for j in range(V):
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            via[i][j] = k
                            dist[i][j] = dist[i][k] + dist[k][j]

        return dist

    def reconstruct_path(u, v, path):
        if via[u][v] == -1:
            path.append(u)
            if u != v:
                path.append(v)
        else:
            w = via[u][v]
            reconstruct_path(u, w, path)
            path.pop()
            reconstruct_path(w, v, path)

        return path

    dist = calc(g)
    path = reconstruct_path(src, dest, [])

    return dist[src][dest], path


if __name__ == '__main__':
    # test set 1
    graph1 = [[NO_EDGE] * 4 for _ in range(4)]
    connnect(graph1, 0, 1, 2)
    connnect(graph1, 0, 2, 12)
    connnect(graph1, 1, 3, 4)
    connnect(graph1, 2, 3, 3)

    # test set 2
    graph2 = [[NO_EDGE] * 7 for _ in range(7)]
    connnect(graph2, 0, 1, 5)
    connnect(graph2, 0, 2, 1)
    connnect(graph2, 2, 3, 2)
    connnect(graph2, 1, 3, 1)
    connnect(graph2, 3, 4, 5)
    connnect(graph2, 1, 5, 3)
    connnect(graph2, 1, 6, 3)
    connnect(graph2, 5, 6, 2)
    connnect(graph2, 3, 5, 3)


    # test_set = [graph1, graph2]
    test_set = [graph2]
    for i, g in enumerate(test_set):
        print('\n' + '-' * 30)
        print('Test', i+1, '/', len(test_set))
        print(floyd_prototype(g, 2, 5))

        print('\n' + '-' * 30)
        print('Test', i+1, '/', len(test_set))
        print(floyd(g, 2, 5))

        print('\n' + '-' * 30)
        print('Test', i+1, '/', len(test_set))
        print(floyd2(g, 0, 6))
