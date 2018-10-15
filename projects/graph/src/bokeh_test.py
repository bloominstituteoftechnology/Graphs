# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle
from graph import Graph
from draw import BokehGraph

# setup some sample data
g = Graph()
g.add_vertex('0')
g.add_vertex('1')
g.add_vertex('2')
g.add_vertex('3')
g.add_vertex('4')
g.add_vertex('5')
g.add_vertex('6')
g.add_vertex('7')
g.add_edge('0', '1')
g.add_edge('0', '3')
g.add_edge('0', '5')
g.add_edge('2', '5')
g.add_edge('3', '4')
g.add_edge('6', '5')
g.add_edge('2', '6')

bokeh = BokehGraph(g)
bokeh.make_graph()
# # grab vertex keys for indexing
# node_indices = list(g.vertices.keys())
#
# # setup the graph box
# plot = figure(title='Graph Layout Demonstration', x_range=(-1, 6),
#               y_range=(-1, 6), tools='', toolbar_location=None)
#
# # create instance of graph
# graph = GraphRenderer()
#
# # append the index data_source, the list of nodes
# graph.node_renderer.data_source.add(node_indices, 'index')
# # define node shaping/coloring
# graph.node_renderer.glyph = Circle(size=30, fill_color='green')
#
# # this sets up start and end position for connecting lines
# # start_i is a list of vertex keys
# # end_i is a list of the keys that it connects to
# # these two lists have to be the same, so need to append to both for each
# # connection
# start_i = []
# end_i = []
# checked = set()
# for vert, edges in g.vertices.items():
#     if vert not in checked:
#         for d in edges.edges:
#             start_i.append(vert)
#             end_i.append(d)
#         checked.add(vert)
#
# # pass the two lists as a dict to edge_renderer
# graph.edge_renderer.data_source.data = dict(
#     start=start_i,
#     end=end_i)
#
# # setup x, y coords of the nodes, text as well, but not implemented
# names = []
# x = []
# y = []
# for vertex in g.vertices:
#     names.append(g.vertices[vertex].label)
#     x.append(g.vertices[vertex].x)
#     y.append(g.vertices[vertex].y)
#
# # create a dict out of the index, and x, y positions, pass to provider
# # is there a way to get the class to format all of these and send them back
# graph_layout = dict(zip(node_indices, zip(x, y)))
# graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
#
# # append graph to box
# plot.renderers.append(graph)
#
# # output
# output_file('graph.html')
# show(plot)
