#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from graph import Graph
from draw import BokehGraph
from sys import argv
import random


def main():
    randomgraph = Graph()
    def rand():
        return random.randint(1,11)
    for i in range(rand()):
        randomgraph.add_vertex(rand())
    def randedge():
        return random.randint(randomgraph.vertices.index(0), randomgraph.vertices.index(-1)
    for i in randomgraph.vertices:
        randomgraph.add_edge(i, randedge())
    boke = BokehGraph(randomgraph)


if __name__ == '__main__':
    # TODO - parse argv
    main()
