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
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_edge('1', '2')
    graph.add_edge('2', '3')
    graph.add_edge('2', '4')
    graph.add_edge('3', '5')
    graph.add_edge('4', '6')
    graph.add_edge('4', '7')
    graph.add_edge('5', '3')
    graph.add_edge('6', '3')
    graph.add_edge('7', '6')
    graph.add_edge('7', '1')
    # graph.add_edge('3', '2')
    # graph.add_edge('3', '1')
    # graph.add_edge('3', '0')

    print(graph.vertices)

    graph.breadth_first_traversal('1')

    print("\n")
    graph.depth_first_traversal_rec('1')

    print("\n")
    shortest_path = graph.depth_first_search('0', '1')
    #print(shortest_path)

if __name__ == '__main__':
    # TODO - parse argv
    main()
