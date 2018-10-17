#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

# Our boilerplate graph
def defaultGraph():
    graph = Graph() # Instantiates our graph

    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')

    graph.add_edge('0', '1')
    graph.add_edge('0', '4')
    graph.add_edge('1', '3')

    bg = BokehGraph(graph)
    bg.draw()

    


def main():
    pass  # TODO


if __name__ == '__main__':
    # TODO - parse argv
    main()
