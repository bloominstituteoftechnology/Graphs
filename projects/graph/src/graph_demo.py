#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('0', '5')
    graph.add_edge('5', '4')
    graph.add_edge('4', '2')
    graph.add_edge('0', '20')
    print(graph.vertices)

    graph.bft('2')
    graph.bft('0')

    graph.dft('0')

    graph.dft_r('0')

    graph.bfs('0', '2')


if __name__ == '__main__':
    # TODO - parse argv
    main()
