"""
General drawing methods for graphs using Bokeh.
"""

from random import choice, random, randint
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet, ColumnDataSource)
from graph import Graph


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


    def _setup_graph_renderer(self, circle_size):
        #source = ColumnDataSource(data={
        #"names": list(self.graph.vertices.keys())
        #})
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
        self._get_labels()

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
        def __random_helper():
            x = 1 + random() * (self.width - 2)
            y = 1 + random() * (self.height - 2)

            for item in self.pos:
                if self.pos[item][0] - x < 1 and x < 28:
                    x += 1
                elif self.pos[item][0] - x < 1:
                    x -= 5
                if self.pos[item][1] - y < 1 and y < 28:
                    y += 1
                elif self.pos[item][0] - y < 1:
                    print(self.pos[item][0])
                    y -= 5
            return x, y
        
        for vertex in self.graph.vertices:
            self.pos[vertex] = (__random_helper())

    def _get_labels(self):
        label_data = {"x": [], "y": [], "name": []}
        for vertex, edges in self.pos.items():
            label_data["x"].append(edges[0])
            label_data["y"].append(edges[1])
            label_data["name"].append(vertex)
        label_source = ColumnDataSource(label_data)

        labels = LabelSet(
            x="x",
            y="y",
            text="name",
            text_color="black",
            level="glyph",
            text_align="center",
            text_baseline="middle",
            text_line_height=1,
            source=label_source,
            render_mode="canvas",
        )
        self.plot.add_layout(labels)


def initiate_Graph(verts_num):
    new_graph = Graph()

    ints = []
    for x in range(0, verts_num):
        ints.append(x)

    for x in ints:
        new_graph.add_vert(f"v {x}")

    for x in range(0,int(verts_num * 1.25)):
        new_graph.add_edge(f"v {randint(0, verts_num - 1)}", f"v {randint(0, verts_num - 3) + 2}")
    return new_graph

x = initiate_Graph(10)



bokeh = BokehGraph(x, "AWESOME GRAPH!", 30, 30, True, True, 25)
bokeh.show()
