#!/usr/bin/python
from graph import Graph
"""
Demonstration of Graph functionality.
"""

from sys import argv


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'F')
    graph.add_edge('D', 'G')
    graph.add_edge('E', 'C')
    graph.add_edge('F', 'C')
    graph.add_edge('G', 'F')
    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_edge('0', '1')
    # graph.add_edge('0', '3')
    # print(graph.vertices)
    # print(graph.vertices['D'])
    # print(graph.depth_first_traversal(1))
    # print(graph.depth_first_traversal("A"))
    # print(graph.bredth_first_search("A", "B"))
    print(graph.depth_first_search("A", "B"))


if __name__ == '__main__':
    # TODO - parse argv
    main()
