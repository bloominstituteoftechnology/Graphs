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
        self.width = width
        self.height = height
        self.pos = {}  # dict to map vertices to x, y positions
        # Set up plot, the canvas/space to draw on
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)
        self._setup_labels()


    def _setup_graph_renderer(self, circle_size):
        # The renderer will have the actual logic for drawing
        graph_renderer = GraphRenderer()

        # Add the vertex data as instructions for drawing nodes
        graph_renderer.node_renderer.data_source.add(
            list(self.graph.vertices.keys()), 'index')
        # Nodes will be random colors
        graph_renderer.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        # And circles
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')

        # Add the edge [start, end] indices as instructions for drawing edges
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()  # Randomize vertex coordinates, and set as layout
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        # Attach the prepared renderer to the plot so it can be shown
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
    graph = Graph()  # Instantiate your graph
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
    graph.add_edge('0', '1')
    graph.add_edge('0', '2')
    graph.add_edge('1', '3')
    graph.add_edge('1', '4')
    graph.add_edge('2', '5')
    graph.add_edge('2', '6')
    graph.add_edge('3', '1')
    graph.add_edge('4', '8')
    graph.add_edge('5', '9')
    graph.add_edge('9', '10')
    bg = BokehGraph(graph)
    bg.show()
if __name__ == '__main__':
    main()
print(__name__)