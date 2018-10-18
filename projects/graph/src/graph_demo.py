#!/usr/bin/python
from graph import Graph
from draw import BokehGraph
from random import randint
"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
import argparse


def main(numVertices=None, numEdges=None, color=None, style='square', arrows=None, groupColor=None):
    colorGroups = []

    if color is None:
        color = 'viridis'
    if style is None:
        style = 'square'
    if numVertices is None:
        numVertices = randint(3, 12)
    verticesList = list(range(0, numVertices))
    if numEdges is None:
        numEdges = 0
        for num in verticesList:
            numEdges += randint(0, num)
            numEdges -= randint(0, int(num*.5))
    if (numVertices*(numVertices+1))/2 < numEdges:
        print('Invalid number of edges')
        return
    graphConstruct = Graph()

    for i in verticesList:
        graphConstruct.add_vertex(i)

    while(numEdges >= 0):
        ranNum1 = randint(0, numVertices-1)
        ranNum2 = randint(0, numVertices-1)
        if ranNum2 not in graphConstruct.vertices[ranNum1] and ranNum1 != ranNum2:
            graphConstruct.add_edge(ranNum1, ranNum2)
            numEdges -= 1
    if groupColor is True:
        for key in graphConstruct.vertices:
            toAdd = graphConstruct.returnAllPath(key)
            if toAdd not in colorGroups:
                colorGroups.append(toAdd)
    graphDisplay = BokehGraph(graphConstruct.vertices)
    graphDisplay.show(style, color, arrows, colorGroups)


if __name__ == '__main__':
    # TODO - parse argv
    # print(argv[1])
    parser = argparse.ArgumentParser(description='Generate a graph!')
    parser.add_argument('-v', '--vertices', nargs='?', type=int,
                        help='number of vertices wanted (default is random)')
    parser.add_argument('-e', '--edges', nargs='?', type=int,
                        help='number of edges wanted (default is random)')
    parser.add_argument('-c', '--color', nargs='?', type=str,
                        help='pick the output color (specify color, or use viridis for random colors or use connectedOnly for connected highlighting')
    parser.add_argument('-s', '--style', nargs='?', type=str,
                        help='either circle,square, or random')
    parser.add_argument('-a', '--arrows',
                        help='if added will turn on arrows', action="store_true")
    parser.add_argument('-g', '--groupColor',
                        help='colors each connection group', action="store_true")
    args = parser.parse_args()
    main(args.vertices, args.edges, args.color,
         args.style, args.arrows, args.groupColor)
