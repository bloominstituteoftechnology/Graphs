#!/usr/bin/python
from graph import Graph
from draw import BokehGraph
from random import randint
"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
import argparse


def main(numVertices=None, numEdges=None,color=None,style='square',arrows=None):
    if color is None:
        color='viridis'
    if style is None:
        style ='square'
    if numVertices is None:
        numVertices = randint(2, 12)
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
    graphDisplay = BokehGraph(graphConstruct.vertices)
    graphDisplay.show(style,color,arrows)


if __name__ == '__main__':
    # TODO - parse argv
    # print(argv[1])
    parser = argparse.ArgumentParser(description='Generate a graph!')
    parser.add_argument('--vertices', nargs='?', type=int,
                        help='number of vertices wanted (default is random)')
    parser.add_argument('--edges', nargs='?', type=int,
                        help='number of edges wanted (default is random)')
    parser.add_argument('--color', nargs='?', type=str,
                        help='pick the output color (specify color, or use viridis for random colors or use connectedOnly for connected highlighting')
    parser.add_argument('--style', nargs='?', type=str,
                        help='either circle,square, or random')
    parser.add_argument('--arrows',
                        help='if added will turn on arrows',action="store_true")
    args = parser.parse_args()
    main(args.vertices, args.edges,args.color,args.style,args.arrows)
