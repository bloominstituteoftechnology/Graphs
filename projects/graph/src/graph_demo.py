#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    # graph = Graph()  # Instantiate your graph
    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_vertex('4')
    # graph.add_vertex('5')
    # graph.add_vertex('6')
    # graph.add_vertex('7')
    # graph.add_edge('1', '2')
    # graph.add_edge('2', '3')
    # graph.add_edge('3', '2')
    # graph.add_edge('0', '4')
    # graph.add_edge('4', '5')
    # graph.add_edge('5', '2')
    # graph.add_edge('5', '6')
    # graph.add_edge('6', '7')
    # print(graph.vertices)
    # print("\n")
    # graph.bft(1) # cant start at 0 because no edges

    graph2 = Graph()
    graph2.add_vertex('0')
    graph2.add_vertex('1')
    graph2.add_vertex('2')
    graph2.add_vertex('3')
    graph2.add_vertex('4')
    graph2.add_vertex('5')
    graph2.add_edge('0', '3')
    graph2.add_edge('0', '1')
    graph2.add_edge('3', '5')
    graph2.add_edge('1', '4')
    print(graph2.vertices)
    print(graph2.bft("0"))
    print(graph2.dft("0"))
    print(graph2.dft_recursive("0"))

if __name__ == '__main__':
    # TODO - parse argv
    main()
