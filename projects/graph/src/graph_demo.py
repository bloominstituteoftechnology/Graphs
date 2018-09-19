#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph


def main():
    # create graph
    graph = Graph()

    # Add vertexes
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)

    # add edges
    graph.add_edge(1, 2)
    graph.add_edge(2, 1)
    graph.add_edge(2, 6)
    graph.add_edge(3, 5)
    graph.add_edge(5, 6)
    graph.add_edge(5, 6)
    graph.add_edge(6, 5)

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    style = "default"
    num_verts = 5
    num_edges = 6

    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "verts":
                num_verts = int(arg_split[1])
            elif arg_split[0] == "edges":
                num_edges = int(arg_split[1])

    main(style=style, num_verts=num_verts, num_edges=num_edges)
