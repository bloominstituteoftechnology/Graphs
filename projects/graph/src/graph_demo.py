from graph import Graph

"""
Demonstration of Graph functionality.
"""

from sys import argv


def main():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_edge('0', '1')
    graph.add_edge('0', '2')
    graph.add_edge('2', '3')
    graph.add_edge('3', '4')
    graph.add_edge('3', '5')
    graph.add_edge('4', '6')
    print(graph.vertices)
    graph.bft('0')
    print("")
    graph.dft_recursive('0')
    print("")
    graph.dft_stack('0')


if __name__ == '__main__':
    # TODO - parse argv
    main()
