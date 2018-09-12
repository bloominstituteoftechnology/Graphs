#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from draw import BokehGraph
from graph import Graph
from random import sample, randint

def randomGraph(vertices, edges):
    graph = Graph()

    for x in range(vertices):
        if vertices <= 10:
            random_pos = randint(1, 10)
        else:
            random_pos = randint(1, vertices)
        print(graph.vertices.keys())
        while random_pos in graph.vertices.keys():
            if vertices <= 10:
                random_pos = randint(1, 10)
            else:
                random_pos = randint(1, vertices)

        graph.add_vertex(random_pos)

    for y in range(edges):
        random_vertices = sample(graph.vertices.keys(),2)
        graph.add_edge(random_vertices[0], random_vertices[1])

    return graph

def regularGraph():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_vertex('8')
    graph.add_vertex('9')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    
    return graph

def main(**kwargs):
    style = kwargs["style"]
    verts = kwargs["verts"]
    edges = kwargs["edges"]

    if style == "random":
        graph = randomGraph(verts, edges)
    else:
        graph = regularGraph()

    bokeh = BokehGraph(graph)
    bokeh.draw()   

if __name__ == '__main__':
    style="regular"
    verts = 4
    edges = 5

    for arg in argv[1:]:
        args = arg.split("=")
        if len(args) == 2:
            if args[0] == "style":
                style = args[1].lower()
            elif args[0] == "verts":
                verts = int(args[1])
            elif args[0] == "edges":
                edges = int(args[1])
    main(style=style, verts=verts, edges=edges)

