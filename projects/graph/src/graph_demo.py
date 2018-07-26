#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from draw import RandomGraph


def main(NUM_VERTICES=None, NUM_EDGES=None):
    main_graph = RandomGraph(NUM_VERTICES, NUM_EDGES)
    main_graph.show()


if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()
