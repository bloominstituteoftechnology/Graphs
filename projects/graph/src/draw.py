"""
General drawing methods for graphs using Bokeh.
"""
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle,ColumnDataSource,LabelSet)
from graph import Graph


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self,graph):
        self.graph=graph
    def draw(self):
        graph=self.graph
        N = len(graph.vertices)
        vertex_indices = list(graph.vertices.keys())

        plot = figure(title='Graph Layout Demonstration', x_range=(-7,7), y_range=(-7,7),tools='', toolbar_location=None)
        graph_renderer = GraphRenderer()
        graph_renderer.node_renderer.data_source.add(vertex_indices, 'index')
        graph_renderer.node_renderer.data_source.add(vertex_indices, 'index')
        color = []
        for vertex in self.graph.vertices:
            color.append(self.graph.vertices[vertex].color)
        graph_renderer.node_renderer.data_source.add(color, 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')
        edge_start=[]
        edge_end=[]
        for vertex_id in vertex_indices:
            for v in graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(v)
        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)
        
        x=[]
        y=[]
        for vertex_id in vertex_indices:
            vertex=graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(vertex_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)
        label_source=ColumnDataSource(data=dict(x=x,y=y,names=[vertex_id for vertex_id in graph.vertices]))
        labels=LabelSet(x='x',y='y',text='names',level='glyph', text_align='center',text_baseline='middle', source=label_source,render_mode='canvas')
        plot.add_layout(labels)
        output_file('graph.html')
        show(plot)
