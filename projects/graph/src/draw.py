"""
General drawing methods for graphs using Bokeh.
"""
from graph import Graph, Vertex
from collections import deque
from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, 
                          LabelSet, ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=10, height=10,
                 show_axis=False, show_grid=False, circle_size=35):
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
        self.graph = graph
        self.width = width
        self.height = height
        self.circle_size = circle_size
        self.pos = {}  # dict to map vertices to x, y positions
        # Set up plot, the canvas/space to draw on
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        # The renderer will have the actual logic for drawing
        graph_renderer = GraphRenderer()

        # Add the vertex data as instructions for drawing nodes
        print('labels:',[x.label for x in self.graph.vertices.values()])
        graph_renderer.node_renderer.data_source.add(
            [x.label for x in self.graph.vertices.values()], 'index')
        # Nodes will be random colors
        graph_renderer.node_renderer.data_source.add(
            self._get_random_colors(), 'color')
        # And circles
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')

        # Add the edge [start, end] indices as instructions for drawing edges
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self._assign_pos()  # Randomize vertex coordinates, and set as layout
        print('self.pos:',self.pos)
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        # Attach the prepared renderer to the plot so it can be shown
        self.plot.renderers.append(graph_renderer)
        self._setup_labels()

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

        for vertex in self.graph.vertices.values():
            if vertex not in checked:
                for destination in vertex.edges:
                    start_indices.append(vertex.label)
                    end_indices.append(destination.label)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)

    def _assign_pos(self):
        """Assign vertex positions to self.pos"""
        for vertex in self.graph.vertices.values():
            # TODO make bounds and random draws less hacky
            # Attempt
            # self.pos[vertex] = (random.uniform(0, self.width),
            #                     random.uniform(0, self.height))
            if not vertex.pos:
                self.pos[vertex.label] = [
                                         0.35 + random() * (self.width - 0.5),
                                         0.35 + random() * (self.height - 0.5)
                                        ]
            else:
                self.pos[vertex.label] = vertex.pos
 
    def _setup_labels(self):
        label_data = {'x': [], 'y': [], 'names': []}

        for vertex, position in self.pos.items():
            label_data['x'].append(position[0])
            label_data['y'].append(position[1])
            label_data['names'].append(str(vertex))

        label_source = ColumnDataSource(label_data)
        # End Target
        # labels - LabelSet(...)
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                            text_align='center', text_baseline='middle',
                            source=label_source)
        self.plot.add_layout(labels)

    def color_connections(self, graph):
        connected_components = []

        for v in graph.vertices.values():
            v.color = 'white'

        for v in graph.vertices.values():
            component = None

            if v.color == 'white':
                component = self._bfs(v)
            if component:
                connected_components.append(component)

        return connected_components

    def _bfs(self, startVert):
        v_queue = deque()
        visited = set()

        if startVert.color != 'black':
            startVert.color = 'gray'
            visited.add(startVert)
            v_queue.append(startVert)

            while len(v_queue) > 0:
                u = v_queue[0]

                for vertex in u.edges:
                    if vertex.color == 'white':
                        vertex.color = 'gray'
                        visited.add(vertex)
                        v_queue.append(vertex)

                u.color = 'black'
                v_queue.popleft()

        return visited


class RandomGraph(BokehGraph):
    def __init__(self, width=5, height=4, chance=0.6, circle_size=20,
                 title='Graph', show_axis=True, show_grid=True):
        self.graph = Graph(width * height // 2, chance)

        BokehGraph.__init__(self, self.graph, title, width, height,
                            show_axis, show_grid, circle_size)


def main():
    graph = Graph()  # Instantiate your graph

    vl = [
        Vertex('0', (2, 5)),
        Vertex('1', (5, 2)),
        Vertex('2', (2, 8)),
        Vertex('3', (8, 2)),
    ]

    for v in vl:
        graph.add_vertex(v)

    graph.add_edge(vl[0], vl[1])
    graph.add_edge(vl[0], vl[3])
    print(graph.vertices)

    # a_graph = BokehGraph(graph)
    # print('start vertex:', a_graph.graph.vertices['0'].edges)
    # print('bfs result:', a_graph.color_connections(a_graph.graph))
    # a_graph.show()

    b_graph = RandomGraph()
    print("b_graph vertices:", b_graph.graph.vertices)
    print('start vertex:', b_graph.graph.vertices[0].edges)
    print('bfs result:', b_graph.color_connections(b_graph.graph))
    b_graph.show()


if __name__ == '__main__':
    main()
