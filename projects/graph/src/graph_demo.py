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
    for i in range(5):
        graph.add_vertex(str(i))
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('2', '4')

    bg = BokehGraph(graph)
    bg.draw()



def createRandomGraph(numNodes, numEdges):
    graph = Graph() #Instantiate your graph

    all_edges = []

    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            all_edges.append((i,j))
    

    random.shuffle(all_edges)
    edges = all_edges[:numEdges]

    if numEdges > len(all_edges):
        print("Warning: Too many edges")

    for edge in edges:
        print(edge)

    for i in range(numNodes):
        graph.add_vertex(i)
    
    for edge in edges:
        print(edge)
        graph.add_edge(edge[0], edge[1])
    print(len(edges))

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
    numNodes = 5
    numEdges = 5
    """
    a = [0, 1, 2, 3]
    b = a[1:]
    b = [1, 2, 3]
    """
    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "nodes":
                numNodes = int(arg_split[1])
            elif arg_split[0] == "edges":
                numEdges = int(arg_split[1])
            else:
                print("I don't understand that command")
    print('style:', style, 'numNodes:', numNodes, 'numEdges:', numEdges)
    print(main(style,numNodes,numEdges))