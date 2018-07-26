"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph
import random
import math


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        if not graph.vertices:
            raise Exception("Graph should contain vertices")
        self.graph = graph
        self.pos = {}

    def _setup_labels(self):
        label_data = {'x': [], 'y': [], 'names': []}
        for vertex, position in self.pos.items():
            label_data['x'].append(position[0])
            label_data['y'].append(position[1])
            label_data['names'].append(vertex)
        label_source = ColumnDataSource(label_data)
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                            text_align='center', text_baseline='middle',
                            source=label_source, render_mode='canvas')
        return labels

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

    def _map_coords(self, width, height):
        cells = math.ceil(len(self.graph.vertices.keys())**(1/2))
        cube = (width-1)/cells
        x_grid = 0.5
        y_grid = 0.5
        for vertex in self.graph.vertices.keys():
            self.pos[vertex.label] = (random.uniform(x_grid,x_grid+cube), 
                                    random.uniform(y_grid,y_grid+cube))
            if x_grid + cube >= (width - cube):
                x_grid = 0.5
                y_grid += cube
            else:
                x_grid += cube
    
    def _get_indices(self):
        indices = []
        for vertex in self.graph.vertices.keys():
            indices.append(vertex.label)
        return indices
        
    def draw(self, title='Graph', width=10, height=10,
                show_axis=False, show_grid=False, circle_size=25):
        plot = figure(title=title, x_range=(0,width), y_range=(0,height))
        
        plot.axis.visible = show_axis
        plot.grid.visible = show_grid

        graph = GraphRenderer()
        graph.node_renderer.data_source.add(
            self._get_indices(), 'index')
        graph.node_renderer.data_source.add(
            self._get_colors(), 'color')
        graph.node_renderer.glyph = Circle(size=circle_size,
            fill_color='color')
        graph.edge_renderer.data_source.data = self._get_edges()

        self._map_coords(width, height)
        graph.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        plot.renderers.append(graph)

        labels = self._setup_labels()
        plot.add_layout(labels)

        output_file('./graph.html')
        show(plot)

def randomize_graph(vertices=10, connections=5):
    graph = Graph()
    for i in range(vertices):
        graph.add_vertex(str(i))
    for i in range(connections):
        start, end = random.sample(list(graph.vertices), 2)
        graph.add_edge(start, end)
    colors = ['#FF395B', '#FC928F', '#F9C6A3', '#C0BF9F',
                '#79A792', '#1A8CC1', '#FECE6B', '#F69D61']
    color_index = 0
    searched = set()
    for vertex in graph.vertices:
        if vertex not in searched:
            if color_index > len(colors):
                color_index = 0
            color = colors[-color_index]
            searched.update(graph.search(vertex, color))
            color_index += 1
    bokeh = BokehGraph(graph)
    bokeh.draw()
    
if __name__ == '__main__':
    randomize_graph(16, 6)