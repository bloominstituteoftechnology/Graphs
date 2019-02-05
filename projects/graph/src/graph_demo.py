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
    # graph.add_vertex('8')
    # graph.add_vertex('9')
    # graph.add_vertex('10')
    # graph.add_vertex('11')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('3', '4')
    graph.add_edge('4', '5')
    # graph.add_edge('1', '8')
    # graph.add_edge('0', '9')
    # graph.add_edge('9', '10')
    # graph.add_edge('10', '11')
    print(graph.vertices)
    print(graph.breadth_first_traversal("4"))
    print(graph.depth_first_traversal("4"))
    print(graph.depth_first_recursive("4"))

if __name__ == '__main__':
    # TODO - parse argv
    main()
