#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv
from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    # graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    # graph.add_edge('0', '1')
    # graph.add_edge('0', '3')
    # graph.add_edge('1', '3')
    # graph.add_edge('1', '2')
    # graph.add_edge('2', '3')
    # graph.add_edge('3', '1')
    graph.add_edge('1', '2')
    graph.add_edge('2', '3')
    graph.add_edge('2', '4')
    graph.add_edge('3', '5')
    graph.add_edge('5', '3')
    graph.add_edge('4', '6')
    graph.add_edge('4', '7')
    graph.add_edge('6', '3')
    graph.add_edge('7', '6')
    graph.add_edge('7', '1')
    # graph.add_edge('1', '4')  # throws error - doesnt add 4
    # graph.add_edge('5', '3')  # throws error - doesnt add 5
    print(f"Adjacency List -> {graph.vertices}")
    print(graph.bft('1'))
    print(graph.dft('1'))
    print('DFT_REC NODES VISITED:')
    print(graph.dft_rec('1'))
    print(graph.bfs('7', '5'))  # False
    # print(graph.bfs('1', '3'))  # True


if __name__ == '__main__':
    # TODO - parse argv
    main()
