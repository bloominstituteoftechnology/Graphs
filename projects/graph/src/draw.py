"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)
from bokeh.plotting import figure
from bokeh.palettes import Spectral8
from random import (choice, randint)

# custom class
from graph import Graph

# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#     def __init__(self, x_range, y_range):
#         self.x_range = x_range
#         self.y_range = y_range
#         self.plot = figure(x_range=self.x_range, y_range=self.y_range)

#     def render_graph(self):
#         graph_renderer = GraphRenderer()
#         start = []
#         end = []
#         pos = {}
#         colors = []

# create new instance of `Graph` custom class
graph = Graph()
graph.add_random_vertices(20)
graph.add_random_edges()

print(graph.graph)

plot = figure(x_range=(0, 10), y_range=(0, 10)) # create the graph's canvas
# remove X and Y grid lines
plot.xgrid.grid_line_color = None
plot.ygrid.grid_line_color = None

graph_renderer = GraphRenderer()

start      = []
end        = []
color      = []
position   = {}

for vert in graph.graph:
    position[ int(vert) ] = [ randint(1, len(graph.graph)), randint(1, len(graph.graph)) ]
    random_color     = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])

    color.append(random_color)

    for edge in graph.graph[ vert ]:
        start.append(int(vert))
        end.append(int(edge))
        
# create labels for each vertice
source = ColumnDataSource(data={
        'x': [ position[ pos ][0] for pos in position ], # retrieve the X axis from each vertice
        'y': [ position[ pos ][1] for pos in position ], # retrieve the Y axis from each vertice
        'names': [ vert for vert in graph.graph ] # grab the KEY of each vertice and use it as the label
    }
)

# create a label set
labels = LabelSet(x='x', y='y', text='names', level='glyph', x_offset=5, y_offset=5, source=source, render_mode='canvas')

# add data to `data_source`
graph_renderer.node_renderer.data_source.add([ key for key in graph.graph ], 'index')
graph_renderer.node_renderer.data_source.add(color, 'color')

# render circles and give them a color from the `color` list
# these colors were added into `data_source` from the `graph_renderer.node_renderer.data_source.add(color, 'color')`
# the first parameter refers to the list `color` and the second is a string to reference in our `Circle` class below that
graph_renderer.node_renderer.glyph = Circle(size=10, fill_color='color')

# defines where our edges will be rendered `{ 'start': [0, 0, 1, 2, 3], 'end': [1, 3, 2, 3, 1] }`
# `start` refers to which node the edge will begin
# `end` refers to where the edge will end
graph_renderer.edge_renderer.data_source.data = { 'start': start, 'end': end }

# let our graph know where we want our nodes to render on the graph
graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=position)
plot.add_layout(labels)

plot.renderers.append(graph_renderer)

output_file('./graph.html')
# call `show` and give it our `plot`
show(plot)
