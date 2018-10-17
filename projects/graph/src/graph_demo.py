#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

def createDefaultGraph():
    graph = Graph()  
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('1', '2')

    bg = BokehGraph(graph)
    bg.draw()

def createRandomGraph(numNodes):
    graph = Graph()

    for i in range(numNodes):
        graph.add_vertex(i)
    
    bg = BokehGraph(graph)
    bg.draw()
    
def main(style, numNodes):
    if style == 'default':
        createDefaultGraph()
    elif style == 'random':
        createRandomGraph(numNodes)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    style = 'default'
    numNodes = 2
    
    for arg in argv:
        arg_split = arg.split('=')
        if len(arg_split) == 2:
            if arg_split[0] == 'style':
                style = arg_split[1].lower()
            elif len(arg_split) == 2:
                if arg_split[0] == 'nodes':
                    if arg_split[1] == 'random':
                        numNodes = random.randrange(1,20)
                    else:
                        numNodes = int(arg_split[1])
            else: 
                print("I don't understand that command")
            

    main(style, numNodes)
