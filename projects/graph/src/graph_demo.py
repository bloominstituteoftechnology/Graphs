#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

def create_random_graph(num_nodes,num_edges):
    graph=Graph()
    possible_edges=[]
    for i in range(num_nodes):
        for j in range(i+1,num_nodes):
            possible_edges.append((i,j))
    random.shuffle(possible_edges)
    edges=possible_edges[:num_edges]
    if num_edges>len(possible_edges):
        print("Way too many edges program got lazy and stopped execution.")
        exit()
    for i in range(num_nodes):
        graph.add_vertex(i)
    for edge in edges:
        graph.add_edge(edge[0],edge[1])
    bg=BokehGraph(graph)
    bg.draw()

def main(num_nodes,num_edges):
    create_random_graph(num_nodes,num_edges)

if __name__ == '__main__':
    num_nodes=5
    num_edges=5
    for arg in argv[1:]:
        arg=arg.split('=')
        if len(arg)==2:
            if arg[0]=='nodes':
                num_nodes=int(arg[1])
            elif arg[0]=='edges':
                num_edges=int(arg[1])
            else:
                print('Command invalid.')
    main(num_nodes,num_edges)
