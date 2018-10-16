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
        N = len(vertices_list)
        node_indices = list(range(N))

        plot = figure (title = 'Graph showing vertices and edges', 
                       x_range = (-2, 2), 
                       y_range = (-2, 2),
                       tools = '',
                       toolbar_location = None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.glyph = Circle(size = 8, fill_color = "grey")

        # initiate edges
        from_edges = []
        to_edges = []
        
        for vertex in vertices_list:
            # set contains element
            if len(vertices_list[vertex]) != 0:
                to_vertices = vertices_list[vertex]
                for to_vertex in to_vertices:
                    from_edges.append(vertex)
                    to_edges.append(to_vertex)

        graph.edge_renderer.data_source.data = dict(start = from_edges, end = to_edges)

        ### start of layout code
        circ = [ i*2*math.pi/8 for i in node_indices ]
        x = [ math.cos(i) for i in circ ]
        y = [ math.sin(i) for i in circ ]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout = graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)

graph = Graph()
graph = BokehGraph(graph)
graph.show()