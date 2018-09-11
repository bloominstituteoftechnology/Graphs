#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph


def main(arr, e_arr):
    g = Graph()
    g.add_vertex(arr)
    g.add_edges(e_arr)
    
    bg = BokehGraph(g)
    bg.show()

vertices = ['1', '3', '7', '11', '19', '27']
edges = [('1', '19'), ('1', '3'), ('3', '27'), ('7', '11'), ('11', '27')]
main(vertices, edges)

#if __name__ == '__main__':
    # TODO - parse argv
    #main(vertices, edges)

