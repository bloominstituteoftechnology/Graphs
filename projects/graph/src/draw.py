"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, Oval, 
                        ColumnDataSource)
from bokeh.palettes import Spectral8

from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    def plot(self):
        N = len(self.graph.vertices)

        # Get ref to all node/vertex indexes from the keys of vertices
        node_indices = list(self.graph.vertices.keys())
        
        # Get ref to all lists of each connected node
        connected_nodes_lists = [list(v) for (k,v) in self.graph.vertices.items()]

        # Create a plot / figure
        plot = figure(title='Graph Layout Demonstration', x_range=(-1,5), y_range=(-1,5),
                    tools='', toolbar_location=None)

        # Add Data (Node/Edge) Sources
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Circle(radius=0.2, fill_color='color')
        graph.edge_renderer.data_source.data = dict(
            start=node_indices,
            end=connected_nodes_lists)

        # ### start of layout code
        # Circular 
        # circ = [i*2*math.pi/8 for i in node_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]

        grid = [int(v) for v in self.graph.vertices]
        x = [(i // 3) for i in grid]
        y = [(i % 3) for i in grid]
        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        # Render the plot
        plot.renderers.append(graph)
        output_file('graph.html')
        show(plot)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(f"Graph vertices: {graph.vertices}")

bg = BokehGraph(graph)
bg.plot()
