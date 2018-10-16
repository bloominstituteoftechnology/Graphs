# !/usr/bin/python
from graph import Graph
from draw import BokehGraph

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv


def main():
    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    print(graph.vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    print(graph.vertices)

    # keys = graph.vertices.keys()
    # print(list(keys), "24")
    BokehGraph(graph).show()

if __name__ == '__main__':
    # TODO - parse argv
    main()
