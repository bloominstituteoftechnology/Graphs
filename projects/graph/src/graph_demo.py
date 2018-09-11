#!/usr/bin/python
from graph import Graph
from draw import BokehGraph
import math
import random
"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv


def main():
    # randomize graph
    graph = Graph()
    
    #randomize vertices
    for i in range(1, random.randint(2, 10)):
        graph.addVertex(str(i))
    
    #randomize edges
    randomizeEdges(graph)

    myGraph = BokehGraph(graph)

    myGraph.show()

def randomizeEdges(graph):
    for vertex in graph.vertices:
        print(vertex)
        #check if has neighbors
        # if len(vertex) is 0:
            #no edges 
        numEdgesToAdd = random.randint(1,2)
        count = 0
        while count < numEdgesToAdd:
            v2 = graph.getRandomOtherVertex(vertex)
            graph.addEdge(vertex, v2)
            count += 1

if __name__ == '__main__':
    # TODO - parse argv
    main()


#code for nodes
        # if len(vertex.getNeighbors()) > 0:
        #     numNeighborsToAdd = random.randint(1,3)
        #     count = 0
        #     while count <= numNeighborsToAdd:
        #         vertex.addEdge()