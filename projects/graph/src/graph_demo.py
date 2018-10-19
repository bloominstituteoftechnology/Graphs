#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
import random
import math
from graph import Graph
from draw import BokehGraph

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
    graph.add_edge(2, 1)
    graph.add_edge(4, 3)
    # graph.add_edge(5, 6)
    # graph.add_edge(2, 4)
    # graph.add_edge(6, 7)
    cc = graph.find_connected()
    bg = BokehGraph(graph, cc)
    bg.show()

def createRandomGraph(numNodes, numEdges):
    graph = Graph()  # Instantiate your graph
    all_edges = []

    # O(n^2)
    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            all_edges.append( (i,  j) )

    # O(n)
    random.shuffle(all_edges)
    edges = all_edges[:numEdges]

    # O(1)
    if numEdges > len(all_edges):
        print("Warning: Too many edges")

    # O(n)
    for i in range(numNodes):
        graph.add_vertex(i)

    # O(n)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])


    bg = BokehGraph(graph)
    bg.draw()


def main(style, numNodes,  numEdges):
    if style  == "default":
        createDefaultGraph()
    elif style  == "random":
        createRandomGraph(numNodes, numEdges)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    style = "default"
    numNodes = 5
    numEdges = 5

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

# def main(v, e):
#     graph = Graph()
#     for vertex in range(v):
#         graph.add_vertex(vertex)
#     edges = []
#     for i in range(v):
#         for j in range(v):
#             if i < j:
#                 edges.append((i,j))
#     random.shuffle(edges)
#     randomEdges = edges[:e]
#     for edge in randomEdges:
#         graph.add_edge(edge[0], edge[1])
#     # graph.dfs(0, 3)
#     bg = BokehGraph(graph)
#     # bg.show()


# if __name__ == '__main__':
#     # TODO - parse argv
#     main(6,3)