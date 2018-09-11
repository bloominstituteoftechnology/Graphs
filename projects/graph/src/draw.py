"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource, Square)
from bokeh.palettes import Spectral8
from graph import Graph


# N = len(graph.vertices)
# node_indices = list(graph.vertices)


# plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1), y_range=(-1.1,10.1),
#               tools='', toolbar_location=None)

# graph_renderer = GraphRenderer()

# graph_renderer.node_renderer.data_source.add(node_indices, 'index')
# graph_renderer.node_renderer.data_source.add(['red', 'blue', 'green', 'orange', 'purple', 'yellow'], 'color')
# graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

# start_indices = []
# end_indices = []

# for vertex in graph.vertices:
#     for edge_end in graph.vertices[vertex]:
#         start_indices.append(vertex)
#         end_indices.append(edge_end)
# print(start_indices)
# print(end_indices)


# graph_renderer.edge_renderer.data_source.data = dict(
#     start=start_indices,
#     end=end_indices)

# ### start of layout code
# grid = [int(v) for v in graph.vertices]
# x = [2 * (i // 3) for i in grid]
# y = [2 * (i % 3) for i in grid]
# # x = [i for i in grid]
# # y = [i ** 2 for i in grid]

# graph_layout = dict(zip(node_indices, zip(x, y)))
# graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# plot.renderers.append(graph_renderer)

# labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
# labels = LabelSet(x='x', y='y', text='names', level='glyph',
#              text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')


# plot.add_layout(labels)


# output_file('graph.html')
# show(plot)

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    
    def show(self):
        node_indices = list(self.graph.vertices.keys())
        x_value = [x for (x, y) in self.graph.vertices.items()]
        y_value = [list(y) for (x, y) in self.graph.vertices.items()]

        plot = figure(title='Graph Layout', x_range=(0, 9),
                y_range=(-4,4), tools='', toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(x_value, 'index')
        graph.node_renderer.data_source.add(Spectral8, 'color')
        graph.node_renderer.glyph = Circle(radius=0.1, fill_color='color')

        print("\n x value: ", x_value)
        print("\n y value: ", y_value)

        graph.edge_renderer.data_source.data = dict(
            start=x_value, end=y_value
        )

        circ = [int(i) for i in x_value]
        x = [i for i in circ]
        y = [math.sin(i) for i in circ]

        graph_layout = dict(zip(x_value, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

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
graph.add_vertex('10')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '7')
graph.add_edge('2', '5')
print(graph.vertices)

bg = BokehGraph(graph)
bg.show()