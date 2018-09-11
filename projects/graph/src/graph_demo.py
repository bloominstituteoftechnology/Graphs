#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

# from sys import argv
import sys
from draw import BokehGraph
from graph import Graph
from random import randint

input_cmd = list(sys.argv)

print(len(input_cmd))
print((input_cmd))

if len(input_cmd) > 1:
    number_vertices = int(sys.argv[1])
else:
    number_vertices = randint(4, 8)

if len(input_cmd) > 2:
    number_edges = int(sys.argv[2])
else:
    number_edges = randint(2, 4)


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
    if v1 == v2:
        continue
    if (v2, v1) not in unique_edges:
        unique_edges.add((v1, v2))
        graph.add_directed_edge(v1, v2)

print('unique edges', len(unique_edges))
print('unique edges', len(set(unique_edges)))


boka = BokehGraph(graph)
boka.show()
