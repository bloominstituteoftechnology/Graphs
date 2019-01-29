#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv
<<<<<<< HEAD
from graph import Graph
=======
>>>>>>> origin/master


def main():
    graph = Graph() # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_edge('0', '1')
    graph.add_edge('0', '2')
    graph.add_edge('0', '3')
<<<<<<< HEAD
    graph.add_edge('2', '3')
    graph.add_edge('3', '4')
    graph.add_edge('4', '5')
    print('Graph:', graph.vertices)
    print('BFT:', graph.bft('0'))
    print('DFT:', graph.dft('0'))
    print('DFT_R:', graph.dft_r('0'))
    print('BFS:', graph.bfs('0', '5'))
    print('DFS:', graph.dfs('0', '5'))
=======
    print(graph.vertices)
>>>>>>> origin/master

if __name__ == '__main__':
    # TODO - parse argv
    main()
