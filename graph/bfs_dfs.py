"""Implement DFS and BFS in Python"""
from graph_adjacency_list import list_undirected_weight
from graph_adjacency_matrix import matrix_undirected_weight


# DFS 1. Recursive way
def dfs_recursive(graph, x):
    print(x)
    check[x] = 1
    for i in range(1, graph.vector_n):
        if graph.matrix[x][i] == 1 and check[i] == 0:
            dfs_recursive(graph, i)


def dfs_stack(graph, x):
    pass


def bfs(graph, x):
    check[x] = 1
    queue.append(x)
    print(x)

    while queue:
        y = queue.pop(0)
        for i in range(1, graph.vector_n):
            if graph.matrix[y][i] == 1 and check[i] == 0:
                check[i] = 1
                queue.append(i)
                print(i)


if __name__ == '__main__':

    g = matrix_undirected_weight(5)
    g.add_edge(1, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(1, 5)
    g.add_edge(1, 5)
    g.add_edge(1, 5)


check = [0 for _ in range(1000)]
stack = []
queue = []

# dfs_recursive(g, 1)
check = [0 for _ in range(1000)]
bfs(g, 1)
