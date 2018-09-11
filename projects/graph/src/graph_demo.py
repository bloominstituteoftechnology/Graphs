#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
# from draw import BokehGraph


def main(vertexes = 4, edges = 6, directed=False, layout = 'circle', colors='orange', output=None, edge_prob=None):
    print('vertexes: ', vertexes)
    print('edges: ', edges)
    print('directed: ', directed)
    print('layout: ', layout)
    print('colors: ', colors)
    print('output: ', output)
    print('edge_prob: ', edge_prob)


if __name__ == '__main__':
    # TODO - parse argv

    print(*argv[1:])
    main(*argv[1:])
