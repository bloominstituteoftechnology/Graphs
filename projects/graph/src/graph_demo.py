#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random


def main(arr, e_arr):
    g = Graph()
    g.add_vertex(arr)
    g.add_edges(e_arr)
    
    bg = BokehGraph(g)
    bg.show()

vertices = []
edges = []

for x in range(10):
    vertices.append(str(random.randint(1,31))) 
    print(vertices) 

for y in range(6): 
    for node in vertices[:-1]:
        if int(node) % 2 == 0:
            next = vertices.index(node)+1
            edge = {node, vertices[next]}
            print(edge)
            edges.append(edge)
main(vertices, edges)


#if __name__ == '__main__':
    # TODO - parse argv
    #main(vertices, edges)

