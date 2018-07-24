"""
General drawing methods for graphs using Bokeh.
"""

import random
from random import choice, random, uniform
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, title='Graph', width=10, height=10, show_axis=False, show_grid=False, circle_size=35):
        if not graph.vertices:
            raise Exception('Graph must have vertices')
        self.graph = graph

        self.width = width
        self.height = height
        self.pos = {}
        self.plot = figure(title=title, x_range=(0,width), y_range=(0, height))

        self.xs = []
        self.ys = []
        self.vertex_labels = []
        self.source = ColumnDataSource(data=dict(xs=self.xs, ys=self.ys, vertex_labels=self.vertex_labels))


        self.labels = LabelSet(x='xs', y='ys', text='vertex_labels', source=self.source)


        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid
        self._setup_graph_renderer(circle_size)

    def _setup_graph_renderer(self, circle_size):
        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(list(self.graph.vertices.keys()), 'index')
        graph_renderer.node_renderer.data_source.add(self._get_random_colors(), 'color')
        graph_renderer.node_renderer.glyph = Circle(size=circle_size, fill_color='color')
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        self.randomize()
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=self.pos)
        self.plot.add_layout(self.labels)
        self.plot.renderers.append(graph_renderer)

    def _get_random_colors(self):
        
        # def get_random_color(pastel_factor = 0.5):
        #     return [(x+pastel_factor)/(1.0+pastel_factor) for x in [random.uniform(0,1.0) for i in [1,2,3]]]

        # def color_distance(c1,c2):
        #     return sum([abs(x[0]-x[1]) for x in zip(c1,c2)])

        # def generate_new_color(existing_colors,pastel_factor = 0.5):
        #     max_distance = None
        #     best_color = None
        #     for _ in range(0,100):
        #         color = get_random_color(pastel_factor = pastel_factor)
        #         if not existing_colors:
        #             return color
        #         best_distance = min([color_distance(color,c) for c in existing_colors])
        #         if not max_distance or best_distance > max_distance:
        #             max_distance = best_distance
        #             best_color = color
        #     return best_color

        colors = []
        
        for _ in range(len(self.graph.vertices)):
            # colors.append(generate_new_color(colors,pastel_factor = 0.9))
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
        print (self.pos)

    def randomize(self):
        """Randomize vertex positions."""
        for vertex in self.graph.vertices:
            randomx = 1 + random() * (self.width - 2)
            randomy = 1 + random() * (self.height - 2)
            self.pos[vertex] = (randomx, randomy)
            self.vertex_labels.append(vertex)
            self.xs.append(randomx)
            self.ys.append(randomy)

def main():
    from graph import Graph
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'D')
    graph.add_edge('C', 'B')
    graph.add_edge('C', 'A')

    bg = BokehGraph(graph)
    bg.show()

if __name__ == '__main__':
    main()