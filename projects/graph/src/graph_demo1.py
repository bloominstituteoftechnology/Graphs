#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random
from sys import argv
from graph1 import Graph
from draw1 import BokehGraph

def getDefaultGraph():
    graph = Graph() #Instantiate your graph
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
    graph.add_edge(0,1)
    graph.add_edge(0,3)

    graph.add_edge(1,2)
    graph.add_edge(2,5)
    graph.add_edge(2,4)
    graph.add_edge(4,9)
    graph.add_edge(3,7)
    graph.add_edge(3,6)
    graph.add_edge(7,9)

    return graph

#what's the big O of the getRandomGraph method?
def getRandomGraph(numVerts, numEdges):
    graph = Graph() #Instantiate your graph
    
    for vert_id in range(0,numVerts):
        graph.add_vertex(vert_id)
    
    #O(n^2)
    allEdges = []
    for i in range(0,numVerts):
        for j in range(0, numVerts):
            if i < j: #it will only allow if the second number bigger than the first so that only one edge will be drawn between the elements 1 and 2, for example, instead of two
                allEdges.append( (i,j) )
    #challenge question: max numbers of edges? n*(n-1)/2
    # print(len(allEdges))

    #Interview question: how would you shuffle and what is the big O of that?
    #O(1)
    random.shuffle(allEdges)
    #O(e) where e = # edges (and we know e < n^2)
    randomEdges = allEdges[:numEdges]

    for edge in randomEdges:
        graph.add_edge(edge[0], edge[1])

    return graph

def main(**kwargs):
    print(kwargs)

    style = kwargs["style"]
    numVerts = kwargs["num_verts"]
    numEdges = kwargs["num_edges"]

    if style == "default":
        graph = getDefaultGraph()
    elif style == "random":
        graph = getRandomGraph(numVerts, numEdges)
    else:
        graph = getDefaultGraph()

    # graph.dft(0)
    # graph.bft(0)
    # print(graph.dfs(0,4))
    # print(graph.dfs(0,8))
    print(graph.dfs_path(0,5))

    bokeh_graph = BokehGraph(graph)

    bokeh_graph.drawGraph()


if __name__ == '__main__':
    # TODO - parse argv
    # print(argv)

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
    print(style)
    main(style=style, num_verts=num_verts, num_edges=num_edges)