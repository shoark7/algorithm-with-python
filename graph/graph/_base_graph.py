class _BaseGraph:
    def __init__(self, n, name='graph', weight=1, directed=False):
        self.n_vector = n
        self.n_edge = 0
        self.name = name
        self.weight = weight
        self.directed = directed
        self.name_set = False

    def add_edge(self, src, dest, weight=1):
        raise NotImplementedError("Not implemented boy...")

    def edge_exists(self, src, dest):
        raise NotImplementedError("Not implemented boy...")

    def set_vector_names(self):
        """Later we'll assume vectors have names"""
        raise NotImplementedError("Not implemented boy...")

    def show_graph(self):
        for i in range(1, self.n_vector+1):
            print(f'{i} is connected to {self.graph[i]}')

    def vector_exists(self, src):
        return True if src <= self.n_vector + 1 else False

    def __repr__(self):
        return "Graph named '" + self.name + "'"
