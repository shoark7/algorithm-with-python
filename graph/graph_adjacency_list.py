"""Implement graph in an adjacency matrix form


There are two ways to implement graph.
One is 'adjacency matrix' form.

This implementation has some pros and cons.

Pros:
    1. Easy to implement

Cons:
    1. If Edges are sparse, too much spaces are wasted.
       In a matrix form, space takes of V**2. But even if you assume the graph
       is a complete graph, number of edges are (v-1)(v-2) / 2.

Now, I'm gonna make it.

Date : 2018/09/05
"""
class list_undirected_weight:
    """Graph in an adjacency list form

    Vertex number starts from '1'
    """
    def __init__(self, n):
        self.matrix = [[] for _ in range(n+1)]
        self.vector_n = len(self.matrix)

    def add_edge(self, src, dest, weight=1):
        self.matrix[src].append((dest, weight))
        self.matrix[dest].append((src, weight))
