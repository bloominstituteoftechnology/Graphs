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
    graph.add_vertex('4')    
    graph.add_vertex('5')
    graph.add_vertex('6')
    
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('1', '2')
    graph.add_edge('2', '4')
    graph.add_edge('4', '5')
    graph.add_edge('5', '6')
        

    graph.dbft(-1)
    bg = BokehGraph(graph)
    bg.draw()

def createRandomGraph(numNodes):
    graph = Graph()

    edges = []
    
    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            edges.append((i , j))
    
    random.shuffle(edges)
    edges=[edge for index, edge in enumerate(edges) if 1 < index < random.randrange(2, len(edges))]
    

    
    for i in range(numNodes):
        graph.add_vertex(i)
    
    for edge in edges:
        graph.add_edge(edge[0], edge[1])


    bg = BokehGraph(graph)
    bg.draw()
    
def main(style, numNodes, edges):
    if style == 'default':
        createDefaultGraph()
    elif style == 'random':
        createRandomGraph(numNodes)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    style = 'default'
    numNodes = 2
    edges = 1
    
    for arg in argv:
        arg_split = arg.split('=')
        if len(arg_split) == 2:
            if arg_split[0] == 'style':
                style = arg_split[1].lower()
            elif arg_split[0] == 'nodes':
                if arg_split[1] == 'random':
                    numNodes = random.randrange(2,20)
                else:
                    numNodes = int(arg_split[1])
            elif arg_split[0] == 'edges':
                edges = int(arg_split[1])
            else: 
                print("I don't understand that command")


    main(style, numNodes, edges)
