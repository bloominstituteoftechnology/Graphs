#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

def createDefaultGraph():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex(5)
    graph.add_vertex(2)
    graph.add_vertex(6)
    graph.add_vertex(1)
    graph.add_vertex(4)
    graph.add_vertex(7)
    graph.add_vertex(3)
    graph.add_edge(5, 2)
    graph.add_edge(5, 6)
    graph.add_edge(2, 1)
    graph.add_edge(2, 4)
    graph.add_edge(4, 3)
    graph.add_edge(6, 7)  

    print("DFT:")
    graph.dft(5)
    print("*********\nBFT:")
    graph.bft(5)

    bg = BokehGraph(graph)
    bg.draw()

def createRandomGraph(numNodes, numEdges):     

    graph = Graph()  # Instantiate your graph

    all_edges = []

    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            all_edges.append( (i, j) )

    random.shuffle(all_edges)
    edges = all_edges[:numEdges]

    for i in range(numNodes):
        graph.add_vertex(i)  
    
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    bg = BokehGraph(graph)
    bg.draw()

def main(style, numNodes, numEdges):
    if style == "default":
        createDefaultGraph()
    elif style == "random":
        createRandomGraph(numNodes, numEdges)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    style = "default"
    numNodes = random.randint(3,7)
    numEdges = random.randint(3,10)

    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "nodes":
                numNodes = int(arg_split[1])
            elif arg_split[0] == "edges":
                numEdges = int(arg_split[1])
            else:
                print("I don't understand that command.\n")

    main(style, numNodes, numEdges)

    
