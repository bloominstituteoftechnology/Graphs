#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph

def getGraph():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_edge('0', '1')
    graph.add_edge('0', '6')
    graph.add_edge('2', '3')
    graph.add_edge('3', '6')
    graph.add_edge('4', '5')
    graph.add_edge('5', '6')

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.draw()


getGraph()
