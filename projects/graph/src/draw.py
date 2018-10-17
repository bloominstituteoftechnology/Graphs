import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral4
from graph import Graph, Vertex

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph
        self.keys = []
        self.values = []
        # this mess below here is to turn a key value pair
        # which is 'vertex_name': node object with set of edges
        # to two lists of connections between each vertex
        # e.g. input: { '0': {'1', '3'} }
        #      output: [0, 0], [1, 3]
        for key in self.graph.vertices:
            for vertex in self.graph.vertices[key].edges:
                self.keys.append(key)
                self.values.append(vertex) 
            

    def draw(self):
        print('self.graph.vertices:',self.graph.vertices)
        N = len(self.graph.vertices)
        node_indices = list(self.graph.vertices.keys())
        print('node_indices:', node_indices)

        plot = figure(title="Graph Layout Demonstration", x_range=(-7,7), y_range=(-7,7), tools="", toolbar_location=None)

        graph = GraphRenderer()

        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(Spectral4, 'color')
        graph.node_renderer.glyph = Oval(height=0.1, width=0.2, fill_color="color")

        print(f"self.keys: {self.keys} self.values: {self.values}")
        graph.edge_renderer.data_source.data = dict(
            start=self.keys,
            end=self.values)

        ### start of layout code
        circ = [int(i)*2*math.pi/8 for i in node_indices]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]
        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        ### Draw quadratic bezier paths
        # def bezier(start, end, control, steps):
        #     return [(1-s)**2*start + 2*(1-s)*s*control + s**2*end for s in steps]

        # xs, ys = [], []
        # sx, sy = graph_layout[0]
        # steps = [i/100. for i in range(100)]
        # for node_index in node_indices:
        #     ex, ey = graph_layout[node_index]
        #     xs.append(bezier(sx, ex, 0, steps))
        #     ys.append(bezier(sy, ey, 0, steps))
        # graph.edge_renderer.data_source.data['xs'] = xs
        # graph.edge_renderer.data_source.data['ys'] = ys

        plot.renderers.append(graph)

        output_file("graph.html")
        show(plot)

def main():
    # shit happens here
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    test_graph = BokehGraph(graph)
    test_graph.draw()

if __name__ == '__main__':
    main()                                                    