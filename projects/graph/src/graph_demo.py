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
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_vertex('8')
    graph.add_edge('3', '0')
    graph.add_edge('1', '0')
    graph.add_edge('8', '0')
    graph.add_edge('0', '1')
    graph.add_edge('7', '1')
    graph.add_edge('3', '2')
    graph.add_edge('7', '2')
    graph.add_edge('5', '2')
    graph.add_edge('0', '3')
    graph.add_edge('2', '3')
    graph.add_edge('4', '3')
    graph.add_edge('3', '4')
    graph.add_edge('8', '4')
    graph.add_edge('6', '5')
    graph.add_edge('2', '5')
    graph.add_edge('5', '6')
    graph.add_edge('1', '7')
    graph.add_edge('2', '7')
    graph.add_edge('0', '8')
    graph.add_edge('4', '8')
    print(graph.vertices)
    graph.bf_traversal('0')
    graph.dft_stack('0')
    print("---NEARBY---target tests")
    graph.bfs_search('0', '8')
    graph.dfs_search('0', '8')
    print("---FAR AWAY---  target tests")
    graph.bfs_search('0', '6')
    graph.dfs_search('0', '6')


if __name__ == '__main__':
    # TODO - parse argv
    main()
