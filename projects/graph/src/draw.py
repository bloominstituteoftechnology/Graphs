"""
General drawing methods for graphs using Bokeh.
"""
from sys import argv
from random import choice, random, sample, randint
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)
from graph import Graph, Vertex

# Random Number Generators:
def RNG_vert():
    return randint(1, 20)
def RNG_edge():
    return randint(1, 10)

class BokehGraph:
    """
    Class that takes a graph and exposes drawing methods.
    """
    def __init__(self, graph, title='Graph', width=10, height=10,
                 show_axis=False, show_grid=False, circle_size=35,
                 draw_components=False):
        if not graph.vertices:
            raise Exception('Graph should contain vertices')
        self.graph = graph

        # Setup plot
        self.width = width
        self.height = height
        self.position = {} # dict to map vertices to x, y positions

        # make a canvas to draw on
        self.plot = figure(title=title, x_range=(0, width), y_range=(0, height))
        self.plot.axis.visible = show_axis
        self.plot.grid.visible = show_grid

        # render the vertice as a circle
        self._setup_graph_renderer(circle_size, draw_components)

        # render the labels
        self._setup_labels()

    def _setup_graph_renderer(self, circle_size, draw_components):
        # The renderer will have the actual logic for drawing
        graph_renderer = GraphRenderer()
        # Saving vertices in an arbitrary but persistent order
        self.vertex_keys = list(self.graph.vertices.keys())
        # Add the vertex data as instructions for drawing nodes
        graph_renderer.node_renderer.data_source.add(
            [vertex.label for vertex in self.vertex_keys], 'index')
        # Connected Components will be the same color
        # island components will be random colors
        colors = (self._color_connected_components() if draw_components
                  else self._RCG())
        graph_renderer.node_renderer.data_source.add(colors, 'color')
        # give the vertice shape
        graph_renderer.node_renderer.glyph = Circle(size=circle_size,
                                                    fill_color='color')
        # Add the edge [start, end] indices as instructions for drawing edges
        graph_renderer.edge_renderer.data_source.data = self._get_edge_indexes()
        # Randomize vertex coordinates, and set as layout
        self.randomize()
        # destructure this a little to squish a long line
        _layout = StaticLayoutProvider(graph_layout=self.position)
        graph_renderer.layout_provider = _layout
        # Attach the prepared renderer to the plot so it can be shown
        self.plot.renderers.append(graph_renderer)

    def _RCG(self, num_colors=None):
        """
        Random Color Generator
        """
        colors = []
        num_colors = num_colors or len(self.graph.vertices)
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
                    start_indices.append(vertex.label)
                    end_indices.append(destination.label)
                checked.add(vertex)
        return dict(start=start_indices, end=end_indices)

    def randomize(self):
        """
        Randomize Vertex Positions
        """
        for vertex in self.vertex_keys:
            self.position[vertex.label] = (1 + random() * (self.width - 2),
                                           1 + random() * (self.height - 2))
    
    def _setup_labels(self):
        label_data = {'x': [], 'y': [], 'names': []}
        for vertex, pos in self.position.items():
            label_data['x'].append(pos[0])
            label_data['y'].append(pos[1])
            label_data['names'].append(str(vertex))
        label_source = ColumnDataSource(label_data)
        labels = LabelSet(x='x', y='y', text='names', level='glyph',
                          text_align='center', text_baseline='middle',
                          source=label_source, render_mode='canvas')
        self.plot.add_layout(labels)

    def _color_connected_components(self):
        """
        Return same-color for vertices in connected components
        """
        self.graph.find_components()
        component_colors = self._RCG(self.graph.components)
        vertex_colors = []
        for vertex in self.vertex_keys:
            vertex_colors.append(component_colors[vertex.component])
        return vertex_colors

    def show(self, output_path='./graph.html'):
        output_file(output_path)
        show(self.plot)



# def main(num_vertices=8, num_edges=8, draw_components=True):
#     """
#     Connected Component Graph
#     """
#     graph = Graph()
#     # Add appropriate num of vertices
#     for num in range(num_vertices):
#         graph.add_vertex(Vertex(label=str(num)))
#     # Add random edges between vertices
#     for _ in range(num_edges):
#         vertices = sample(graph.vertices.keys(), 2)
#         # TODO check if edges already exists
#         graph.add_edge(vertices[0], vertices[1])
#     bokeh_graph = BokehGraph(graph, draw_components=draw_components)
#     bokeh_graph.show()

# if __name__ == '__main__':
#     if len(argv) == 4:
#         NUM_VERTICES = int(argv[1])
#         NUM_EDGES = int(argv[2])
#         DRAW_COMPONENTS = bool(int(argv[3]))
#         main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
#     else:
#         print('Expected arguments: num_vertices num_edges draw_components')
#         print('Both numbers should be integers, draw_components should be 0/1')


# def main(num_vertices=RNG_vert(), num_edges=RNG_edge()):
#     """
#     Random Graph
#     """
#     graph = Graph()
#     # Add appropriate num of vertices
#     for num in range(num_vertices):
#         graph.add_vertex(Vertex(str(num)))
#     # Add random edges between vertices
#     for _ in range(num_edges):
#         vertices = sample(graph.vertices.keys(), 2)
#         # TODO check if edges already exists
#         graph.add_edge(vertices[0], vertices[1])
#     bokeh_graph = BokehGraph(graph)
#     bokeh_graph.show()

# if __name__ == '__main__':
#     if len(argv) == 3:
#         NUM_VERTICES = int(argv[1])
#         NUM_EDGES = int(argv[2])
#         main(NUM_VERTICES, NUM_EDGES)
#     else:
#         main()


# def main():
#     """
#     BFS & DFS Graph
#     """
#     graph = Graph()

#     # v0 = Vertex(0)
#     # v1 = Vertex(1)
#     # v2 = Vertex(2)
#     # v3 = Vertex(3)

#     graph.add_vertex(0)
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)

#     graph.add_edge(0, 1)
#     graph.add_edge(0, 2)
#     graph.add_edge(1, 2)
#     graph.add_edge(2, 0)
#     graph.add_edge(2, 3)

#     print("\n")
#     print("The Graph: ", graph.vertices)
#     graph.BFS(0)
#     graph.DFS(3)
#     print("\n")

#     # bokeh_graph = BokehGraph(graph)
#     # bokeh_graph.show()

# if __name__ == '__main__':
#     main()
