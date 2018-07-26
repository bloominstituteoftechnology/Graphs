"""
General drawing methods for graphs using Bokeh.
"""
from bokeh.io import show, output_file
from bokeh.layouts import widgetbox
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle,
                          LabelSet, ColumnDataSource, MultiLine,
                          HoverTool, TapTool, BoxSelectTool)
from bokeh.models.graphs import NodesAndLinkedEdges, EdgesAndLinkedNodes
from bokeh.models.widgets import Button
from bokeh.plotting import figure
from graph import Graph
from math import floor
from random import choice, random


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
        self.plot = figure(title=title, x_range=(0, width),
                           y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self.plot.add_tools(HoverTool(tooltips=None), TapTool(), BoxSelectTool())
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        # The renderer will have the actual logic for drawing
        graph_renderer = GraphRenderer()

        # Add the vertex data as instructions for drawing nodes\
        graph_renderer.node_renderer.data_source.add(
            [x.label for x in self.graph.vertices.values()], 'index')
        # Nodes will be random colors
        self._color_connections(self.graph)
        graph_renderer.node_renderer.data_source.add(
            self._assign_colors(), 'color')
        # And circles
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')
        graph_renderer.node_renderer.selection_glyph = Circle(size=circle_size * 2,
                                                              fill_color='color')
        graph_renderer.node_renderer.hover_glyph = Circle(size=circle_size * 2,
                                                          fill_color='color')
        # And edges
        graph_renderer.edge_renderer.glyph = MultiLine(line_color='color',
                                                       line_alpha=0.8,
                                                       line_width=2)
        graph_renderer.edge_renderer.selection_glyph = MultiLine(line_color='color',
                                                                 line_width=5)
        graph_renderer.edge_renderer.hover_glyph = MultiLine(line_color='color',
                                                             line_width=5)
        # Add the edge [start, end] indices as instructions for drawing edges
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self._assign_pos()  # Randomize vertex coordinates, and set as layout
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        # Set 'dem policies, bruh
        graph_renderer.selection_policy = NodesAndLinkedEdges()
        graph_renderer.inspection_policy = EdgesAndLinkedNodes()
        # Attach the prepared renderer to the plot so it can be shown
        self.plot.renderers.append(graph_renderer)
        self._setup_labels()

    def _get_edge_indexes(self):
        """Generates a dict filled with start/end indicies for edges.
        The output of this method should be assigned to:
        graph_renderer.edge_renderer.data_source.data"""
        start_indices = []
        end_indices = []
        colors = []
        checked = set()

        for vertex in self.graph.vertices.values():
            if vertex not in checked:
                for destination in vertex.edges:
                    start_indices.append(vertex.label)
                    end_indices.append(destination.label)
                    colors.append(vertex.color if vertex.color else '#000000')
                checked.add(vertex)
        return dict(start=start_indices, end=end_indices, color=colors)

    def show(self, output_path='./graph.html'):
        """Generates the visual representation of the graph in HTML format"""
        output_file(output_path)
        show(self.plot)

    def _assign_pos(self):
        """Assign vertex positions to self.pos"""
        for vertex in self.graph.vertices.values():
            # TODO make bounds and random draws less hacky
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

        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                            text_align='center', text_baseline='middle',
                            text_color='#000000', source=label_source)
        self.plot.add_layout(labels)

    def _assign_colors(self):
        """Outputs a color array containing the hex RGB color value of each
           vertex. The value is based off the vertex's color property. If a
           given vertex does not have a valid color property (i.e. None), a
           random color is assigned.
           Output is meant to be used in:
           graph_renderer.node_renderer.data_source.add"""
        colors = []

        for v in self.graph.vertices.values():
            if v.color:
                colors.append(v.color)
            else:
                color = '#' + ''.join([choice('6789ABCDEF') for j in range(6)])
                colors.append(color)
        return colors

    def _color_connections(self, graph):
        """Assigns all vertices in a connected component the same random
           color"""
        connected_components = self.graph.find_connected_components()

        for component in connected_components:
            color = '#'+''.join([choice('6789ABCDEF') for j in range(6)])
            for vertex in component:
                vertex.color = color
        return connected_components


class RandomGraph(BokehGraph):
    """Class which automatically constructs a random graph and makes it
       Bokeh renderable"""
    def __init__(self, num_vertices=None, num_edges=None, chance=1, width=100,
                 height=100, circle_size=25, title='Graph', show_axis=True,
                 show_grid=True):
        self.num_vertices = num_vertices or floor(width * height * 0.0010)
        self.num_edges = num_edges or floor(self.num_vertices * 0.75)
        self.chance = chance
        self.width = width
        self.height = height
        self.circle_size = circle_size
        self.title = title
        self.show_axis = show_axis
        self.show_grid = show_grid
        self.graph = None
        # Create graph then pass it to super `BokehGraph`'s constructor
        # self.graph = self._generate_graph()
        # BokehGraph.__init__(self, self.graph, title, width, height,
        #                     show_axis, show_grid, circle_size)
        self._generate_graph()

    def _generate_graph(self):
        self.graph = Graph(self.num_vertices, self.num_edges, self.chance)
        BokehGraph.__init__(self, self.graph, self.title, self.width,
                            self.height, self.show_axis, self.show_grid,
                            self.circle_size)

    def _button_hander_new_graph(self):
        self._generate_graph()
        show(self.plot)

    def show(self, output_path='./graph.html'):
        """Generates the visual representation of the graph in HTML format"""
        output_file(output_path)
        show(self.plot)


def main():
    # graph = Graph()  # Instantiate your graph

    # vl = [
    #     Vertex('0', (2, 5)),
    #     Vertex('1', (5, 2)),
    #     Vertex('2', (2, 8)),
    #     Vertex('3', (8, 2)),
    # ]

    # for v in vl:
    #     graph.add_vertex(v)

    # graph.add_edge(vl[0], vl[1])
    # graph.add_edge(vl[0], vl[3])
    # print(graph.vertices)

    # a_graph = BokehGraph(graph)
    # a_graph.show()

    b_graph = RandomGraph()
    print('bfs result:', b_graph._color_connections(b_graph.graph))
    b_graph.show()


if __name__ == '__main__':
    main()
