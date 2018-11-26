"""
General drawing methods for graphs using Bokeh.
"""
import math 
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, Oval, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph #should be a object. instance of Graph

    def show(self):
        N = len(self.graph.vertices.keys()) #length of vertices
        node_indices = list(range(N))
        plot = figure(title="Graph of Nodes and Edges", x_range=(-1.1,1.1), y_range=(-1.1,1.1),
        tools='', toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')

        graph.edge_renderer.data_source.data = dict(
            start=[0]*N,
            end=node_indices
        )
        circ =[i*2*math.pi/len(self.graph.vertices.keys()) for i in node_indices]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]

        graph_layout = dict(zip(node_indices, zip(x,y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)
        output_file('graph.html')
        show(plot)


    
test = Graph()
vertex_one = test.add_vertex("0")
vertex_two = test.add_vertex("1")
vertex_three = test.add_vertex("2")
test.add_edge_two_way(vertex_one, vertex_two)
test.add_edge_two_way(vertex_two, vertex_three)
test_Bokeh = BokehGraph(test)

test_Bokeh.show()

