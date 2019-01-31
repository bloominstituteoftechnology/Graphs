#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv
import time

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
    graph.add_edge('1', '2')    # Add edge between 0 and 1, 1 and 0
    graph.add_edge('2', '3')    # Add edge between 0 and 3, 3 and 0
    graph.add_edge('3', '5')
    graph.add_edge('2', '4')
    graph.add_edge('4', '6')
    graph.add_edge('4', '7')
    graph.add_edge('7', '1')
    graph.add_edge('7', '6')
    graph.add_edge('5', '3')
    graph.add_edge('6', '3')
    
    print(graph.vertices)

    start_time = time.time()
    
#    graph.breadth_first_traversal('2')
#    graph.depth_first_traversal('1')
#    graph.depth_first_recursion('6')
    print(graph.breath_first_search_path('1', '6'))
#    print(graph.depth_first_search_path('1', '6'))
    
    end_time = time.time()
    print (f"runtime: {end_time - start_time} seconds")

if __name__ == '__main__':
    # TODO - parse argv
    main()
