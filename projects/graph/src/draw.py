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

		# I first get the keys and values of my vertices as two separate arrays

		keys = [i for i in self.graph.vertices.keys()]
		values = [i for i in self.graph.vertices.values()]

		#I start up two emtpy arrays that will store the starting and ending points
		#that I will use in the graph

		start = []
		end = []

		#I then loop through the array of values, each being its own python set

		for i, j in enumerate(values):

			#if I come across a set bigger than 0 it has an edge 
			#thus connecting to something

			if len(j) > 0:
				for q in range (0, len(j)):

					#I add the current index for spot in the set
					start.append(i)

					#I also add the current set value
					end += list(j)[q]

		graph = GraphRenderer()

		#I use my ordered values to form the connected lines in my graphs
		graph.edge_renderer.data_source.data = dict(
			start=start,
			end=end,
		)

		plot = figure(title='graph', x_range=(-1.1,1.1), y_range=(-1.1,1.1), tools='', toolbar_location=None)

		graph.node_renderer.data_source.add(keys, 'index')
		graph.node_renderer.data_source.add(Set3[7], 'color')
		graph.node_renderer.glyph = Circle(radius=.06, fill_color='color')

		# y = [15, 10, 10, 5, 5, 5, 5]
		# x = [0, -100, 100, -150, -50, 50, 150]

		circ = [int(i)*2*math.pi/8 for i in self.graph.vertices]
		x = [math.cos(i) for i in circ]
		y = [math.sin(i) for i in circ]

		source = ColumnDataSource(data=dict(
			y = y,
			x = x,
			names = keys
		))
		labels = LabelSet(x='x', y='y', text='names', level='glyph', x_offset=-5, y_offset=-10, source=source, render_mode='canvas')



		graph_layout = dict(zip(keys, zip(x, y)))
		graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)



		plot.renderers.append(graph)
		plot.add_layout(labels)

		output_file('graph.html')
		show(plot)

# drawn_tree = BokehGraph(binary_tree)

# drawn_tree.draw_graph()