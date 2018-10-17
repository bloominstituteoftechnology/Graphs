#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from graph import Graph
from draw import BokehGraph
from sys import argv


####################################
# TODO::
# Build Demo classm
# ^^ takes:
# -- number of vertices
# -- number of edges (max = num of vertices)
#
# ^^ create Graph() isntance
# ^^ create vertices (
#     -> range 50,
#     -> call add_vertex
# )
#
# ^^ create edges (
#     -> pick vertex index at random,
#     -> create random integer,
#     -> call add_edge
# )
#
# ^^ create BokehGraph() instance
# ^^ pass Graph to BokehGraph
#     -> call draw() on instance
#############################################

class Network_Graph_Builder:
    def __init__(self, num_vertices, num_edges):
        self.num_vertices = num_vertices
        if(num_edges > num_vertices):
            print("Cannot have more edges than vertices")
        else:
            self.num_edges = num_edges





def main():




if __name__ == '__main__':
    # TODO - parse argv
    main()
