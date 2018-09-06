from _base_graph import _BaseGraph


class _MatrixGraph(_BaseGraph):
    def __init__(self, n, name='Matrix graph'):
        super().__init__(n, name)
        self.graph = [[0 for _ in range(self.n_vector+1)] for _ in range(self.n_vector+1)]

    def add_edge(self, src, dest, weight=1):
        # 1 directed vs undirected

        if not self.graph[src][dest]:
            self.n_edge += 1
        self.graph[src][dest] = weight

        if not self.directed:
            if not self.graph[dest][src]:
                self.n_edge += 1
            self.graph[dest][src] = weight

    def edge_exists(self, src, dest):
        return True if self.graph[src][dest] else False
