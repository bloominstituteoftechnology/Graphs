#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random
from sys import argv
from graph import Graph
from draw import BokehGraph

def main(num_vertices=None, num_edges=None, connected=None):
    if num_vertices is None:
        num_vertices = random.randint(1, 20)
    else:
        num_vertices = int(num_vertices)
    if num_edges is None:
        num_edges = num_vertices
    elif int(num_edges) > num_vertices*(num_vertices-1)/2:
        num_edges = num_vertices*(num_vertices-1)//2
    else:
        num_edges = int(num_edges)
    if connected == 'yes':
        connected = True
    else:
        connected = False
    
    all_edges = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            all_edges.append( (i,  j) )
  
    random.shuffle(all_edges)
    edges = all_edges[:num_edges]
 
    graph = Graph()
    for num in range(num_vertices):
        graph.add_vertex(num)

    for edge in edges:
        graph.add_edge(edge[0], edge[1])
  
    connected_components = graph.connected_components()

    bg = BokehGraph(graph, connected_components, connected)
    bg.draw()

NUM_VERTICES = input("\nNumber of vertices (int)? ")
NUM_EDGES = input("\nNumber of edges (int)? ")
CONNECTED = input("\nColor connected components (yes/no)? ")
if NUM_VERTICES == "":
    NUM_VERTICES = None
if NUM_EDGES == "":
    NUM_EDGES = None
main(NUM_VERTICES, NUM_EDGES, CONNECTED)