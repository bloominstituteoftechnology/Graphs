#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph

def main():
    graph = Graph()

    graph.add_vertex('0', 1, 3, '#777C00')
    graph.add_vertex('1', 4, 6, '#3F0000')
    graph.add_vertex('2', 7, 2, '#E80048')
    graph.add_vertex('3', 2, 9, '#FFBEBD')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    # TODO - parse argv
    main()
