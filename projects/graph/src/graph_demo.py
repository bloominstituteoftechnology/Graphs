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

    graph.add_edge('0', '1')
    graph.add_edge('0', '4')
    graph.add_edge('1', '3')

    bg = BokehGraph(graph)
    bg.draw()


# Random graph that takes number of nodes and number of edges as args
def randomGraph(nNodes, nEdges)
    graph = Graph()
    all_the_edges = []

    for i in range(nNodes):
        for k in range(i + 1, nNodes):
            all_the_edges.append((i , k))

    # random.shuffle(all_the_edges)
    # edges = all_the_edges[:nEdges]

    edges = all_the_edges[:nEdges]

    #print the edges in all edges list
    for edge in edges:
        print(edge)

    for i in range(nNodes):
        graph.add_vertex(i)

   for edge in edges:
       print(edge)
       graph.add_edge(edge[0], edge[1])

    bg = BokehGraph(graph)
    bg.draw()

def main(style, nNodes, nEdges):
    # if our style is default call defaultGraph 
    if style = "default":
        defaultGraph()
    #if style if random call randomGraph and pass in nNodes and nEdges args
    elif style == "random"
        randomGraph(nNodes, nEdges)
    else:
        defaultGraph()
    


if __name__ == '__main__':
    # TODO - parse argv
    main()
