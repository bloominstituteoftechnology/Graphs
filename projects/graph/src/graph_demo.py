#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
from random import sample
from sys import argv
from bokeh.io import show, output_file
from draw import BokehGraph
from graph import Graph



def main(num_vertices=8, num_edges=8):
    graph = Graph()  
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(2, 5)
    graph.add_edge(2, 4)
    graph.add_edge(4, 9)
    graph.add_edge(3, 7)
    graph.add_edge(3, 6)

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.draw()

    
    

if __name__ == '__main__':
    # TODO - parse argv
    main()




