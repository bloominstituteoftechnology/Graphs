#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from draw import BokehGraph

def main(num_vertices, num_edges):
    BokehGraph(num_vertices, num_edges) 

if __name__ == '__main__':
    print(argv, argv[1], argv[2])
    main(argv[1], argv[2])