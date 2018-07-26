#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from draw import BokehGraph
from graph import Graph
from sys import argv
import random


def main():
    vertex_count = random.randint(0, 5) + 5
    graph = Graph()

    for i in range(vertex_count):
        graph.add_vertex(i)

    for start_vertex in graph.vertices:
        for end_vertex in graph.vertices:
            die_roll = random.random()
            if die_roll < .1 and start_vertex is not end_vertex:
                graph.add_edge(start_vertex, end_vertex, False)

    b = BokehGraph(graph)
    b.show()


if __name__ == "__main__":
    # TODO - parse argv
    main()
