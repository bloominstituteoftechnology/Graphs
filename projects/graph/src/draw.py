"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import Graph
from random import choice, random


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__( self, graph, title="Graph", width=800, height=600, show_axis=False, show_grid=False, circle_size=30 ):
        if not graph.vertices:
            raise Exception("Graph should have vertices")
        self.graph = graph
        
        self.width = width 
        self.height = height
        self.pos = {}
        
        self.plot = figure(title="title", x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid

        self._setup_graph_renderer(circle_size)
    
    def _setup_graph_renderer(self, circle_size):
        graph_render = GraphRenderer()

        graph_render.node_render.data_sorce.add(list(self.graph.vertices.keys()), "index")
        graph_render.node_render.data_sorce.add(Spectral8, 'color')
        graph_render.node_render.glyph = Circle(size=circle_size, fill_color='color')
       
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)
    
    def color_generator(self):
        colors = []
        for _ in range(len(self.graph.vertices)):
            color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors
   
    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.append(vertex)
                    end_indices.append(destination)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def randomize(self):
        """
        Randomize Vertex Positions
        """
        for vertex in self.graph.vertices:
            self.position[vertex] = (1 + random() * (self.width - 2),
                                     1 + random() * (self.height - 2))

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)

    def main():
        graph = Graph()
        bg = BokehGraph(graph)

        graph.add_vertex('0')
        graph.add_vertex('1')
        graph.add_vertex('2')
        graph.add_vertex('3')

        graph.add_edge('0', '1')
        graph.add_edge('0', '3')
        graph.add_edge('1', '2')
        graph.add_edge('2', '3')
        graph.add_edge('3', '1')
        print(graph.vertices)
        bg.show()

