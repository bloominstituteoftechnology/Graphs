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
    graph.add_directed_edge('5', '3')
    graph.add_directed_edge('6', '3')
    graph.add_directed_edge('7', '1')
    graph.add_directed_edge('4', '7')
    graph.add_directed_edge('1', '2')
    graph.add_directed_edge('7', '6')
    graph.add_directed_edge('2', '4')
    graph.add_directed_edge('3', '5')
    graph.add_directed_edge('2', '3')
    # graph.add_directed_edge('4', '6')
    print(graph.vertices)
    # graph.breadth_first_search('1')
    # graph.depth_first_search('1')
    # print(graph.recursive_dfs('1'), 'da stack')
    # print(graph.bfs_search('1', '7'))
    print(graph.dfs_search('1', '7'))


if __name__ == '__main__':
    # TODO - parse argv
    main()
