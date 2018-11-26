import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Label, LabelSet
from bokeh.palettes import Spectral8
from graph import Graph
from random import sample

class BokehGraph:
    def __init__(self, graph, draw_components=True):
        self.graph = graph
    def draw(self):
        myGraph = self.graph
        N = len(myGraph.vertices)
        # node_indices = list(myGraph.vertices.keys())

        plot = figure(title="Graph Layout Demonstration", x_range=(-7, 7), y_range=(-7, 7),
                    tools="", toolbar_location=None)

        graph = GraphRenderer()

        print("BFT", myGraph.BFT(myGraph.vertices[0].id))
        connected = myGraph.connected_components()
        node_indices = connected
        print("NI", node_indices)
        # graph.node_renderer.data_source.add(range(N), 'index')
        graph.node_renderer.data_source.add(
            [vertex for vertex in list(self.graph.vertices.keys())], 'index')
        hex_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        # print(random_color)
        component_colors = []
        for v in myGraph.vertices:
            # print(myGraph.vertices[v].color)
            component_colors.append(f"#{''.join(sample(hex_keys, 6))}")
            # myGraph.vertices[v].color = component_colors[myGraph.vertices[v].component]
        vertex_colors = []
        for vertex in myGraph.vertices:
            vertex_colors.append(component_colors[myGraph.vertices[vertex].component])
        print(vertex_colors)
        graph.node_renderer.data_source.add(vertex_colors, 'color')
        graph.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

        edge_start = []
        edge_end = []

        for vertex_id in range(N):
            for v in myGraph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(v)

        graph.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)
        

        ### start of layout code
        # circ = [i*2*math.pi/8 for i in node_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]
        x = []
        y = []
        for vertex_id in range(N):
            vertex = myGraph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)
        graph_layout = dict(zip(range(N), zip(x, y)))
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

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[vertex_id for vertex_id in myGraph.vertices]))
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                text_align='center', text_baseline='middle', source=labelSource, render_mode='canvas')

        plot.add_layout(labels)

        output_file("graph.html")
        show(plot)


# graph = Graph()
# graph.add_vertex(0)
# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)

# graph.add_edge(0, 1)
# graph.add_edge(0, 3)

# bokehGraph = BokehGraph(graph)
# bokehGraph.draw()








