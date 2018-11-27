#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph


def main():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
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
    print("BFT")
    graph.bft(1)
    print("DFT")
    graph.dft(1)
    print("Recursive")
    graph.dft_r(1)
    print("BFS")
    print(graph.bfs(2, 5))
    print("DFS")
    print(graph.dfs(2, 5))


if __name__ == '__main__':
    # TODO - parse argv
    main()
