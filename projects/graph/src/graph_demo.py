#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')

    graph.add_edge('1', '2')
    graph.add_edge('2', '4')
    graph.add_edge('2', '5')
    graph.add_edge('1', '3')
   
    # graph.add_edge('0', '4')
    # graph.add_vertex('2')

    print(graph.vertices)

    graph.bft('1')

    graph.dft('1')

if __name__ == '__main__':
    # TODO - parse argv
    main()
