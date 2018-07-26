#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from draw import RandomGraph


def main():
    main_graph = RandomGraph()
    main_graph.show()


if __name__ == '__main__':
    if len(argv) >= 3 and len(argv) < 5:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        CHANCE = int(argv[3])
        main(NUM_VERTICES, NUM_EDGES)
    else:
        main()
