#!/usr/bin/env python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(**kwargs):
    bg = BokehGraph()  # Instantiate your graph
    bg.graph.add_vertex('0')
    bg.graph.add_vertex('1')
    bg.graph.add_vertex('2')
    bg.graph.add_vertex('3')
    bg.graph.add_vertex('4')
    bg.graph.add_vertex('5')
    bg.graph.add_vertex('6')
    bg.graph.add_vertex('7')
    bg.graph.add_vertex('8')
    bg.graph.add_vertex('9')
    bg.graph.add_edge('0', '1')
    bg.graph.add_edge('0', '3')
    bg.graph.add_edge('1', '2')
    bg.graph.add_edge('2', '5')
    bg.graph.add_edge('5', '8')
    bg.show()


if __name__ == '__main__':
    style = "default"
    num_verts = 5
    num_edges = 6
    for arg in argv[1::]:
        args = arg.split("=")
        if len(args) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            if arg_split[0] == "verts":
                num_verts = int(arg_split[1].lower())
            if arg_split[0] == "edges":
                num_edges = int(arg_split[1].lower())

    print(style)

    main(style=style, num_verts=num_verts, num_edges=num_edges)