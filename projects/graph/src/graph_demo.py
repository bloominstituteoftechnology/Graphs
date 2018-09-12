#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

def main(v,e):

    graph = Graph()  # Instantiate your graph
    for v in range(0,int(v)):
        graph.add_vertex(str(v))
    print(graph.vertices)
    for e in range(1,int(e)):
        verts = list(range(v+1))
        random.shuffle(verts)
        print(f"Shuffled verts: {verts}")
        # rand_par = shuffled_verts[0]
        # rand_chi = shuffled_verts[1]

        # print(f"Rand Parent: {rand_par}")
        # print(f"Rand Child: {rand_chi}")
        graph.add_edge(str(verts[0]),str(verts[1]))
    print(graph.vertices)
    bg = BokehGraph(graph)
    bg.render()

if __name__ == '__main__':
    #Parse the argv
    if len(argv) == 1:
        raise ValueError("Please enter the number of vertices and edges")
    elif len(argv) == 2:
        raise ValueError("Please enter the number of edges as the second argument")
    elif len(argv) > 3:
        raise ValueError("Too many arguments, expecting only two, vertices and edges")
    else:
        main(argv[1],argv[2])
