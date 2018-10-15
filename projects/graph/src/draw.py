"""
General drawing methods for graphs using Bokeh.
"""

import math
# import networkx as nx
from graph import Graph

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource, MultiLine
# from bokeh.models.graphs import from_networkx, NodesAndLinkedEdges, EdgesAndLinkedNodes

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    """
    Use Bokeh to generate and display HTML that draws the graph
    included Pipfile will install Bokeh and necessarily dependencies
    """
    def show(self):
        vertices_list = self.graph.vertices_list
        plot = figure(title = "Boken Graph", x_range = (-2, 2), y_range= (-2, 2),
                    tools = "", toolbar_location = None)
        x = [0, 1, 0, 1]
        y = [0, 0, 1, 1]
        # initiate vertice in square shape
        plot.circle(x, y, size = 15, color = "grey")
        # initiate edges
        for vertex in vertices_list:
            # if set is not empty
            if len(vertices_list[vertex]) != 0:
                to_vertices = list(vertices_list[vertex])
                for to_vertex in to_vertices:
                    # draw edge 
                    plot.line([x[int(vertex)], x[int(to_vertex)]],
                              [y[int(vertex)], y[int(to_vertex)]],
                              line_width = 3,
                              color = "grey")

        output_file("graph.html")
        show(plot)

graph = Graph()
# print(graph.show_graph())
graph = BokehGraph(graph)
graph.show()