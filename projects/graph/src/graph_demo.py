#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

# exploration with random functions
random.seed(123)
print(random.random())
#help(random.shuffle)
x = [2,4,6,8,10]
random.shuffle(x)
print(x)

# make a graph with vertices and edges for demonstration purposes
def createTestGraph():
    graph = Graph() # instantiate the graph using the Graph class
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('1', '2')
    graph.add_edge('1', '4')

    # bkg = BokehGraph(graph)
    # bkg.display()

# create a random graph

def createRandomGraph(vertices_count, edges_count):
    


def main():
    pass  # TODO


if __name__ == '__main__':
    # TODO - parse argv
    main()
