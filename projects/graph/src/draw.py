import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, Circle
from bokeh.palettes import Inferno8
from graph import Graph
import random

class BokehGraph:
    def __init__(self, newGraph=None):
        # Instantiate your graph
        if newGraph: self.graph = newGraph
        else:
            self.graph = Graph()
            self.graph.addVertex('0')
            self.graph.addVertex('1')
            self.graph.addVertex('2')
            self.graph.addVertex('3')
            self.graph.addEdge('0', '1')
            self.graph.addEdge('0', '3')
            print(self.graph.vertices)
        
    def show(self):
        N = len(self.graph.vertices)
        node_indices = list(self.graph.vertices)

        plot = figure(title='Graph Layout Demonstration', x_range=(-1.1,10.1), y_range=(-1.1,10.1),
              tools='', toolbar_location=None)
        
        graph_renderer = GraphRenderer()
        graph_renderer.node_renderer.data_source.add(node_indices, 'index')
        graph_renderer.node_renderer.data_source.add(getColors(N), 'color')
        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color='color')

        start_indices = []
        end_indices = []

        for vertex in self.graph.vertices:
            for edge_end in self.graph.vertices[vertex]:
                start_indices.append(vertex)
                end_indices.append(edge_end)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=start_indices,
            end=end_indices)

        ### start of layout code
        circ = [int(v) for v in self.graph.vertices]
        x = [2 * (i // 3) for i in circ]
        y = [2 * (i % 3) for i in circ]

        # x = [2 * (i // 3) for i in node_indices]
        # y = [2 * (i % 3) for i in node_indices]


        graph_layout = dict(zip(node_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        output_file('graph.html')
        show(plot)

def getColors(numIndices):
    def randomColor():
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white', 'black']
        return colors[random.randint(0, len(colors) - 1)]
    count = 0
    colorArr = []
    while count < numIndices:
        colorArr.append(randomColor())
        count += 1
    return colorArr

    

# mygraph = BokehGraph()
# mygraph.show()










