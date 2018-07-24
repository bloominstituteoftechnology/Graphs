"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph
import random


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        if not graph.vertices:
            raise Exception("Graph should contain vertices")
        self.graph = graph
        self.pos = {}

    def _get_edges(self):
        start = []
        end = []
        checked = set()
        for startpoint, endpoints in self.graph.vertices.items():
            for endpoint in endpoints:
                if (startpoint, endpoint) not in checked:
                    checked.add((startpoint, endpoint))
                    start.append(startpoint)
                    end.append(endpoint)
        return dict(start=start, end=end)

    def _get_random_colors(self):
        colors = []
        for vertex in self.graph.vertices:
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            colors.append(color)
        return colors

    def map_coords(self):
        for vertex in self.graph.vertices.keys():
            self.pos[vertex] = (random.uniform(0.5,9.5), random.uniform(0.5,9.5))
        
    def draw(self, title='Graph', width=10, height=10,
                show_axis=False, show_grid=False, circle_size=15):
        plot = figure(title=title, x_range=(0,width), y_range=(0,height))
        
        plot.axis.visible = show_axis
        plot.grid.visible = show_grid

        graph = GraphRenderer()
        graph.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        graph.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        graph.node_renderer.glyph = Circle(size=circle_size,
            fill_color='color')
        graph.edge_renderer.data_source.data = self._get_edges()

        self.map_coords()
        graph.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        plot.renderers.append(graph)

        output_file('./graph.html')
        show(plot)

def randomize_graph(size=10):
    graph = Graph()
    for i in range(size):
        graph.add_vertex(str(i))
    # make connections
    for vertex in graph.vertices.keys():
        vertices = list(graph.vertices.keys())
        vertices.remove(vertex)
        # 30% chance that a vertex will have connections
        if random.random() > 0.5:
            num_connections = random.randint(0, min(size//3, 3))
            if num_connections > 0:
                for i in range(num_connections):
                    end = random.choice(vertices)
                    vertices.remove(end)
                    graph.add_edge(vertex, end)
    bokeh = BokehGraph(graph)
    bokeh.draw()
    
if __name__ == '__main__':
    randomize_graph()