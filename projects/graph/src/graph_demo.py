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
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('3', '2')
    graph.add_edge('3', '1')
    graph.add_edge('3', '0')

    print(graph.vertices)

    graph.breadth_first_traversal('0')

    print("\n")
    graph.depth_first_traversal_rec('0')

if __name__ == '__main__':
    # TODO - parse argv
    main()
