#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from graph import Graph
from draw import BokehGraph
from sys import argv
import random


#############################################
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
    def __init__(self, num_v, num_e):
        self.num_v = num_v
        if(num_e > num_v):
            print("Cannot have more edges than vertices")
        else:
            self.num_e = num_e
        self.grf = Graph()
        self.verts = self.grf.get_vertices()
        self.bok = BokehGraph()

    def create_vertices(self):
        for v in range(len(self.num_v)):
            self.grf.add_vertex(v)

    def create_edges(self):
        for ez in range(self.num_e):
            self.grf.add_edge(self.rndm_int(self.num_v),self.rndm_int(self.num_v))

    def get_rndm_vertex(self):
        rndm_int =  random.randint(self.num_v)
        verts = self.grh.get_vertices()
        return verts[rndm_int]

    def rndm_int(self, qty):
        return random.randint(qty)

    def init_graph(self):
        self.create_vertices()
        self.create_edges()






# def main():
#
#
#
#
# if __name__ == '__main__':
#     # TODO - parse argv
#     main()


ntx = Network_Graph_Builder(20,10)
ntx.init_graph()