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
    graph.add_edge('0', '1')    # Add edge between 0 and 1, 1 and 0
    graph.add_edge('0', '3')    # Add edge between 0 and 3, 3 and 0
    graph.add_edge('2', '4')
    graph.add_edge('2', '5')
    graph.add_edge('5', '6')
    
    print(graph.vertices)
    
    graph.breadth_first_traversal('2')

if __name__ == '__main__':
    # TODO - parse argv
    main()
