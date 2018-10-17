# # """
# # General drawing methods for graphs using Bokeh.
# # """

# # from bokeh.io import show, output_file
# # from bokeh.plotting import figure
# # from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
# #                           ColumnDataSource)

# # graph = {
# #     '0': {'1', '3'},
# #     '1': {'0'},
# #     '2': set(),
# #     '3': {'0'}
# # }

# # p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# # p.line(x, y, legend="Temp.", line_width=2)

# # class BokehGraph:
# #     """Class that takes a graph and exposes drawing methods."""
# #     def __init__(self):
# #         pass  # TODO

# import math

# from bokeh.io import show, output_file
# from bokeh.plotting import figure
# from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
# from bokeh.palettes import Spectral8
# from graph import Graph

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)

# class BokehGraph:



# N = len(graph.vertices)
# node_indices = list(graph.vertices)

# plot = figure(
#     title="Graph Layout Demonstration",
#     x_range=(-1.1, 10.1),
#     y_range=(-1.1, 10.1),
#     tools="",
#     toolbar_location=None,
# )

# graph_renderer = GraphRenderer()

# graph_renderer.node_renderer.data_source.add(node_indices, "index")
# graph_renderer.node_renderer.data_source.add(Spectral8, "color")
# graph_renderer.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color="color")

# start_indices = []
# end_indices = []

# for vertex in graph.vertices:
#     for edge_end in graph.vertices[vertex]:
#         start_indices.append(vertex)
#         end_indices.append(edge_end)

# graph_renderer.edge_renderer.data_source.data = dict(
#     start=start_indices, 
#     end=end_indices)

# ### start of layout code
# circ = [int(v) for v in graph.vertices]
# print("circ ", circ)
# x = [2 * (i // 3) for i in circ]
# y = [2 * (i % 3) for i in circ]

# graph_layout = dict(zip(node_indices, zip(x, y)))
# graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# plot.renderers.append(graph_renderer)

# output_file("graph.html")
# show(plot)


"""
Simple graph implementation compatible with BokehGraph class.
"""
import random


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add an vertex to the graph
        """
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def dft(self, starting_node, visited=None):
        # Mark the node as visited
        if visited is None:
            visited = []
        visited.append(starting_node)
        # For each child, if that child hasn't been visited, call dft() on that node
        for child in children:
            if child not in visited:
                dft(child, visted)
    def bft(self, starting_node):
        # create an empty queue
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(starting_node)
        visited = []
        while q.size() > 0:
            # Remove the first node from the queue...
            q.shift(first_node)
            # If it has not been visited yet,...
            if not first_node in visited:
            # Mark it as visited....
                visited.append(first_node)
            # Then put all it's children in the back of the queue
                for child of q:
                    q.append(child)




class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """
        Create an empty vertex
        """
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"
