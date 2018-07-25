#!/usr/bin/python
from draw import BokehGraph
from random import sample
from sys import argv
from graph import Graph
"""
Simple graph implementation compatible with BokehGraph class.
"""
# graph.add_edge('A', 'B')
# graph = {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
    # TODO
        self.vertices = {}

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Start and or end doesn't exist here")
        else:
            self.vertices[start].add(end)
            if bidirectional == True:
                self.vertices[end].add(start)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            raise ValueError("that vertex already exists")

def main():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')
    graph.add_vertex('H')
    graph.add_edge('B', 'C')
    graph.add_edge('A', 'H')
    graph.add_edge('D', 'G')

    bg = BokehGraph(graph)
    bg.show()

if __name__ == "__main__":
    main()
