"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)
from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        self.graph = graph
        self.graph_data = self.graph.vertices
        self.x = []
        self.y = []

    # def map_x_y_lists(self):
    #     for val in graph

    def tellme(self):
        output_file("lines.html")
        x = [1, 2, 3, 4, 5]
        y = [6, 7, 2, 4, 5]
        p = figure(plot_width=600, plot_height=600)
        # p.line(x, y, legend="Temp.", line_width=2)
        p.diamond(x, y, size=335, line_color="pink", fill_color="#b7d2ff", fill_alpha=0.6)
        # show(p)

    def create_data_lists(self):
        for key in self.graph_data:
            for val in self.graph_data[key]:
                self.x.append(key)
                self.y.append(val)
                print(f"x of x list:: {self.x}, y of y list:: {self.y}")

    def 



graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('2', '3')
graph.add_edge('5', '2')
graph.add_edge('6', '1')
graph.add_edge('4', '6')
graph.add_edge('1', '6')
print(graph.vertices)

bok = BokehGraph(graph)
bok.tellme()
bok.create_data_lists()


