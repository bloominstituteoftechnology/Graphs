#!/usr/bin/python
from graph import Graph
"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv


def main():
    graph = Graph()  # Instantiate your graph
    '''graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    
    print(graph.vertices)'''

    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_directed_edge(1, 2)
    graph.add_directed_edge(2, 3)
    graph.add_directed_edge(2, 4)
    graph.add_directed_edge(3, 5)
    graph.add_directed_edge(4, 6)
    graph.add_directed_edge(4, 7)
    graph.add_directed_edge(5, 3)
    graph.add_directed_edge(6, 3)
    graph.add_directed_edge(7, 6)
    graph.add_directed_edge(7, 1)
    
    # print(graph.bft(1))
    # print(graph.dft(1))
    print(graph.bfs(1, 5))
if __name__ == '__main__':
    # TODO - parse argv
    main()
