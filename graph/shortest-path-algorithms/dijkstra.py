from heapq import heappop, heappush
# Python's heapq is min-queue, unlike C++ priority_queue data structure
from math import inf


# Connect two vetcies in a graph with value 'v'. Undirected is default.
def connnect(graph, a, b, v, directed=False):
    graph[a][b] = v
    if not directed:
        graph[b][a] = v


def dijkstra(src, graph):
    # we suppose graph is matrix-based.
    N = len(graph)
    dist = [inf] * N
    dist[src] = 0
    pq = [(0, src)] # pq is a priority queue of (cost, vertex) tuples

    while pq:
        cost, here = heappop(pq)
        if dist[here] < cost:
            continue

        for there in range(N):
            if graph[here][there] != -1: # We suppose '-1' means 'not connected' here.
                next_dist = cost + graph[here][there]
                if dist[there] > next_dist:
                    dist[there] = next_dist
                    heappush(pq, (next_dist, there))
    return dist


if __name__ == '__main__':
    # test set 1
    graph1 = [[-1] * 4 for _ in range(4)]
    connnect(graph1, 0, 1, 2)
    connnect(graph1, 0, 2, 12)
    connnect(graph1, 1, 3, 4)
    connnect(graph1, 2, 3, 3)

    # test set 2
    graph2 = [[-1] * 7 for _ in range(7)]
    connnect(graph2, 0, 1, 5)
    connnect(graph2, 0, 2, 1)
    connnect(graph2, 2, 3, 2)
    connnect(graph2, 1, 3, 1)
    connnect(graph2, 3, 4, 5)
    connnect(graph2, 1, 5, 3)
    connnect(graph2, 1, 6, 3)
    connnect(graph2, 5, 6, 2)
    connnect(graph2, 3, 5, 3)


    test_set = [graph1, graph2]
    for i, g in enumerate(test_set):
        print('\n' + '-' * 30)
        print('Test', i+1, '/', len(test_set))
        print(dijkstra(0, g))
