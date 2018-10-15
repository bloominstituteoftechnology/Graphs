#!/usr/bin/python
from graph import Graph
from draw import BokehGraph
from random import randint

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv


def main(numVertices=None):
    if numVertices is None:
        numVertices = randint(2,12)
    verticesList = list(range(0,numVertices))

    graphConstruct = Graph()

    for i in verticesList:
        graphConstruct.add_vertex(i)
    for i in verticesList:
        for chance in verticesList[i+1:]:
            if randint(1,4) ==1:
                graphConstruct.add_edge(i,chance)
    graphDisplay = BokehGraph(graphConstruct.vertices)
    graphDisplay.show()

if __name__ == '__main__':
    # TODO - parse argv
    main()
