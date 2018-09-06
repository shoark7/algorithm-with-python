"""Implement DFS and BFS in Python"""
from graph_adjacency_list import list_undirected_weight
from graph_adjacency_matrix import matrix_undirected_weight


# DFS 1. Recursive way
def dfs_recursive(graph, x):
    _check = [0 for _ in range(graph.vector_n+1)]
    _check[x] = 1
    print(x)

    def _recursive(graph, x):
        for i in range(1, graph.vector_n+1):
            if graph.matrix[x][i] == 1 and _check[i] == 0:
                print(i)
                _check[i] = 1
                _recursive(graph, i)

    _recursive(graph, x)


# DFS 2. Stack way
def dfs_stack(graph, x):
    _check = [0 for _ in range(graph.vector_n+1)]
    stack = []
    _check[x] = 1
    stack.append(x)
    print(x)

    while stack:
        n = stack[-1]
        for i in range(1, graph.vector_n+1):
            found = False
            if graph.matrix[n][i] == 1 and _check[i] == 0:
                print(i)
                _check[i] = 1
                stack.append(i)
                found = True
                break
        if not found:
            stack.pop()


# BFS
def bfs(graph, x):
    check[x] = 1
    queue.append(x)
    print(x)

    while queue:
        y = queue.pop(0)
        for i in range(1, graph.vector_n+1):
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


queue = []
dfs_recursive(g, 1)
print()
dfs_stack(g, 1)
print()
check = [0 for _ in range(1000)]
bfs(g, 1)
