#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

# Our boilerplate graph
def defaultGraph():
    graph = Graph() # Instantiates our graph

    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')

    graph.add_edge('1', '2')
    graph.add_edge('2', '3')
    graph.add_edge('3', '4')

    bg = BokehGraph(graph)
    bg.draw()


# Random graph that takes number of nodes and number of edges as args
def randomGraph(nNodes, nEdges):
    graph = Graph()
    all_the_edges = []

    for i in range(nNodes):
        for k in range(i + 1, nNodes):
            all_the_edges.append((i , k))

    # random.shuffle(all_the_edges)
    # edges = all_the_edges[:nEdges]

    edges = all_the_edges[:nEdges]

    #print the edges in all edges list

    for i in range(nNodes):
        graph.add_vertex(i)

    for edge in edges:
       print(edge)
       graph.add_edge(edge[0], edge[1])

    bg = BokehGraph(graph)
    bg.draw()

def main(style, nNodes, nEdges):
    # if our style is default call defaultGraph 
    if style == "default":
        defaultGraph()
    #if style if random call randomGraph and pass in nNodes and nEdges args
    elif style == "random":
        randomGraph(nNodes, nEdges)
    else:
        defaultGraph()
    


if __name__ == '__main__':
    # TODO - parse argv
    style = "default"
    nNodes = 4
    nEdges = 4

    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "nodes":
                nNodes = int(arg_split[1])
            elif arg_split[0] == "edges":
                nEdges = int(arg_split[1])
            else:
                print("Sorry, I don't understand that command.\n")

    main(style, nNodes, nEdges)
