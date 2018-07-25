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
                if (startpoint.label, endpoint.label) not in checked:
                    checked.add((startpoint.label, endpoint.label))
                    start.append(startpoint.label)
                    end.append(endpoint.label)
        return dict(start=start, end=end)

    def _get_colors(self):
        colors = []
        for vertex in self.graph.vertices.keys():
            color = vertex.color
            colors.append(color)
        return colors

    def map_coords(self):
        for vertex in self.graph.vertices.keys():
            self.pos[vertex.label] = (random.uniform(0.5,9.5), random.uniform(0.5,9.5))
    
    def _get_labels(self):
        labels = []
        for vertex in self.graph.vertices.keys():
            labels.append(vertex.label)
        return labels
        
    def draw(self, title='Graph', width=10, height=10,
                show_axis=False, show_grid=False, circle_size=15):
        plot = figure(title=title, x_range=(0,width), y_range=(0,height))
        
        plot.axis.visible = show_axis
        plot.grid.visible = show_grid

        graph = GraphRenderer()
        graph.node_renderer.data_source.add(
            self._get_labels(), 'index')
        graph.node_renderer.data_source.add(
            self._get_colors(), 'color')
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
    searched = set()
    for vertex in graph.vertices:
        if vertex not in searched:
            searched.update(graph.search(vertex))
    bokeh = BokehGraph(graph)
    bokeh.draw()
    
if __name__ == '__main__':
    randomize_graph()