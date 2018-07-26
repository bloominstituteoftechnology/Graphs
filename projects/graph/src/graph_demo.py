#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from random import randint
from sys import argv
from draw import BokehGraph
from graph import Graph


def main(vertices, edges, show_components, title, file_name):
    """
    Build a random graph and display in browser
    """
    graph = Graph()
    edges_added = []

    for i in range(vertices):
        graph.add_vertex('V{}'.format(i))

    while len(edges_added) < edges:
        start = 'V{}'.format(randint(0, vertices-1))
        end = 'V{}'.format(randint(0, vertices-1))
        if start != end and end not in graph.vertices[start]:
            graph.add_edge(start, end)
            edges_added.append((start, end))

    if show_components:
        graph.find_connected_components()

    bokeh_graph = BokehGraph(graph, show_components, title, file_name)
    bokeh_graph.show()


if __name__ == '__main__':
    # TODO: limit number of vertices and edges
    # TODO: elaborate on required and optional fields in console message
    if len(argv) > 2:
        NUMBER_VERTICES = int(argv[1])
        NUMBER_EDGES = int(argv[2])
        SHOW_COMPONENTS = bool(int(argv[3])) if len(argv) > 3 else True
        GRAPH_TITLE = str(argv[4]) if len(argv) > 4 else 'Graph'
        OUTPUT_FILE_NAME = str(argv[5]) if len(argv) > 5 else './graph.html'
        main(NUMBER_VERTICES, NUMBER_EDGES, SHOW_COMPONENTS, GRAPH_TITLE,
             OUTPUT_FILE_NAME)
    else:
        print('\nError: Graph demo requires two arguments: number of'
              'vertices as an int and the number of edges as an int:\n\n\t'
              'graph_demo.py NUMBER_VERTICES NUMBER_EDGES'
              '[SHOW COMPONENTS] [GRAPH TITLE] [OUTPUT FILE NAME]\n')
