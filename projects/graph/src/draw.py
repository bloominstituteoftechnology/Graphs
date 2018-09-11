"""
General drawing methods for graphs using Bokeh.
"""
import math
from graph import Graph
from node import Node
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
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
        graph.node_renderer.data_source.add(['pink'] * N, 'color')
        graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color')

      
        # Draws the edges to neighboring nodes
        start_indices = []
        end_indices = []
        for vertex in self.graph.vertices:
            for edge_end in self.graph.vertices[vertex]:
                start_indices.append(vertex.id)
                end_indices.append(edge_end.id)
        graph.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)
        
        # Plots the node locations
        x = [vertex.x for vertex in self.graph.vertices]
        y = [vertex.y for vertex in self.graph.vertices]
        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)



        output_file('graph.html')
        show(plot)


if __name__ == '__main__':
    graph = Graph()
    # Middle Node
    node0 = Node(0,0, .2)
    # Bottom Left
    node1 = Node(-0.5,-0.5, .2)
    # Top Left
    node2 = Node(-0.5, 0.5, .2)
    # Top Right
    node3 = Node(0.5,0.5, .2)
    # Bottom Right
    node4 = Node(0.5,-0.5, .2)
    graph.add_vertex(node0)
    graph.add_vertex(node1)
    graph.add_vertex(node2)
    graph.add_vertex(node3)
    graph.add_vertex(node4)
    # Middle to Top Right
    graph.add_edge(node0, node1)
    # Middle to Bottom Right
    graph.add_edge(node0, node2)
    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()