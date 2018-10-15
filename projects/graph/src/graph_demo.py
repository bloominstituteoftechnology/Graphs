#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import sys
from graph import Graph
from draw import BokehGraph
from images import getGraph
from random import randint
from bokeh.palettes import Viridis256

def getDefaultGraph():
    graph = Graph()
    for i in range(10):
        graph.add_vertex(i)
    for i in range(10):
        graph.add_edge(i, i % 5)

    return graph

def getRandomGraph(num_verts, num_edges, connected=False):
    graph = Graph()
    vertices = num_verts
    edges = num_edges

    # Add vertices
    for n in range(0, vertices):
        graph.add_vertex(n)

    # Add Edges
    edgesOut = []
    while len(edgesOut) < edges:
        starting = randint(0, vertices - 1)
        ending = randint(0, vertices - 1)
        if starting != ending and (starting, ending) not in edgesOut and (ending, starting) not in edgesOut:
            edgesOut.append((starting,ending))

    for edge in edgesOut:
        graph.add_edge(edge[0], edge[1])  
           
    # Color connected components the same color
    if connected:
        vertices = list(graph.vertices.keys())[:]
        node_color = 0
        while vertices:
            group = graph.breadth_first_for_each(vertices[0])
            node_color += 20
            for node in group:
                graph.vertices[node].color = Viridis256[node_color % 256]
            
            vertices = [i for i in vertices if i not in group]

    return graph

def main(**kwargs):
    style = kwargs["style"]
    numVerts = kwargs["num_verts"]
    numEdges = kwargs["num_edges"]

    if style == "default":
        graph = getDefaultGraph()
    elif style == "random":
        graph = getRandomGraph(numVerts, numEdges)
    elif style == 'awesome':
        graph = getGraph('awesome')
    elif style == 'radiohead':
        graph = getGraph('radiohead')
    elif style == 'bender':
        graph = getGraph('bender')
    elif style == 'lambda_logo':
        graph = getGraph('lambda_logo')
    elif style == 'connected':
        graph = getRandomGraph(numVerts, numEdges, 'connected')
    else:
        graph = getDefaultGraph()

    bokeh_graph = BokehGraph(graph)

    bokeh_graph.show()


if __name__ == '__main__':
    style="default"
    num_verts = 15
    num_edges = 6

    for arg in sys.argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "verts":
                num_verts = int(arg_split[1])
            elif arg_split[0] == "edges":
                num_edges = int(arg_split[1])
    # Check edge numbers
    max_edges = 0
    for num in range(num_verts):
        max_edges += num
    if num_edges > max_edges:
        print("Maximum number of edges exceeded!")
    else:
        main(style=style, num_verts=num_verts, num_edges=num_edges)

