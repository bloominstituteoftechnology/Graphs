"""
General drawing methods for graphs using Bokeh.
"""
from bokeh.io import output_notebook, output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, GraphRenderer, StaticLayoutProvider, LabelSet, Circle, HoverTool, MultiLine
from bokeh.palettes import Category20c
from bokeh.models.graphs import NodesAndLinkedEdges
import math

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        self.graph = graph

    def show(self):
        #Get list of nodes
        nodes = list(self.graph.vertices.keys())

        #Create plot figure
        plot = figure(title = 'Graph Plot', x_range = (-1.5, 1.5) , y_range = (-1.5, 1.5), tools = "", toolbar_location = None)
              
        #create a GraphRenderer Object
        G = GraphRenderer()

        #map nodes to node_renderer and format glyph for nodes
        G.node_renderer.glyph = Circle(radius = 0.1, fill_color = "fill_color")
        G.node_renderer.data_source.data = dict(
            index = nodes,
            fill_color = Category20c[14]
            )

        #Get start and end list of edges
        edge_starts = []
        edge_ends = []
        for k, v in self.graph.vertices.items():
            edge_starts += [k]*len(v)
            edge_ends += v

        #map data to edge_renderer and format glyph for edges
        G.edge_renderer.glyph = MultiLine(line_color="#cccccc", line_alpha=0.8, line_width=2)
        G.edge_renderer.data_source.data = dict(
            start = edge_starts,
            end = edge_ends)

        #add hover effects for nodes and edges
        G.node_renderer.hover_glyph = Circle(radius=0.3)
        G.edge_renderer.hover_glyph = MultiLine(line_color='#abdda4', line_width=4)

        # When we hover over nodes, highlight adjecent edges too
        G.inspection_policy = NodesAndLinkedEdges()

        #setup layout coordinates
        circ = [i*2*math.pi/14 for i in range(14)]
        x = [math.cos(i) for i in circ]
        y = [math.sin(i) for i in circ]

        graph_layout = dict(zip(nodes, zip(x, y)))
        G.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
        
        #setup labels
        data = {
                'x': x,
                'y': y,
                'name': nodes
               }
        source = ColumnDataSource(data)
        labels = LabelSet(x="x", y="y", text="name", y_offset = -5,
                        text_font_size="12pt", text_color="#555555",
                        source=source, text_align='center')
        
        #add 
        plot.renderers.append(G)
        #Add hovering tool
        plot.add_tools(HoverTool(tooltips=None))
        #Add node label
        plot.add_layout(labels)

        #save file to graph.html
        output_file('graph.html')

        #show plot
        show(plot)
