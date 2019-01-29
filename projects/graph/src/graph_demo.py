#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_edge('0', '1')
    # graph.add_edge('0', '3')
    # print(graph.vertices)
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_vertex('8')
    graph.add_vertex('9')
    graph.add_edge('1', '6')
    graph.add_edge('1', '8')
    graph.add_edge('1', '2')
<<<<<<< HEAD
    graph.add_edge('6', '7')    
=======
    graph.add_edge('6', '7')
>>>>>>> f7307ef8e525814dee71ba130d8898701404cded
    graph.add_edge('8', '3')
    graph.add_edge('2', '3')
    graph.add_edge('7', '9')
    graph.add_edge('7', '5')
<<<<<<< HEAD
    graph.add_edge('9', '3')
    graph.add_edge('9', '5')
    graph.add_edge('3', '4')
    graph.add_edge('4', '5')

    print(graph.vertices)
    print('\n bfs_path')
    print(graph.bfs_path('1', '3'))
    print(graph.bfs_path('1', '7'))
    print(graph.bfs_path('8', '5'))
    print('\n dfs_path')
    print(graph.dfs_path('1', '4'))
    print(graph.dfs_path('8', '5'))
    print(graph.dfs_path('2', '5'))
=======
    graph.add_edge('9', '5')
    graph.add_edge('7', '9')
    graph.add_edge('3', '4')
    graph.add_edge('4', '5')

    # print(graph.vertices)

    print(graph.bfs_path('1', '3')) # correct
    print(graph.bfs_path('1', '7')) # correct
    print(graph.bfs_path('8', '5')) # correct
>>>>>>> f7307ef8e525814dee71ba130d8898701404cded

    

if __name__ == '__main__':
    # TODO - parse argv
    main()
