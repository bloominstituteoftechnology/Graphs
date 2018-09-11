"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import demo_g

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph=None, title='Simple Graph Title', w=10, h=10):
        self.graph = graph
        self.plot = figure(
            title=title, 
            x_range=(-1, w), 
            y_range=(-1, h), 
            tools='', 
            toolbar_location=None
        )

    def setup_graph(self, circle_radius=0.5):
        node_indices = list(self.graph.vertices)
        
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Spectral8[:4], 'color')
        graph.node_renderer.glyph = Circle(radius=circle_radius, fill_color='color')

        start_indices = [vertex for vertex, edges in self.graph.vertices.items() for edge in edges]
        end_indices = [edge for vertex, edges in self.graph.vertices.items() for edge in edges]

        graph.edge_renderer.data_source.data = dict(start = start_indices, end = end_indices)
        
        grid = [int(vertex) for vertex in self.graph.vertices.keys()]
        x = [2 * (vertex // 3) for vertex in grid]
        y = [2 * (vertex % 3) for vertex in grid]

        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        self.plot.renderers.append(graph)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
        labels = LabelSet(
            x='x', 
            y='y', 
            text='names', 
            level='glyph',
            text_align='center',
            text_baseline='middle',
            source=labelSource,
            render_mode='canvas'
        )

        self.plot.add_layout(labels)

    def show_plot(self, output_path = './graph.html'):
        output_file(output_path)
        show(self.plot)

demo_b = BokehGraph(demo_g)
demo_b.setup_graph()
demo_b.show_plot()
