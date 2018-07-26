"""
General drawing methods for graphs using Bokeh.
"""
from graph import Graph
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

        # Setup plot
        self.width = width
        self.height = height
        self.pos = {}  # dict to map vertices to x, y positions
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)


    def _setup_graph_renderer(self, circle_size, ):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
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
            color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors

    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()

        for vertex, edges in self.graph.vertices.items():
            if vertex not in checked:
                for destination in edges:
                    start_indices.append(vertex)
                    end_indices.append(destination)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.graph.vertices:
            # TODO make bounds and random draws less hacky
            self.pos[vertex] = (1 + random() * (self.width - 2),
                                1 + random() * (self.height - 2))

def main():
    graph = Graph()

    graph.add_vortex('A')
    graph.add_vortex('B')
    graph.add_vortex('C')
    graph.add_vortex('D')
    graph.add_vortex('E')
    graph.add_vortex('F')
    graph.add_vortex('G')
    graph.add_vortex('H')
    graph.add_vortex('I')
    graph.add_vortex('J')

    graph.add_edge('H','A','J',)
    graph.add_edge('B','D','J',)
    graph.add_edge('B','F','E',)
    graph.add_edge('B','F','A',)
    graph.add_edge('B','C','G',)
    graph.add_edge('D','I','G',)
    graph.add_edge('D','I','A',)
    graph.add_edge('J','I','J',)
    graph.add_edge('A','G')
    graph.add_edge('E','I')
    graph.add_edge('B','J')
    graph.add_edge('H','E')
    graph.add_edge('B','F')
    graph.add_edge('H','C','J',)
    graph.add_edge('B','A','J',)
    graph.add_edge('B','H','E',)
    graph.add_edge('B','F','B',)
    graph.add_edge('B','E','G',)
    graph.add_edge('D','I','G',)
    graph.add_edge('B','I','A',)
    graph.add_edge('J','I','F',)

    bg = BokehGraph(graph)
    
    print(bg.pos)
    print(bg.pos.keys())
    bg.show()

if __name__ == '__main__':
    main()
        
    


