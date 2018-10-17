#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from graph import Graph
from draw import BokehGraph
from sys import argv


def create_default_graph():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('5')
    graph.add_vertex('2')
    graph.add_vertex('6')
    graph.add_vertex('1')
    graph.add_vertex('4')
    graph.add_vertex('7')
    graph.add_vertex('3')
    graph.add_vertex('99')

    graph.add_edge('5', '2')
    graph.add_edge('5', '6')
    graph.add_edge('2', '1')
    graph.add_edge('2', '4')
    graph.add_edge('4', '3')
    graph.add_edge('6', '7')

    bg = BokehGraph(graph)
    bg.draw()


def create_random_graph(num_nodes):

    graph = Graph()
    for i in range(num_nodes):
        graph.add_vertex(i)

    bg = BokehGraph(graph)
    bg.draw()


def main(style, num_nodes):
    if style == "default":
        create_default_graph()
    elif style == "random":
        create_random_graph(num_nodes)
    else:
        create_default_graph()


if __name__ == '__main__':
    style = "default"
    num_nodes = 5
    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "nodes":
                num_nodes = int(arg_split[1])
            else:
                print("I don't understand that command")

    main(style, num_nodes)
