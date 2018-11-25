import math
from graph import binary_tree

from bokeh.plotting import figure, show, output_file
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Set3
from bokeh.transform import jitter


class BokehGraph:
	"""Class that takes a graph and exposes drawing methods."""
	def __init__(self, graph):
		self.graph = graph
	def __str__(self):
		return f'{self.graph}'

	def draw_graph(self):

		node_indices = list(self.graph.vertices)

		start_indices = []
		end_indices = []

		graph = GraphRenderer()

		for vertex_id in self.graph.vertices:
			for edge_end in self.graph.vertices[vertex_id].edges:
				start_indices.append(vertex_id)
				end_indices.append(edge_end)

		#I use my ordered values to form the connected lines in my graphs
		graph.edge_renderer.data_source.data = dict(
			start=start_indices,
			end=end_indices,
		)

		plot = figure(title='graph', x_range=(-1.1,11.1), y_range=(-1.1,11.1), tools='', toolbar_location=None)

		graph.node_renderer.data_source.add(node_indices, 'index')
		graph.node_renderer.data_source.add([self.graph.vertices[vertex_id].color for vertex_id in self.graph.vertices], 'color')
		graph.node_renderer.glyph = Circle(radius=.5, fill_color='color')

		# grid = [int(i) for i in self.graph.vertices]
		# x = [2 * (i // 3) for i in grid]
		# y = [2 * (i % 3) for i in grid]

		x = [self.graph.vertices[vertex_id].x for vertex_id in self.graph.vertices]
		y = [self.graph.vertices[vertex_id].y for vertex_id in self.graph.vertices]

		source = ColumnDataSource(data=dict(
			y = y,
			x = x,
			names = [self.graph.vertices[vertex_id].value for vertex_id in self.graph.vertices]
		))

		labels = LabelSet(x='x', y='y', text='names', level='glyph', x_offset=-5, y_offset=-10, source=source, render_mode='canvas')

		graph_layout = dict(zip(node_indices, zip(x, y)))
		graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)



		plot.renderers.append(graph)
		plot.add_layout(labels)

		output_file('graph.html')
		show(plot)

drawn_tree = BokehGraph(binary_tree)

drawn_tree.draw_graph()