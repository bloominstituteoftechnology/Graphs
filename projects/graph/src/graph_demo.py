#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

# exploration with random functions
random.seed(123)
print(random.random())
#help(random.shuffle)
x = [2,4,6,8,10]
n = len(x)
x[:n]
random.shuffle(x)
print(x)

# make a graph with vertices and edges for demonstration purposes
def createTestGraph():
    graph = Graph() # instantiate the graph using the Graph class
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('1', '2')
    graph.add_edge('1', '4')

# create a random graph

def createRandomGraph(numVertices, numEdges):
    graph = Graph() #instantiate the graph

    all_edges = []
    # for each of the nodes, it is possible to connect to each of the other nodes except for itself
    for i in range(numVertices):
        for j in range(i+1, numVertices): # start at i+1 because the vertex is not connected to itself
            all_edges.append( (i, j) )
 
    random.shuffle(all_edges) # shuffle the array of edges
    edges = all_edges[:numEdges]

    if numEdges > len(all_edges): 
        print("warning:  Too many edges")

    for edge in edges:
        print(edge) # print all of the connections

    for i in range(numVertices):
        graph.add_vertex(i)
    
    for edge in edges:
        print(edge)
        graph.add_edge(edge[0], edge[1])

    print(len(edges))

    bg = BokehGraph(graph)
    bg.draw()    


# def main():
#     pass  # TODO


# if __name__ == '__main__':
#     # TODO - parse argv
#     main()
