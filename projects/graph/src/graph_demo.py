#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph


    # g = Graph()
    # g.add_vertex('0')
    # g.add_vertex('1')
    # g.add_vertex('2')
    # g.add_vertex('3')
    # g.add_vertex('4')
    # g.add_edge('0', '1')
    # g.add_edge('0', '3')
    # g.add_edge('0', '3')
    # g.add_edge('4', '3')
    # bg = BokehGraph(g)
    # bg.show()

def main(**kwargs):
    if style == 'default':
        graph = getDefaultGraph()
    elif style == 'random':
        graph = getRandomGraph()
    else:
        graph = getDefaultGraph()
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.draw()

if __name__ == '__main__':
    
    style='default'
    num_verts = 5
    num_edges = 6

    for arg in argv[1:]:
        arg_split = arg.split('=')
        if len(arg_split) == 2:
            if arg_split[0] == 'style':
                style = arg_split[1].lower()
            elif arg_split[0] == 'verts':
                num_verts = int(arg_split[1])
            elif arg_split[0] == 'edges':
                num_verts = int(arg_split[1])

    main(style='style', num_verts=num_verts, num_edges=num_edges)
