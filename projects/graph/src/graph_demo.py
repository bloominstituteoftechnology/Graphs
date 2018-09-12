#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import random

from sys import argv
from graph import Graph
from draw import BokehGraph

def main(num_vertices = 10, num_edges = 10, min_x_range = 0, max_x_range = 10, min_y_range = 0, max_y_range = 10):
    graph = Graph()

    for i in range(num_vertices):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        x = random.randint(min_x_range, max_x_range)
        y = random.randint(min_y_range, max_y_range)
        graph.add_vertex(str(i), x, y, color)
    
    for _ in range(num_edges):
        vertices = random.sample(graph.vertices.keys(), 2)
        graph.add_edge(vertices[0], vertices[1])

    print("BFS Result")
    print(graph.bfs("4"))

    bokeh_graph = BokehGraph(graph, "Random Graph", min_x_range, max_x_range, min_y_range, max_y_range)
    bokeh_graph.show()

if __name__ == '__main__':
    if len(argv) == 7:
        num_vertices = int(argv[1])
        num_edges = int(argv[2]) 
        min_x_range = int(argv[3])
        max_x_range = int(argv[4])
        min_y_range = int(argv[5]) 
        max_y_range = int(argv[6])
        main(num_vertices, num_edges, min_x_range, max_x_range, min_y_range, max_y_range)
    else:
        main() 
