#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv
from graph import Graph

def main():
    graph = Graph() #my graph instance
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('4', '3')
    print(graph.vertices)


if __name__ == '__main__':
    # TODO - parse argv
    main()
