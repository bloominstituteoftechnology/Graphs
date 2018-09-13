"""
General drawing methods for graphs using Bokeh.
"""
import math
import random
from functools import partial
from graph import Graph
from node import Node
from bokeh.io import show, output_file
from bokeh.plotting import figure

from bokeh.models import (GraphRenderer, Arrow, OpenHead, NormalHead, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, x_range = (-1.1, 1.1), y_range = (-1.1, 1.1)):
        self.graph = graph
        self.x_range = x_range
        self.y_range = y_range

    
    def show(self):
        N = len(self.graph.vertices)
        node_indices = list(range(N))

        plot = figure(title='Graph Layout Demonstration', x_range=self.x_range, y_range=self.y_range,
                    tools='', toolbar_location=None)

        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add([vertex.color for vertex in self.graph.vertices], 'color')
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

    def generate_random_nodes(self, node_quantity):
        print(*self.x_range)
        for i in range(node_quantity):
            # The arguments in create_with_random_props, ensure that the
            # nodes stay within the graph
            node = Node.create_with_random_props(self.x_range[1], self.y_range[1])
            node.assign_random_color()
            self.graph.add_vertex(node)


    def generate_one_connect_directional_edges(self):
        if len(self.graph.vertices) < 2:
            raise Exception('Please add 2 or more nodes for creating edges')
        
        directional_fn = self.graph.add_directional_edge
        
        for vertex in self.graph.vertices:

            directional_fn = partial(directional_fn, vertex)

            if len(directional_fn.args) == 2:
                directional_fn()
                directional_fn = partial(self.graph.add_directional_edge, vertex)
    



if __name__ == '__main__':
    # graph = Graph()
    # node0 = Node(1,1.5)
    # node1 = Node(.5,1)
    # node2 = Node(0.25, 0.5)
    # node3 = Node(.75,.5)
    # node4 = Node(1.5, 1)

    # graph.add_vertex(node0)
    # graph.add_vertex(node1)
    # graph.add_vertex(node2)
    # graph.add_vertex(node3)
    # graph.add_vertex(node4)

    # graph.add_edge(node0, node1)
    # graph.add_edge(node1, node2)
    # graph.add_edge(node1, node3)
    # graph.add_edge(node0, node4)
    # bokeh_graph = BokehGraph(graph)
    # print(bokeh_graph.bfs())
    # Directional bokeh_graph
    bokeh_graph = BokehGraph(Graph())
    bokeh_graph.generate_random_nodes(5)
    bokeh_graph.generate_one_connect_directional_edges()
    bokeh_graph.show()