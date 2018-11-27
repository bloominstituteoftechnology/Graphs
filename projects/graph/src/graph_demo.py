#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from graph import Graph
from sys import argv

def main():
    graph = Graph()
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
    

if __name__ == '__main__':
    # TODO - parse argv
    main()
