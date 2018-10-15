#!/usr/bin/python
from graph import Graph
from draw import BokehGraph
from random import randint
"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv


def main(numVertices=None,numEdges=None):
    if numVertices is None:
        numVertices = randint(2,12)


    verticesList = list(range(0,numVertices))

    if numEdges is None:
        numEdges = 0
        for num in verticesList:
            numEdges += randint(0,num)
            numEdges -= randint(0,int(num*.5))


    graphConstruct = Graph()

    for i in verticesList:
        graphConstruct.add_vertex(i)
        
    while(numEdges >= 0):
        ranNum1 = randint(0,numVertices-1)
        ranNum2 = randint(0,numVertices-1)
        if ranNum2 not in graphConstruct.vertices[ranNum1]:
            graphConstruct.add_edge(ranNum1,ranNum2)
            numEdges -=1

    graphDisplay = BokehGraph(graphConstruct.vertices)
    graphDisplay.show()

if __name__ == '__main__':
    # TODO - parse argv
    # print(argv[1])
    main()
