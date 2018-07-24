"""
General drawing methods for graphs using Bokeh.
"""
import math

from graph import Graph

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          Oval, ColumnDataSource)
from bokeh.palettes import Spectral4


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
        self.node_indices = graph.vertices.keys()

    def __get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set() # study this more

        # you can iterate for both keys and values at the same time
        # for a given dict with `items()`
        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.append(vertex)
                    end_indices.append(destination)
                    checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def render(self):
        plot = figure(title="Graph Layout Demonstration", x_range=(-1.1,1.1), y_range=(-1.1,1.1),
              tools="", toolbar_location=None)
        
        graph = GraphRenderer()

        graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color="fill_color")

        graph.node_renderer.data_source.data = dict(
            index=list(self.node_indices),
            fill_color=Spectral4)
        
        graph.edge_renderer.data_source.data = self.__get_edge_indexes()

        print('node_indicies:',self.node_indices)
        ### start of layout code
        circ = [float(i)*2*math.pi/4 for i in self.node_indices]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]

        graph_layout = dict(zip(self.node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph)

        output_file('graph.html')
        show(plot)
    
def main():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

    b_graph = BokehGraph(graph)
    b_graph.render()

if __name__ == '__main__':
    main()