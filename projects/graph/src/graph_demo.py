#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

def main(d,v,e):

    graph = Graph()  # Instantiate your graph
    
    # For all vertices, call .add()
    for v in range(0,int(v)):
        graph.add_vertex(str(v))
    
    
    verts = list(range(v+1))

    # For all edges, add edges
    for e in range(int(e)):    
        random.shuffle(verts)
        print(f"Shuffled verts: {verts}")
        if d == 'd':
            graph.add_directed_edge(str(verts[0]),str(verts[1]))
        else:
            graph.add_edge(str(verts[0]),str(verts[1]))
    
    print(graph.vertices)
    
    bg = BokehGraph(graph)
    
    bg.render()

if __name__ == '__main__':
    #Parse the argv
    if len(argv) != 4:
        raise ValueError("Incorrect number of args, directed/und, #vertices and #edges")
    else:
        main(argv[1],argv[2], argv[3])
