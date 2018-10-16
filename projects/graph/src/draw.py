"""
General drawing methods for graphs using Bokeh.
"""
from bokeh.io import output_notebook, output_file, show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, GraphRenderer, StaticLayoutProvider, LabelSet, Circle, MultiLine
from bokeh.palettes import Category20c
from bokeh.models.graphs import NodesAndLinkedEdges
from graph import Graph
import math

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph=graph
    
    def show(self):
        nodes = list(self.graph.vertices.keys())
        N=len(nodes)

        #Create plot
        plot = figure(title = 'Graph', x_range = (-7, 7) , y_range = (-7, 7), tools = "", toolbar_location = None)

        g = GraphRenderer()
        
        g.node_renderer.glyph = Circle(radius = 0.5, fill_color = "fill_color")  
        g.node_renderer.data_source.data = dict(
            index = nodes,
            fill_color = ['red']*N
            )

        '''start_edge = []
        end_edge = []
        for keys, values in self.graph.vertices.items():
            start_edge += [keys]*len(values)
            end_edge += values'''

        edge_start = []
        edge_end = []
        
        for vertex_id in nodes:
            for value in graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(value)    

        g.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end)

        ##start of layout code
        #circ = [i*2*math.pi/len(nodes) for i in range(len(nodes))]
        #x = [math.cos(i) for i in circ]
        #y = [math.sin(i) for i in circ]
        
        x = []
        y = []

        for vertex_id in nodes:
            vertex = graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)
        
        graph_layout = dict(zip(nodes, zip(x, y)))
        g.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
        
        #add labels to the graph
        labels_data = {
                'x': x,
                'y': y,
                'name': nodes
               }

        source = ColumnDataSource(labels_data)
        labels = LabelSet(x="x", y="y", text="name", y_offset = -5,
                        text_font_size="12pt", text_color="white",
                        source=source, text_align='center')


        plot.renderers.append(g)

        plot.add_layout(labels)

        output_file('graph.html')

        show(plot)



graph=Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_undirected_edge('0', '1')
graph.add_undirected_edge('0', '3')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('1', '4')
graph.add_directed_edge('4', '5')
graph.add_directed_edge('4', '6')
graph.breadth_first_search('0')
#graph.add_directed_edge('7','4')
#graph.add_directed_edge('7','4')
g1 = BokehGraph(graph)
g1.show()
