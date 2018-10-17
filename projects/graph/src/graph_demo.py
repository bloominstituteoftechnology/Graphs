#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from graph import Graph
from draw import BokehGraph
from sys import argv
import random

def createDefaultGraph():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '2')
    graph.add_edge('1', '3')

    bg = BokehGraph(graph)
    bg.draw()

def main():
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
                print("Cannot do that")
    
    main(style, numNodes, numEdges)
