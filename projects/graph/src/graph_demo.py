#!/usr/bin/python
from graph import Graph
from draw import BokehGraph
import math
import random
"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv


def main(graphArgs = None):
    # randomize graph
    graph = Graph()
    
    #randomize vertices
    for i in range(0, random.randint(2, 11)):
        graph.addVertex(str(i))
    
    #randomize edges
    randomizeEdges(graph)
    if graphArgs: myGraph = BokehGraph(graph, graphArgs)
    else: myGraph = BokehGraph(graph)

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

def translateArg(fullArg):
    arr = fullArg.split('=')
    possArgs = {
        "title": "title",
        "t" : "title",
        # "x_range" : "x_range",
        # "x" : "x_range",
        # "y_range" : "y_range",
        # "y": "y_range",
        "tools" : "tools",
        "toolbar_location" : "toolbar_location"
        }

    if len(arr) > 1:
        argKey = arr[0]
        argVal = arr[1]
        if argKey in possArgs:
            return {possArgs[argKey] : argVal}
        else: 
            print("argument not found")
            return None

    else:
        print('invalid argument syntax, use an = to separate key and value')

if __name__ == '__main__':
    # TODO - parse argv
    graphArgs = {}

    if len(argv) > 1: 
        print(argv)
        newArgs = []
        for i, value in enumerate(argv):
            if i is not 0:
                argObj = translateArg(value)
                if argObj:
                    graphArgs.update(argObj)


    main(graphArgs)




#code for nodes
        # if len(vertex.getNeighbors()) > 0:
        #     numNeighborsToAdd = random.randint(1,3)
        #     count = 0
        #     while count <= numNeighborsToAdd:
        #         vertex.addEdge()