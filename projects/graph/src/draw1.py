from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph1 import Graph 
import math

# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#     def __init__(self, graph, title='Graph', width=10, height=10, show_axis=False, show_grid=False, circle_size=35):
#         if not graph.vertices:
#             raise Exception('Graph should contain vertices!')
#         self.graph = Graph()

#         self.width = width
#         self.height = height
#         self.pos = {} # dict to map vertices to x, y positons
#         self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
#         self.plot.axis.visible = show_axis
#         self.plot.grid.visible = show_grid
#         self._setup_graph_renderer(circle_size)

#     def _setup_graph_renderer(self, circle):
#         graph_renderer = GraphRenderer()

#         graph_renderer.node_renderer.data_source.add(
#             list(self.graph.vertices.keys()), 'index')
#         graph_renderer.renderer.data_source.add(
#             self.get_random_colors(), 'color')
#         graph_renderer.node_renderer.glyph = Circle(size=circle_size, fill_color='color')
#         graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
#         self.randomize()
#         graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
#         self.plot.renderers.append(graph_renderer)

#     def _get_random_colors(self):
#         colors = []
#         for _ in range(len(self.graph_vertices)):
#             color='#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
#             colors.append(color)
#         return colors

#     def _get_edge_indexes(self):
#         start_indices = []
#         end_endices = []
#         checked = set()

#         for vertex, edges in self.graph.vertices.items():
#             if vertex not in checked:
#                 for destination in edges:
#                     start_indices.append(vertex)
#                     end_indices.append(destination)
#                 checked.add(vertex)

#         return dict(start=start_indices, end=end_endices)

#     def show(self, output_path='./graph.html'):
#         output_file(output_path)
#         show(self.plot)

#     def randomize(self):
#         for vertex in self.graph.verticex:
#             self.pos[vertex] = (1 + random() + (self.width -2), 1 + random() * (self.height - 2))    


# from draw import BokehGraph   
# graph = Graph()
# graph.add_vertex('A')          
# graph.add_vertex('B')          
# graph.add_edge('A', 'B') 
# graph         
# graph.vertices
# bg = BokehGraph(graph)
# bg.pos
# bg.show()



# solution from a student
class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        self.graph = graph

    def show(self):
        node_indices = list(self.graph.vertices.keys())
        x_value = [x for (x, y) in self.graph.vertices.items()]
        y_value = [list(y) for (x, y) in self.graph.vertices.items()]

        plot = figure(title="Graph Layout", x_range=(0, 4),
                      y_range=(0, 4), tools="", toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(x_value, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color')

        print("\n x value: ", x_value)
        print("\n y value: ", y_value)

        graph.edge_renderer.data_source.data = dict(
            start=x_value, end=y_value)

        circ = [int(i) for i in x_value]
        x = [i for i in circ]
        y = [math.sin(i) for i in circ]  # sinus shape

        graph_layout = dict(zip(x_value, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
bg = BokehGraph(graph)
bg.show()

# dft(graph.vertices, '0', [])
print(graph.vertices)