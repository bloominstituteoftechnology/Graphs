#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph

def createDefaultGraph():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_edge('0', '1')
    graph.add_edge('0', '2')
    graph.add_edge('1', '3')
    graph.add_edge('2', '4')
    graph.add_edge('3', '5')

    bg = BokehGraph(graph)
    bg.draw()

def createRandomGraph(numNodes, numEdges):
    numNodes = 5
    all_edges = []

    graph = Graph()

    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            edges.append((i, j))
    
    random.shuffle(all_edges)

    edges = all_edges[:numEdges]

    if numEdges > len(all_edges):
        print("To many edges")

    for edge in edges:
        print(edge)

    for i in range(numNodes):
        graph.add_vertex(i)
    
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    bg = BokehGraph(graph)
    bg.draw()

def main(style, numNodes, numEdges):
    if style == 'default':
        createDefaultGraph()
    elif style == 'random':
        createRandomGraph(numNodes, numEdges)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    style = 'default'
    numNodes = 5
    numEdges = 5

    for arg in argv[1:]:
        arg_split = arg.split('=')
        if len(arg_split) == 2:
            if arg_split[0] == 'style':
                style = arg_split[1].lower()
            elif arg_split[0] =='nodes':
                numNodes = int(arg_split[1])
            elif arg_split[0] == 'edges':
                numEdges = int(arg_split[1])
            else:
                print("I dont understand that commmand")
