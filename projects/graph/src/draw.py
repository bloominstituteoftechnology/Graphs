"""
General drawing methods for graphs using Bokeh.
"""

from math import ceil, floor, sqrt
from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=100, height=100,
                 show_axis=False, show_grid=False, circle_size=35,
                 draw_components=False):
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
        self.graph = graph
        self.width = width
        self.height = height
        self.pos = {}  # dict to map vertices to x, y positions
        # Set up plot, the canvas/space to draw on
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size, draw_components)
        self._setup_labels()


    def _setup_graph_renderer(self, circle_size, draw_components):
        # The renderer will have the actual logic for drawing
        graph_renderer = GraphRenderer()
        # Saving vertices in an arbitrary but persistent order
        self.vertex_list = list(self.graph.vertices.keys())

        # Add the vertex data as instructions for drawing nodes
        graph_renderer.node_renderer.data_source.add(
            [vertex.label for vertex in self.vertex_list], 'index')
        colors = (self._get_connected_component_colors() if draw_components
                  else self._get_random_colors())
        graph_renderer.node_renderer.data_source.add(colors, 'color')
        # And circles
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')

        # Add the edge [start, end] indices as instructions for drawing edges
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()  # Randomize vertex coordinates, and set as layout
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        # Attach the prepared renderer to the plot so it can be shown
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self, num_colors=None):
        colors = []
        num_colors = num_colors or len(self.graph.vertices)
        for _ in range(num_colors):
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
                    start_indices.append(vertex.label)
                    end_indices.append(destination.label)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def _setup_labels(self):
        label_data = {'x': [], 'y': [], 'names': []}
        for vertex_label, (x_pos, y_pos) in self.pos.items():
            label_data['x'].append(x_pos)
            label_data['y'].append(y_pos)
            label_data['names'].append(vertex_label)
        label_source = ColumnDataSource(label_data)
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                          text_align='center', text_baseline='middle',
                          source=label_source, render_mode='canvas')
        self.plot.add_layout(labels)

    def show(self, output_path='./graph.html'):
        """Render the graph to a file on disk and open with default browser."""
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions, trying to minimize collisions."""
        # Split space into a grid of ~sqrt(num_of_vertices)^2
        rows = floor(sqrt(len(self.vertex_list)))
        cols = ceil(sqrt(len(self.vertex_list)))
        grid_height = self.height / rows
        grid_width = self.width / cols
        for i, vertex in enumerate(self.vertex_list):
            # Randomly place each vertex in a different grid cell
            # TODO: improve, this spreads things out some but still collides
            col = (i % rows) + 1
            row = (i + 1) // cols
            x_pos = 10 + (col + random()) * grid_width - 15
            y_pos = 10 + (row + random()) * grid_height - 15
            self.pos[vertex.label] = (x_pos, y_pos)

    def _get_connected_component_colors(self):
        """Return same-colors for vertices in connected components."""
        self.graph.find_components()
        component_colors = self._get_random_colors(self.graph.components)
        vertex_colors = []
        for vertex in self.vertex_list:
            vertex_colors.append(component_colors[vertex.component])
        return vertex_colors





# import math

# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet
# from bokeh.palettes import Spectral8
# from graph import Graph
# from random import sample

# class BokehGraph:
#     def __init__(self, graph, draw_components=True):
#         self.graph = graph
#     def draw(self):
#         myGraph = self.graph
#         N = len(myGraph.vertices)
#         node_indices = list(myGraph.vertices.keys())

#         plot = figure(title="Graph Layout Demonstration", x_range=(-7, 7), y_range=(-7, 7),
#                     tools="", toolbar_location=None)

#         graph = GraphRenderer()

#         connected = myGraph.connected_components()
#         node_indices = list(connected)
#         print(node_indices)
#         print("BFT", myGraph.BFT(myGraph.vertices.[0].id))
#         graph.node_renderer.data_source.add(node_indices, 'index')
#         hex_keys = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
#         random_color = "_".join(sample(hex_keys, 6))
#         print(random_color)
#         node_colors = []

#         for v in connected:
#             # print(myGraph.vertices[v].color)
         
#                  node_colors.append(f"#{random_color}")
#         graph.node_renderer.data_source.add(node_colors, 'color')
#         graph.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

#         edge_start = []
#         edge_end = []

#         for vertex_id in range[N]:
#             for v in myGraph.vertices[vertex_id].edges:
#                 edge_start.append(vertex_id)
#                 edge_end.append(v)

#         graph.edge_renderer.data_source.data = dict(
#             start=edge_start,
#             end=edge_end)
        

#         ### start of layout code
#         # circ = [i*2*math.pi/8 for i in node_indices]
#         # x = [math.cos(i) for i in circ]
#         # y = [math.sin(i) for i in circ]
#         x = []
#         y = []
#         for vertex_id in node_indices:
#             vertex = myGraph.vertices[vertex_id]
#             x.append(vertex.x)
#             y.append(vertex.y)
#         graph_layout = dict(zip(range(N), zip(x, y)))
#         graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

#         ### Draw quadratic bezier paths
#         # def bezier(start, end, control, steps):
#         #     return [(1-s)**2*start + 2*(1-s)*s*control + s**2*end for s in steps]

#         # xs, ys = [], []
#         # sx, sy = graph_layout[0]
#         # steps = [i/100. for i in range(100)]
#         # for node_index in node_indices:
#         #     ex, ey = graph_layout[node_index]
#         #     xs.append(bezier(sx, ex, 0, steps))
#         #     ys.append(bezier(sy, ey, 0, steps))
#         # graph.edge_renderer.data_source.data['xs'] = xs
#         # graph.edge_renderer.data_source.data['ys'] = ys
#         plot.renderers.append(graph)

#         labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[vertex_id for vertex_id in myGraph.vertices]))
#         labels = LabelSet(x='x', y='y', text='names', level='glyph',
#                 text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

#         plot.add_layout(labels)

#         output_file("graph.html")
#         show(plot)


# graph = Graph()
# graph.add_vertex(0)
# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)

# graph.add_edge(0, 1)
# graph.add_edge(0, 3)

# bokehGraph = BokehGraph(graph)
# bokehGraph.draw()









