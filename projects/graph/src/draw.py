"""
General drawing methods for graphs using Bokeh.
"""
from graph import Graph
from random import sample
from sys import argv
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
        self._setup_labels()


    def _setup_graph_renderer(self, circle_size):
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

    def _setup_labels(self):
        label_data = {'x': [], 'y': [], 'names': []}
        for vertex, position in self.pos.items():
            label_data['x'].append(position[0])
            label_data['y'].append(position[1])
            label_data['names'].append(str(vertex))
        label_source = ColumnDataSource(label_data)
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                          text_align='center', text_baseline='middle',
                          source=label_source, render_mode='canvas')
        self.plot.add_layout(labels)

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


def main(num_vertices=8, num_edges=8):
    graph = Graph()  # Instantiate your graph

    # random way
    # for num in range(num_vertices):
    #     graph.add_vertex(str(num))
    
    # for _ in range(num_edges):
    #     vertices = sample(graph.vertices.keys(), 2)
    #     graph.add_edge(vertices[0], vertices[1])

    # print(len(vertices))

    # graph.bfs("1")
    # hard coded way
    
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_vertex('5')
    graph.add_vertex('6')
    graph.add_vertex('7')
    graph.add_vertex('8')
    graph.add_vertex('9')
    graph.add_vertex('10')


    graph.add_edge('2', '10')
    graph.add_edge('2', '7')
    graph.add_edge('2', '4')
    graph.add_edge('7', '3')
    graph.add_edge('3', '8')
    graph.add_edge('4', '5')
    graph.add_edge('5', '3')
    graph.add_edge('2', '8')

    # graph.add_edge('1', '10')
    # graph.add_edge('2', '7')
    # graph.add_edge('3', '2')
    # graph.add_edge('4', '10')
    # graph.add_edge('5', '6')
    # graph.add_edge('8', '9')
    # graph.add_edge('2', '5')
    # graph.add_edge('2', '6')
    # graph.add_edge('7', '6')
    # graph.add_edge('9', '3')
    # graph.add_edge('5', '8')

    graph.bfs("2")




    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    if len(argv) == 3:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        main(NUM_VERTICES, NUM_EDGES)
    main()
print(__name__)


