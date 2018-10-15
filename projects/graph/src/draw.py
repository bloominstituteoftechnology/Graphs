"""
General drawing methods for graphs using Bokeh.
"""
from bokeh.io import output_notebook, output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, GraphRenderer, StaticLayoutProvider, LabelSet, Circle, MultiLine
from bokeh.palettes import Category20c
from bokeh.models.graphs import NodesAndLinkedEdges
from graph import Graph
import math


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph=graph
    
    def graph_render(self):
        nodes = list(self.graph.vertices.keys())
        N=len(nodes)

        #Create plot
        plot = figure(title = 'Graph', x_range = (-1.5, 1.5) , y_range = (-1.5, 1.5), tools = "", toolbar_location = None)

        graph = GraphRenderer()
        
        graph.node_renderer.glyph = Circle(radius = 0.1, fill_color = "fill_color")  
        graph.node_renderer.data_source.data = dict(
            index = nodes,
            fill_color = ['blue']*N
            )

            
        graph.edge_renderer.data_source.data = dict(start=[0]*N,end=nodes)

        ##start of layout code
        circ = [i*2*math.pi/len(nodes) for i in range(len(nodes))]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]


        graph_layout = dict(zip(nodes, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')

        show(plot)

