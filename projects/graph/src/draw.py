"""
General drawing methods for graphs using Bokeh.
"""
import math
import random

from graph import Graph
from node import Node
from bokeh.io import show, output_file
from bokeh.plotting import figure

from bokeh.models import (GraphRenderer, Arrow, OpenHead, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    
    def show(self):
        N = len(self.graph.vertices)
        node_indices = list(range(N))

        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,1.1), y_range=(-1.1,1.1),
                    tools='', toolbar_location=None)

        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        r = lambda: random.randint(50,255)
        graph.node_renderer.data_source.add(['#%02X%02X%02X' % (r(),r(),r()) for i in range(N)], 'color')
        graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color')


        # Draws the edges to neighboring nodes
        start_indices = []
        end_indices = []
        make_arrow = []
        for vertex in self.graph.vertices:
            for edge_end in self.graph.vertices[vertex]:
                # Bi-directional
                if vertex in self.graph.vertices[edge_end]:
                    start_indices.append(vertex.id)
                    end_indices.append(edge_end.id)
                else:
                    # Directional Edges
                    plot.add_layout(Arrow(end=OpenHead(line_color="firebrick", line_width=4),x_start=vertex.x, y_start=vertex.y, x_end=edge_end.x, y_end=edge_end.y))
        
        # Renders the Bi-directional edges
        graph.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)

        # Plots the node locations
        x = [vertex.x for vertex in self.graph.vertices]
        y = [vertex.y for vertex in self.graph.vertices]
        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        identities = [vertex.id for vertex in self.graph.vertices]
        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=identities))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas', text_color='black')
        plot.renderers.append(graph)

        plot.add_layout(labels)

        output_file('graph.html')
        show(plot)


if __name__ == '__main__':
    # graph = Graph()

    # Square with a dot in the middle
    graph = Graph()
    # Middle Node
    node0 = Node(0,0)
    # Bottom Left
    node1 = Node(-0.5,-0.5)
    # Top Left
    node2 = Node(-0.5, 0.5)
    # Top Right
    node3 = Node(0.5,0.5)
    # Bottom Right
    node4 = Node(0.5,-0.5)
    graph.add_vertex(node0)
    graph.add_vertex(node1)
    graph.add_vertex(node2)
    graph.add_vertex(node3)
    graph.add_vertex(node4)
    graph.add_edge(node1, node2)
    graph.add_edge(node2, node3)
    graph.add_directional_edge(node3, node4)
    graph.add_directional_edge(node4, node1)
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()