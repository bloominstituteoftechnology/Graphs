#!/usr/bin/env python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = defaultdict(set)
        pass
   

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        self.vertices[v2]
        pass

    @property
    def matrix(self):
        nodes = list(self.vertices.keys())
        n = len(nodes)
        mat = [[0 for _ in nodes] for _ in nodes]
        for tail in self.vertices.keys():
            tail_idx = nodes.index(tail)
            for head in self.vertices[tail]:
                head_idx = nodes.index(head)
                mat[tail_idx][head_idx] = 1

        return mat

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph

    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
