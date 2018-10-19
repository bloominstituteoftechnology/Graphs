#!/usr/bin/python
from draw import BokehGraph
from graph import Graph
from sys import argv
import math, random


def main(argv):
    if argv and argv[0]:
        num_vert = int(argv[0])
    else:
        num_vert = math.floor(random.random() * 10 + 3)
    if argv and argv[1]:
        num_edges = int(argv[1])
    else:
        num_edges = math.floor(random.random() * (num_vert*(num_vert-1)))
    graph = Graph()
    id = 0
    while len(graph.vertices) < num_vert:
        graph.add_vertex(id)
        id += 1
    cnt = 0
    while cnt < num_edges:
        v1 = math.floor(random.random()*num_vert)
        v2 = math.floor(random.random()*num_vert)
        if v1 is not v2:
            graph.add_edge(v1,v2)
            cnt += 1

    print(graph.dfs(graph.vertices[0],4))

    bg = BokehGraph(graph)
    bg.draw()

if __name__ == '__main__':
    if len(argv) > 1:
        main(argv[1:])
    else:
        main(None)
