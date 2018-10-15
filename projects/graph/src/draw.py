"""
General drawing methods for graphs using Bokeh.
"""
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet

from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    def show (self, graph, node_list):
        N = len(node_list)
        node_indices = list(node_list)
        print(node_indices)


        plot = figure(title="Graph Layout Demonstration", x_range=(-1.1, 10.1), y_range=(-1.1, 10.1),
                    tools="", toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(['white'] * N, 'color')
        graph.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

        start_indices = [] 
        end_indices = []

        for vertex in node_list:
            for edge_end in node_list[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge_end)

        graph.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices
        )

        circ = [int(v) for v in node_list]
        x = [2 * (i // 3) for i in circ]
        y = [2 * (i % 3) for i in circ]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(
            graph_layout=graph_layout)

        plot.renderers.append(graph)
        
        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=circ))
       
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                    text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')
        plot.add_layout(labels)
        output_file('graph.html')
        show(plot)


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_vertex('8')
graph.add_vertex('9')
graph.add_edge('0', '1')
graph.add_edge('1', '3')
graph.add_edge('2', '4')
graph.add_edge('3', '4')
graph.add_edge('4', '5')
graph.add_edge('5', '6')
graph.add_edge('6', '7')

print(graph.vertices)

newGraph = BokehGraph(graph)
newGraph.show(graph, graph.vertices)