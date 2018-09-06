from _base_graph import _BaseGraph


class _ListGraph(_BaseGraph):
    def __init__(self, n, name='List graph'):
        super().__init__(n, name)
        self.graph = [[] for _ in range(n+1)]

    def add_edge(self, src, dest, weight=1):
        if not self.edge_exists(src, dest):
            self.n_edge += 1
            self.graph[src].append((dest, weight))
        else:
            for i, tup in enumerate(self.graph[src]):
                if dest == tup[0]:
                    self.graph[src][i] = (dest, weight)

        if not self.directed:
            if not self.edge_exists(dest, src):
                self.n_edge += 1
                self.graph[dest].append((src, weight))
            else:
                for i, tup in enumerate(self.graph[dest]):
                    if src == tup[0]:
                        self.graph[dest][i] = (src, weight)

    def edge_exists(self, src, dest):
        for v, w in self.graph[src]:
            if dest == v:
                return True
        return False
