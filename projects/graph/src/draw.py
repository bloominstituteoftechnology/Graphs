"""
General drawing methods for graphs using Bokeh.
"""
from graph import Graph
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)

g = Graph()
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_edge('0', '1')
g.add_edge('0', '3')
g.add_edge('0', '3')
g.add_edge('4', '3')
print(g.vertices)

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.vertices = graph.vertices
        self.size = len(graph.vertices)

    def show(self):
        node_indices = list(self.vertices.keys())

        plot = figure(title="Graph Layout Render", x_range=(-1.1, 10.1), y_range=(-1.1, 10.1), tools="", toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(['red'] * self.size, 'color')
        graph.node_renderer.glyph = Circle(radius=0.25, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex in self.vertices:
            for edge_end in self.vertices[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge_end)

        ### start of layout code
        circ = [int(v) for v in g.vertices]
        x = [2 * (i // 3) for i in circ]
        y = [2 * (i % 3) for i in circ]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)

bg = BokehGraph(g)
bg.show()
