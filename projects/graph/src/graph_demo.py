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
    graph.add_edge('7', '1')
    graph.add_edge('7', '6')

    # graph.add_vertex('2')
    # graph.add_edge('0', '4')
    # graph.add_edge('1', '10')

    print(graph.vertices)

    # graph.bft('1')

    # graph.dft('1')

    # graph.dft_r('1')

    # print(graph.bfs('1', '6'))

    # print(graph.dfs('1', '6'))

    print(graph.bfs_p('1', '5'))



if __name__ == '__main__':
    # TODO - parse argv
    main()
