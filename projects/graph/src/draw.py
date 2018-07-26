"""
General drawing methods for graphs using Bokeh.
"""

import itertools
from bokeh.palettes import brewer
from graph import Graph
from random import choice, random
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle,
                          LabelSet, ColumnDataSource, HoverTool)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=10, height=10,
                 show_axis=False, show_grid=False, circle_size=35,):
        if not graph.vertices:
            raise Exception('Graph should contain vertices!')
        self.graph = graph

        # Setup plot
        self.width = width
        self.height = height
        self.pos = {}  # dict to map vertices to x, y positions
        self.plot = figure(title=title, x_range=(
            0, width * 2), y_range=(0, height * 2), width=800, height=600)
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)
        self._setup_labels()

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(
            list(sorted(self.graph.vertices.keys())), 'index')
        graph_renderer.node_renderer.data_source.add(
            self._get_colors(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color',
                                                    line_color="#000000",
                                                    line_width=2)
        graph_renderer.edge_renderer.data_source.data = (
            self._get_edge_indexes())
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=self.pos)
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self):
        pass
        """colors = []
        for _ in range(len(self.graph.vertices)):
            color = '#'+''.join([choice('0123456789ABCDEF') for j in range(6)])
            colors.append(color)
        return colors"""

    def _get_colors(self):
        colors = []
        for i in range(len(self.graph.vertices)):
            colors.append(self.graph.vertices[str(i)].color)
        print(colors)
        return colors

    def _get_edge_indexes(self):
        start_indices = []
        end_indices = []
        checked = set()

        for index, vertex in self.graph.vertices.items():
            if vertex not in checked:
                for destination in vertex.edges:
                    start_indices.append(vertex.label)
                    end_indices.append(destination.label)
                checked.add(vertex)

        return dict(start=start_indices, end=end_indices)

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)

    def randomize(self):
        prev_vert = (0, 0)
        storage = set()
        counter = 0
        while len(storage) < len(self.graph.vertices):
            for vertex in self.graph.vertices:
                # TODO make bounds and random draws less hacky
                temp = (int(counter + random() * (self.width - 3)),
                        int(counter + random() * (self.height - 3)))
                counter += 1
                if temp and reversed(temp) not in storage:
                    if temp[0] and temp[1] not in storage:
                        if temp[0] + 3, 2, 1 > (prev_vert[0]):
                            if (temp[1] + 3) > (prev_vert[1]):
                                self.pos[vertex] = temp
                                prev_vert = temp
                                print(prev_vert)
                                storage.add(self.pos[vertex])

        print("storage", storage)

        """ while len(storage) < len(self.graph.vertices):
            for vertex in self.graph.vertices:
                # TODO make bounds and random draws less hacky
                temp = (counter + random() * (self.width - 2),
                        counter + random() * (self.height - 2))
                counter += 2
                if counter > 7:
                    counter -= 1.5
                print(counter)
                if temp not in storage:
                    self.pos[vertex] = temp
                    storage.append(self.pos[vertex])
        print("storage", storage[0])"""
# ############ More Hackey Stuff ###############
# #### working on implementation ###############
        """Randomize vertex positions."""
        """storage = set()
        storage = {}
        counter = 0
        numbers = (random(0, 30), random(0, 30))
        pairs = list(itertools.combinations(numbers, 2))
        print(pairs)"""
        """while counter < len(self.graph.vertices):
            r = (random.randint(0, 30), random.randint(0, 30))
            if r not in storage:
                counter += 1
                storage.add(r)
                self.pos[vertex] = r"""

    def _setup_labels(self):
        label_data = {'x': [], 'y': [], 'names': []}
        for vertex, edges in self.pos.items():
            label_data['x'].append(edges[0])
            label_data['y'].append(edges[1])
            label_data['names'].append(vertex)
        label_source = ColumnDataSource(label_data)
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                          text_align='center', text_baseline='middle',
                          source=label_source, render_mode='canvas',
                          text_color="white")
        self.plot.add_layout(labels)

# ########### Hackey bits ################
"""
for vertex in self.graph.vertices:
            # TODO make bounds and random draws less hacky
            self.pos[vertex] = (1 + random() * (self.width - 2),
                                1 + random() * (self.height - 2))
turn tuple to list
comp prev tuple to current tuple
append
counter
if statement


while l:
    for x, y in l:
        if x <= x + 1 or x - 1:
            print(x)
        else:
            l.pop(x)
            r.append(x)
            print(l)"""
