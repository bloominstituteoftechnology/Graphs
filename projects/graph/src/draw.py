"""
General drawing methods for graphs using Bokeh.
"""

from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=10, height=10,
    show_axis=False, show_grid=False, circle_size=35):
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
        self.graph = graph
        """go to sleep, duuuuuudddeeee"""
        self.width = width
        self.height = height
        self.pos = {}
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()) , 'index')
        graph_renderer.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()           
        self.randomize() 
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)  
        self.plot.renderers.append(graph_renderer)                        

    def _get_random_colors(self):
        colors = []
        for _ in range(len(self.graph.vertices)):
            color = "#"+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors

    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()
        # for key, value in dictionary.items():
        # Double check this but, some_dictionary.items()
        # will return a list of tuples. Each tuple will
        # be a key, value pair e.g. ('0', {'1', '3'})
        # in our implementation, it would be (string, vertex object)
        for key, vertex in self.graph.vertices.items():
            if key not in checked:
                for destination in vertex.get_edges():
                    start_indices.append(key)
                    end_indices.append(destination)
                checked.add(key)
        return dict(start=start_indices, end=end_indices)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)
    
    def randomize(self):
        #Randomize vertex positions.
        for vertex in self.graph.vertices:
            self.pos[vertex] = (1 + random() * (self.width -2),
                                1 + random() * (self.height -2))

def main():
    from graph import Graph
    from draw import BokehGraph
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_edge('0', '1')
    graph.add_edge('2', '1')
    bg = BokehGraph(graph)
    dir(bg)
    bg.pos
    bg.show()

if __name__ == '__main__':
    main()
        


