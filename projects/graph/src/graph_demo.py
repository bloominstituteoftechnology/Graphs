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
    print("vertices:", graph.vertices)
    print("")
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
    graph2 = Graph()  # Instantiate your graph
    graph2.add_vertex("2")
    graph2.add_vertex("1")
    graph2.add_vertex("3")
    graph2.add_vertex("4")
    graph2.add_vertex("5")
    graph2.add_vertex("6")
    graph2.add_vertex("7")
    graph2.add_edge("4", "1")
    graph2.add_edge("2", "1")
    graph2.add_edge("3", "2")
    graph2.add_edge("4", "2")
    graph2.add_edge("5", "3")
    graph2.add_edge("6", "4")
    graph2.add_edge("7", "4")
    graph2.add_edge("3", "5")
    graph2.add_edge("3", "6")
    graph2.add_edge("1", "7")
    print("vertices:", graph2.vertices)
    print("")
    print("breath-first search:")
    print(graph2.bf_search("1", "6"))  # ['1', '4', '6']
    print("")
    print("depth-first search:")
    print(graph2.df_search("1", "6"))  # ['1', '4', '6'] or ['1', '2', '4', '6']


if __name__ == "__main__":
    # TODO - parse argv
    main()
