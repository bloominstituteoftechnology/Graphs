import math
import random

# !/usr/bin/python
from graph import Graph
from draw import BokehGraph


"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv



def main():

    graph = Graph()
    graph.add_vertex(0)
    # graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    print(graph.vertices,'graph vertecies')
    graph.add_edge(5, 4)
    graph.add_edge(0, 5)
    graph.add_edge(4, 3)
    graph.add_edge(3, 2)
    print(graph.vertices,'graph vertecies')
    BokehGraph(graph).show()

    #random
    rando_graph = Graph()
    verts = math.floor(random.random() * 10) + 2
    # print(verts, 'verts')
    for v1 in range(0, verts):
        rando_graph.add_vertex(v1)
        # print(v2s, 'v2s')
    keys = list(rando_graph.vertices.keys())
    for v in keys:
        rando_edges = math.floor(random.randrange(0, len(keys)))
        # print(rando_edges, "rando_edges")
        for v2 in range(0, rando_edges):
            if v2 != v: #v1 if want to loop on itself
                rando_graph.add_edge(v, v2)  

    BokehGraph(rando_graph).show()
    # rando_graph.dfs(9)
    graph.dfs(9)
    

if __name__ == '__main__':
    # TODO - parse argv
    main()
    
