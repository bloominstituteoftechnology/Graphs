#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

# from sys import argv
import sys
from draw import BokehGraph
from graph import Graph
from random import randint

number_vertices = int(sys.argv[1])
number_edges = int(sys.argv[2])

if number_vertices < 0 or number_edges < 0:
    raise ValueError("number must be greater than zero")
elif number_edges > number_vertices * (number_vertices-1)/2:
    raise ValueError("max number of edges exceeded")


x = 8

# list_vertices = [i for i in range(number_vertices)] or [i for i in range(x)]

graph = Graph()
g = [graph.add_vertex(x) for x in range(number_vertices + 1)]
# print("mylist is ", my_list)

unique_edges = set()
while(len(unique_edges) < number_edges):
    v1 = randint(0, number_vertices)
    v2 = randint(0, number_vertices)
    if (v2, v1) not in unique_edges:
        unique_edges.add((v1, v2))
        graph.add_directed_edge(v1, v2)


print('unique edges', len(unique_edges))
print('unique edges', len(set(unique_edges)))


boka = BokehGraph(graph)
boka.show()
