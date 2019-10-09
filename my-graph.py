from collections import defaultdict
from typing import List
from math import log

class Graph:
    """ directed unweighted graph """
    def __init__(self):
        self.vertices = defaultdict(set)
        pass

    def add_edge(self, v1: int, v2: int):
        """ add a directed edge. """
        self.vertices[v1].add(v2)
        self.vertices[v2]

        pass

    @property
    def matrix(self) -> List[List[int]]:
        """ adjacency matrix """
        nodes = list(self.vertices.keys())
        n = len(nodes)
        mat = [[0 for _ in nodes] for _ in nodes]
        for tail in nodes:
            tail_idx = nodes.index(tail)
            for head in self.vertices[tail]:
                head_idx = nodes.index(head)
                mat[tail_idx][head_idx] = 1

        return mat

    @property
    def num_edges(self) -> int:
        """ current number of edges """
        return sum(sum(row) for row in self.matrix)

    @property
    def num_vertices(self) -> int:
        """ current number of vertices """
        return len(self.vertices.keys())

    @property
    def density(self) -> float:
        """ current density """
        v = self.num_vertices
        return self.num_edges / (v * (v-1))

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph

    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    assert graph.num_edges == 4
    print(graph.density)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    print(graph.num_edges)
    print(graph.density)
