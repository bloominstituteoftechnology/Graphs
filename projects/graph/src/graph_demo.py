#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
import random
from graph import Graph
from draw import BokehGraph


def createDefaultGraph():
    graph = Graph() # instantiate graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('3', '4')

    bg = BokehGraph(graph)
    bg.draw()

def createRandomGraph(num_nodes, num_edges):
    graph = Graph()

    all_edges = []

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            all_edges.append((i, j))

    random.shuffle(all_edges)
    edges = all_edges[:num_edges]

    if num_edges > len(all_edges):
        print('Warning: max edges reached')
    
    # for edge in edges:
    #     print(edge)

    for i in range(num_nodes):
        graph.add_vertex(i)

    for edge in edges:
        # print(edge)
        graph.add_edge(edge[0], edge[1])

    # print(len(edges))
    print(graph.vertices)

    bg = BokehGraph(graph)
    bg.graph.dft_st(3)
    bg.draw()


def main(style, num_nodes, num_edges):
    if style == 'default':
        createDefaultGraph()
    elif style == 'random':
        createRandomGraph(num_nodes, num_edges)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    style = 'default'
    num_nodes = 5
    num_edges = 5

    for arg in argv[1:]:
        arg_split = arg.split('=')
        if len(arg_split) == 2:
            if arg_split[0] == 'style':
                style = arg_split[1].lower()
            elif arg_split[0] == 'nodes':
                num_nodes = int(arg_split[1])
            elif arg_split[0] == 'edges':
                num_edges = int(arg_split[1])
            else:
                print('command unclear \n')
    
    main(style, num_nodes, num_edges)



# def main(v=7, e=7):
#     graph = Graph()
#     for i in range(v):
#         graph.add_vertex(i)
#     for j in range(e):
#         random_vertex = int(random.random() * v)
#         random_edge = int(random.random() * e)
#         print(random_vertex, random_edge)
#         graph.add_edge(random_vertex, random_edge)
#     bg = BokehGraph(graph)
#     bg.draw()


# if __name__ == '__main__':
#     if len(argv) == 3:
#         v = argv[1]
#         e = argv[2]
#         main(int(v), int(e))
#     else:
#         main()
