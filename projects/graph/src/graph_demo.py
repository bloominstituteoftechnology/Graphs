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
        return random.randint(1,20)
    for i in range(rand()):
        randomgraph.add_vertex(rand())
    def randnode():
        index = random.randint(0, len(randomgraph.vertices)-1)
        nodes = list(randomgraph.vertices.keys())
        return nodes[index]
    for i in randomgraph.vertices.keys():
        randomgraph.vertices[i].add_edge(randnode())
    boke = BokehGraph(randomgraph)


if __name__ == '__main__':
    # TODO - parse argv
    main()
