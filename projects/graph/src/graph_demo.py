#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph


def main():
    graph = Graph()  # Instantiate your graph

    #Vertices
    for i in range(0, 10):
        graph.add_vertex(str(i))

    #Edges
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('1', '2')
    graph.add_edge('2', '5')
    graph.add_edge('2', '4')
    graph.add_edge('4', '9')
    graph.add_edge('3', '7')
    graph.add_edge('3', '6')

    # graph.add_edge('0', '8')
    # graph.add_edge('8', '128')
    # graph.add_edge('128', '120')
    # graph.add_edge('120', '0')

    # graph.add_edge('8', '100')
    # graph.add_edge('0', '96')
    # graph.add_edge('120', '156')
    # graph.add_edge('128', '160')


    # graph.add_edge('96', '100')
    # graph.add_edge('100', '160')
    # graph.add_edge('160', '156')
    # graph.add_edge('156', '96')

    # graph.add_edge('100', '146')
    # graph.add_edge('96', '144')
    # graph.add_edge('156', '174')
    # graph.add_edge('160', '176')

    # graph.add_edge('144', '146')
    # graph.add_edge('146', '176')
    # graph.add_edge('176', '174')
    # graph.add_edge('174', '144')

    # dft(graph.vertices, '8', [])
    # dfs(graph.vertices, '8', [], '128')
    # graph.bft(graph.vertices, '0')

    bokeh_graph = BokehGraph(graph)

    bokeh_graph.draw()


if __name__ == '__main__':
    # TODO - parse argv
    main()
