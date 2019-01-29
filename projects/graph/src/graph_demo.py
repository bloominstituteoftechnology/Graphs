#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from graph import Graph


def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_edge("B", "A")
    graph.add_edge("C", "B")
    graph.add_edge("D", "B")
    graph.add_edge("E", "C")
    graph.add_edge("A", "D")
    graph.add_edge("D", "E")
    print("breadth-first traversal:")
    graph.bf_traversal("A")
    print("")
    print("depth-first traversal:")
    graph.df_traversal("A")
    print("")
    print("depth-first traversal w/ recursion:")
    print(graph.recursive_dft("A"))
    print("")
    print("breath-first search:")
    print(graph.bf_search("A", "E"))
    print("")
    print("depth-first search:")
    print(graph.df_search("A", "9"))
    print("")
    print(graph.vertices)


if __name__ == "__main__":
    # TODO - parse argv
    main()
