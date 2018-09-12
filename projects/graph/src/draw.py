"""
General drawing methods for graphs using Bokeh.
"""
import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource, Label, LabelSet
from bokeh.palettes import Spectral8, all_palettes
from graph import Graph
import random

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
    def draw(self):
        graph = self.graph
        N = len(graph.vertices)
        node_indices = list(graph.vertices)

        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,35), y_range=(-1.1,4.5),
                      tools='', toolbar_location=None, plot_width=1450, plot_height=1000)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add([graph.vertices[vertex_id].color for vertex_id in graph.vertices], 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex_id in graph.vertices:
            for edge_end in graph.vertices[vertex_id].edges:
                start_indices.append(vertex_id)
                end_indices.append(edge_end)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)

        ### start of layout code
        x = [graph.vertices[vertex_id].x for vertex_id in graph.vertices]
        y = [graph.vertices[vertex_id].y for vertex_id in graph.vertices]


        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[graph.vertices[vertex_id].value for vertex_id in graph.vertices]))
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                     text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')


        plot.add_layout(labels)


        output_file('graph.html')
        show(plot)


# class BokehGraph2:
#     def __init__(self, graph):
#         self.graph = graph
#     def draw(self):
#         graph = self.graph
#         N = len(graph.vertices)
#         node_indices = list(graph.vertices)

#         plot = figure(title="My Graph", x_range=(-3, 40), y_range=(-3,40), tools='', toolbar_location=None)

#         graph_renderer = GraphRenderer()

#         graph_renderer.node_renderer.data_source.add(node_indices, 'index')
#         graph_renderer.node_renderer.data_source.add([graph.vertices[vertex_id].color for vertex_id in graph.vertices], 'color')
#         graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

#         start_indices = []
#         end_indices = []

#         for vertex_id in graph.vertices:
#             for edge_end in graph.vertices[vertices_id].edges:
#                 start_indices.append(vertex_id)
#                 end_indices.append(edge_end)

#         graph_renderer.edge_renderer.data_source.data = dict(
#             start=start_indices,
#             end=end_indices
#         )

#         x = [graph.vertices[vertex_id].x for vertex_id in graph.vertices]
#         y = [graph.vertices[vertex_id].y for vertex_id in graph.vertices]

#         graph_layout = dict(zip(node_indices), zip(x,y)))
#         graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

#         plot.renderers.append(graph_renderer)

#         labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[graph.vertices[vertex_id].value for vertex_id in graph.vertices]))
#         labels = LabelSet(x='x', y='y', text='names', level='glyph', text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

#         plot.add_layout(labels)

#         output_file('Day3_graph.html')
#         show(plot)


# class BokehGraph:
#     """Class that takes a graph and exposes drawing methods."""
#     def __init__(self, graph=None, title="My Graph"):
#         self.graph = Graph()
#         self.p = figure(
#             title=title,
#             x_range=(-3,40),
#             y_range=(-3,20),
#             tools="",
#             toolbar_location=None,
#             plot_width=1450,
#             plot_height=500
#         )

#     def make_graph(self):
#         N = len(self.graph.vertices)
#         node_indices = list(self.graph.vertices)
#         graph_renderer = GraphRenderer()
#         graph_renderer.node_renderer.data_source.add(node_indices, "index")
#         graph_renderer.node_renderer.data_source.add(Spectral8[:N], "color")
#         graph_renderer.node_renderer.glyph = Circle(radius=0.75, fill_color="color")
#         start_indices = []
#         end_indices = []
#         for vertex_id in self.graph.vertices:
#             for edge_end in self.graph.vertices[vertex_id].edges:
#                 start_indices.append(vertex_id)
#                 end_indices.append(edge_end)
#         graph_renderer.edge_renderer.data_source.data = dict(
#             start=start_indices,
#             end=end_indices
#         )
#         grid = [int(v) for v in self.graph.vertices]
#         # x = [6 * (i // 4) for i in grid]
#         # y = [6 * (i % 4) for i in grid]
#         x = [graph.vertices[vertex_id].x for vertex_id in graph.vertices]
#         y = [graph.vertices[vertex_id].y for vertex_id in graph.vertices]
#         graph_layout = dict(zip(node_indices, zip(x, y)))
#         graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
#         self.p.renderers.append(graph_renderer)
#         labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
#         labels = LabelSet(x="x", y="y", text= "names", level="glyph", text_align="center", text_baseline="middle", source= labelSource, render_mode="canvas")
#         self.p.add_layout(labels)

#     def show_graph(self, output_path="./BokehGraph.html"):
#         output_file(output_path)
#         show(self.p)


# myGraph = Graph()  # Instantiate your graph
# myGraph.add_vertex('0')
# myGraph.add_vertex('1')
# myGraph.add_vertex('2')
# myGraph.add_vertex('3')
# myGraph.add_vertex('4')
# myGraph.add_vertex('5')
# myGraph.add_vertex('6')
# myGraph.add_vertex('7')
# myGraph.add_vertex('8')
# myGraph.add_vertex('9')
# myGraph.add_vertex('10')
# myGraph.add_vertex('11')
# myGraph.add_vertex('12')
# myGraph.add_vertex('13')
# myGraph.add_vertex('14')
# myGraph.add_vertex('15')
# myGraph.add_vertex('16')
# myGraph.add_vertex('17')
# myGraph.add_vertex('18')
# myGraph.add_vertex('19')
# myGraph.add_vertex('20')
# myGraph.add_vertex('21')
# myGraph.add_vertex('22')
# myGraph.add_vertex('23')
# myGraph.add_vertex('24')
# myGraph.add_vertex('25')
# myGraph.add_vertex('26')
# myGraph.add_vertex('27')
# myGraph.add_edge('0', '1')
# myGraph.add_edge('0', '5')
# myGraph.add_edge('2', '4')
# myGraph.add_edge('3', '7')
# myGraph.add_edge('2', '6')
# myGraph.add_edge('6', '9')
# myGraph.add_edge('5', '8')
# myGraph.add_edge('7', '11')
# myGraph.add_edge('8', '13')
# myGraph.add_edge('10', '11')
# myGraph.add_edge('10', '13')
# myGraph.add_edge('11', '14')
# myGraph.add_edge('12', '16')
# myGraph.add_edge('13', '17')
# myGraph.add_edge('14', '15')
# myGraph.add_edge('15', '19')
# myGraph.add_edge('16', '17')
# myGraph.add_edge('17', '18')
# myGraph.add_edge('17', '20')
# myGraph.add_edge('17', '22')
# myGraph.add_edge('18', '21')
# myGraph.add_edge('20', '27')
# myGraph.add_edge('21', '24')
# myGraph.add_edge('22', '27')
# myGraph.add_edge('23', '26')
# myGraph.add_edge('24', '25')
# myGraph.add_edge('25', '26')
# print(f"Hey, these are the vertices: {myGraph.vertices}")

# N = len(myGraph.vertices)
# node_indices = list(myGraph.vertices)


# plot = figure(title="graph layout demo", x_range=(-3,40), y_range=(-3,20), tools='', toolbar_location=None, plot_width=1450, plot_height=500)

# graph_renderer = GraphRenderer()

# graph_renderer.node_renderer.data_source.add(node_indices, 'index')
# graph_renderer.node_renderer.data_source.add(['teal', 'green', 'crimson', 'blue', 'cyan', 'orange', 'yellow', 'olive', 'gold', 'pink', 'red', 'white', 'magenta', 'aquamarine', 'turquoise', 'gray', 'salmon', 'lemonchiffon', 'khaki', 'chartreuse', 'mediumspringgreen', 'seagreen', 'darkcyan', 'hotpink', 'blueviolet', 'skyblue', 'navy', 'lightcoral'], 'color')
# # graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color='color')
# graph_renderer.node_renderer.glyph = Circle(radius=0.75, fill_color='color')

# start_indices = []
# end_indices = []

# for vertex in myGraph.vertices:
#     for edge_end in myGraph.vertices[vertex]:
#         start_indices.append(vertex)
#         end_indices.append(edge_end)
# print(start_indices)
# print(end_indices)

# graph_renderer.edge_renderer.data_source.data = dict(
#     start=start_indices,
#     end=end_indices
# )

# # layout
# # circ = [i*2*math.pi/8 for i in node_indices]
# # x = [math.cos(i) for i in circ]
# # y = [math.sin(i) for i in circ]
# grid = [int(v) for v in myGraph.vertices]
# x = [6 * (i // 4) for i in grid]
# y = [6 * (i % 4) for i in grid]
# # x = [i for i in grid]
# # y = [i ** 2 for i in grid]

# graph_layout = dict(zip(node_indices, zip(x, y)))
# graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# # graph_layout = dict(zip(node_indices, zip(x, y)))
# # graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# plot.renderers.append(graph_renderer)

# labelSource = ColumnDataSource(data=dict(x=x, y=y, names=grid))
# labels = LabelSet(x='x', y='y', text= 'names', level='glyph', text_align='center', text_baseline='middle', source= labelSource, render_mode='canvas')

# # p.circle([1,2,3,4,5],[5,6,5,5,3],size=5,color="red")
# # p.triangle([1,2,3,4,5],[5,6,5,5,3],size=12,color="red")
# # p.triangle([1,2,3,4,5],[5,6,5,5,3],size=[10,10,10,10,10],color="red")

# plot.add_layout(labels)

# output_file("Day 2 Testing Graphs.html")
# show(plot)

################## earlier attempts below
# show(p)

# N = len(graph.vertices)
# node_indices = list(graph.vertices)

# start_indices = []
# end_indices = []

# for vertex in graph.vertices:
#     for edge in graph.vertices[vertex]:
#         start_indices.append(vertex)
#         end_indices.append(edge_end)

# graph_renderer.layout_provider = StaticLayoutProvider(graph_layout)

# labels = LabelSet(x='x', y='y', text='names', level='glyph', text_align='center', text_baseline='middle', source=labelSource )


# N = 8
# node_indices = list(range(N))

# # dataframe=pandas.DataFrame(columns=["X", "Y"])
# # dataframe["X"]=[1,2,3,4,5]
# # dataframe["Y"]=[5,6,4,5,3]

# # p=Scatter(dataframe, x="X", y="Y", title="Temperature Observations", xlabel="Day of observations", ylabel="Temperature")

# # output_file("Scatter_charts.html")

# # show(p)


# p=figure(plot_width=500,plot_height=400,title="This is the title, now")
# p=figure(
#     plot_width=500,
#     plot_height=400,
#     title="Learning to Graph using Bokeh",
#     tools='',
#     toolbar_location=None
# )