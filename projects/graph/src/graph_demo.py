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

# {
#     '0': {'1', '3'},
#     '1': {'0', '4'},
#     '2': set(),
#     '3': {'0', '5'}
#     '4': {'0', '1'}
#     '5': {'0', '3'}
# }

        # self.vertices = {
        #                   "A": {"B"},
        #                   "B": {"C", "D"},
        #                   "C": {"E"},
        #                   "D": {"F", "G"},
        #                   "E": {"C"},
        #                   "F": {"C"},
        #                   "G": {"A", "F"}
        #                 }

def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    # graph.add_vertex('3')     # checked if multiple values would be added
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    # graph.add_edge('0', '4') # raise IndexError("No vertex")
    print(graph.vertices)
    print(('*' * 10))
    print(graph.bft('0'))
    print(graph.bft('2'))
    print(('*' * 10))
    print(graph.dft('0'))
    print(graph.dft('2'))
    print(('*' * 10))
    print(graph.dft_recursive('0'))
    print(graph.dft_recursive('2'))
    print(('*' * 15))
    print(graph.bfs('0', '3'))
    print(graph.bfs('2', '2'))
    # print(('*' * 10))
    # print(graph.dfs('0', '3'))
    # print(graph.dfs('2', '2'))
    # print(('*' * 10))
    # print(graph.dfs_recursive('0', '3'))
    # print(graph.dfs_recursive('2', '2'))
    print(('*' * 20))
    graph2 = Graph()  # Instantiate your graph
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
    # graph.add_edge('0', '4') # raise IndexError("No vertex")
    print(graph2.vertices)
    print(('*' * 10))
    print(graph2.bft('0'))
    print(graph2.bft('2'))
    print(('*' * 10))
    print(graph2.dft('0'))
    print(graph2.dft('2'))
    print(('*' * 10))
    print(graph2.dft_recursive('0'))
    print(graph2.dft_recursive('2'))
    print(('*' * 15))
    print(graph2.bfs('0', '5'))
    print(graph2.bfs('2', '5'))
    print(('*' * 10))
    # print(graph2.dfs('0', '5'))
    # print(graph2.dfs('2', '5'))
    # print(('*' * 10))
    # print(graph2.dfs_recursive('0', '5'))
    # print(graph2.dfs_recursive('2', '5'))

if __name__ == '__main__':
    # TODO - parse argv
    # main(sys.argv[1:])
    main()