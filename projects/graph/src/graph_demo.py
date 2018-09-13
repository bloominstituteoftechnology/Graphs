#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

def getDefaultGraph():
    graph = Graph()
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 5)
    graph.add_edge(2, 4)
    graph.add_edge(4, 9)
    graph.add_edge(3, 7)
    graph.add_edge(3, 6)

    return graph

def getRandomGraph(numVerts, numEdges):
    graph = Graph()

    for vert_id in range(0, numVerts):
        graph.add_vertex(vert_id)

    allEdges = []

    for i in range(0, numVerts):
        for j in range(0, numVerts):
            if i < j:
                allEdges.append( (i,j) )

    random.shuffle(allEdges)
    randomEdges = allEdges[:numEdges]

    for edge in randomEdges:
        graph.add_edge(edge[0], edge[1])

    return graph

def main(**kwargs):
    style = kwargs["style"]
    numVerts = kwargs["num_verts"]
    numEdges = kwargs["num_edges"]

    if style == "default":
        graph = getDefaultGraph()
    elif style == "random":
        graph = getRandomGraph(numVerts, numEdges)
    else:
        graph = getDefaultGraph()
    
    # graph.breadth_first(2)

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
