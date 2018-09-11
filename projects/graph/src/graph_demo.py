#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph


def main():
    #create graph
    graph = Graph()

    #Add vertexes
    graph.add_vertex('v1')
    graph.add_vertex('v2')
    graph.add_vertex('v3')
    graph.add_vertex('v4')
    graph.add_vertex('v5')
    graph.add_vertex('v6')
    graph.add_vertex('v7')
    graph.add_vertex('v8')
    graph.add_vertex('v9')
    graph.add_vertex('v10')
    graph.add_vertex('v11')
    graph.add_vertex('v12')
    graph.add_vertex('v13')
    graph.add_vertex('v14')

    #add edges
    graph.add_edge('v1', 'v2')
    graph.add_edge('v2', 'v1')
    graph.add_edge('v2', 'v7')
    graph.add_edge('v3', 'v8')
    graph.add_edge('v5', 'v6')
    graph.add_edge('v5', 'v10')
    graph.add_edge('v6', 'v5')
    graph.add_edge('v6', 'v7')
    graph.add_edge('v7', 'v2')
    graph.add_edge('v7', 'v6')
    graph.add_edge('v8', 'v3')
    graph.add_edge('v8', 'v7')
    graph.add_edge('v8', 'v9')
    graph.add_edge('v8', 'v13')
    graph.add_edge('v9', 'v8')
    graph.add_edge('v9', 'v14')
    graph.add_edge('v10', 'v5')
    graph.add_edge('v12', 'v13')
    graph.add_edge('v13', 'v12')
    graph.add_edge('v13', 'v8')
    graph.add_edge('v13', 'v14')
    graph.add_edge('v14', 'v13')
    graph.add_edge('v14', 'v9')

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    # TODO - parse argv
    main()
