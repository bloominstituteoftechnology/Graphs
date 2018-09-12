"""
General drawing methods for graphs using Bokeh.
"""
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, Oval, 
                        ColumnDataSource, MultiLine)
from bokeh.models.graphs import NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.palettes import Spectral8, Spectral4, inferno

# from graph import Graph

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    def render(self):
        N = len(self.graph.vertices)

        # Get ref to all node/vertex indexes from the keys of vertices
        node_indices = list(self.graph.vertices.keys())
        
        # Create a plot / figure
        plot = figure(title='Graph Layout Demonstration', 
                    x_range=(-1,math.sqrt(N)+1), 
                    y_range=(-1,math.sqrt(N)+1),
                    tools='', toolbar_location=None)

        # Add Data (Node/Edge) Sources
        graph = GraphRenderer()
        graph.node_renderer.data_source.add(node_indices, 'index')
        graph.node_renderer.data_source.add(inferno(N), 'color')
        graph.node_renderer.glyph = Circle(radius=.3, fill_color='color')

        # Create the edge renderer data
        start_indices = []
        end_indices = []

        for vertex in self.graph.vertices:
            for edge_end in self.graph.vertices[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge_end)
        
        print(start_indices)
        print(end_indices)

        graph.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)

        # Sibhat's method, all edges don't get drawn?
        # Get ref to all lists of each connected node
        # connected_nodes_lists = [list(v) for (k,v) in self.graph.vertices.items()]
        
        # graph.edge_renderer.data_source.data = dict(
        #     start=node_indices,
        #     end=connected_nodes_lists)

        #Layout code
        # Grid or Square Layout
        grid = [int(v) for v in self.graph.vertices]
        x = [(i // math.ceil(math.sqrt(N))) for i in grid]
        y = [(i % math.ceil(math.sqrt(N))) for i in grid]
        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        # Circular Layout
        # circ = [i*2*math.pi/8 for i in node_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]

        # Create the labels
        labelSource = ColumnDataSource(data = dict(x=x, y=y, names= grid))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', 
            text_align='center', text_baseline='middle', source=labelSource,
            render_mode='canvas')
        
        # Render the plot
        plot.renderers.append(graph)
        plot.add_layout(labels)
        output_file('graph.html')
        show(plot)


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(f"Graph vertices: {graph.vertices}")

# bg = BokehGraph(graph)
# bg.render()
