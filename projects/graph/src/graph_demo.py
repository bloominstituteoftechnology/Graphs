#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph

# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }

def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    # graph.add_edge('0', '4') # raise IndexError("No vertex")
    print(graph.vertices)
    print(graph.bft('0'))
    print(graph.bft('2'))
    print(graph.dft_recursive('0'))
    print(graph.dft_recursive('2'))

if __name__ == '__main__':
    # TODO - parse argv
    # main(sys.argv[1:])
    main()