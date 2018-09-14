#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
# from graph import Graph
# from draw import BokehGraph


def main(**kwargs):
    print(kwargs)
    graph = Graph(vertices, edge_prob)
    graph.generate_vertices()
    graph.generate_edges()

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()

if __name__ == '__main__':
    # TODO - parse argv
    LAYOUT = 'default'
    NUM_VERTS = 4
    NUM_EDGES = 4
    COLOR = 'orange'
    for arg in argv[1:]:
        split_arg = arg.split("=")
        if len(split_arg) == 2:
            if split_arg[0] == 'layout':
                LAYOUT = split_arg[1].lower()
            elif split_arg[0] == 'vertices':
                NUM_VERTS = split_arg[1]
            elif split_arg[0] == 'edges':
                NUM_EDGES = split_arg[1]
            elif split_arg[0] == 'color':
                COLOR = split_arg[1].lower()
    main(layout = LAYOUT, num_verts = NUM_VERTS, num_edges = NUM_EDGES, color = COLOR)
