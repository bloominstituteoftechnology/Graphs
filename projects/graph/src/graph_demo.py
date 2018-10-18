"""
Demonstration of Graph and BokehGraph functionality.
"""
import random

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, LabelSet,
                          ColumnDataSource)


def random_color():
    """
    This is a random_color generator that will return a #color.
    """
    valid_chars = '0123456789ABCDEF'
    new_color = '#'
    while len(new_color) <= 6:
        new_color += valid_chars[random.randint(0, 15)]
    return new_color


class Vertex:
    """Vertex class featuring add edge get edge methods"""

    def __init__(self, value, x=None, y=None):
        """Setting up the Vertex class required value optional x y """
        self.value = value
        self.edges = set()

        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y

    def add_edge(self, vertex):
        """ will add an edge to the set of the vertex"""
        self.edges.add(vertex)

    def get_edges(self):
        """ will return the edges for the vertex"""
        return self.edges

    def __repr__(self):
        """ use the print method and this method will return the edges as a string"""
        return f"{self.edges}"


class Edge:
    """ this is the Edge class that shows connections between Vertex's"""

    def __init__(self, label, destination, weight=0, color=None):
        """Initailizing the Edge class label destination required weight and color are defaults"""
        self.label = label
        self.destination = destination  # edges
        self.weight = weight
        self.color = color

    def __repr__(self):
        """this will produce a string of the edge"""
        return f"Label: {self.label} Destinations: {self.destination} \
         Weight: {self.weight} Color: {self.color}"


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        """ initializing the graph class no parmaters needed
        vertices start off as a empty dictionary"""
        self.vertices = {}

    def add_vertex(self, value):
        """This method adds a vertex to the self.vertices"""
        new_vertex = Vertex(value)
        self.vertices[value] = new_vertex
        return new_vertex

    def add_edge_one_way(self, from_vertex, to_vertex):
        """ This is a one way edge it does accept and handle two way connections"""

        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].add_edge(to_vertex)
        else:
            raise IndexError("That vertex does not exist!")

    def add_edge_two_way(self, vertex1, vertex2):
        """
        This is a bidirectional method to the edges.
        """

        self.add_edge_one_way(vertex1, vertex2)
        self.add_edge_one_way(vertex2, vertex1)
    #

    def breadth_first(self, start):
        """This is a breadth first traversal algorithm"""
        adj = self.vertices
        level = {start: 0}
        parent = {start: None}
        index = 1
        frontier = [start]
        while frontier:
            nexts = []
            for item in frontier:
                for vertex in adj[item].edges:
                    if vertex not in level:
                        level[vertex] = index
                        parent[vertex] = item
                        nexts.append(vertex)

            frontier = nexts
            index += 1
        print("bfs levels")
        print(level)
    #

    def depth_first(self, start):
        """ This is a depth first traversal algorithm"""
        adj = self.vertices
        parent = {start: None}

        def visited(adj, start):
            """ this is a function used inside of depth_first that is recursive"""
            for vertex in adj[start].edges:
                if vertex not in parent:
                    parent[vertex] = start
                    visited(adj, vertex)
        # end of for loop
        visited(adj, start)
        print("Parents dfs")
        print(parent)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph):
        """ initialze the bokeh graph only requirement is a graph make use of the graph class"""
        self.graph = graph  # should be a object. instance of Graph

    def __repr__(self):
        """Will show what the graph looks like return self.graph"""
        return f"{self.graph}"

    def show(self):
        """ this method makes use of the bokeh package to produce a graph in html """
        vertex_indices = list(self.graph.vertices.keys())
        print(vertex_indices[0], "starting point for traversal")
        self.graph.depth_first(vertex_indices[0])
        self.graph.breadth_first(vertex_indices[0])

        plot = figure(title="Random Generated Graph", x_range=(-7, 7), y_range=(-7, 7),
                      tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(vertex_indices, 'index')

        x_coordinates = []
        y_coordinates = []

        disconnected_color = random_color()
        connected_color = random_color()

        colors_layout = []

        edge_start = []
        edge_end = []
        for vertex_id in vertex_indices:
            for vertices_edges in self.graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(vertices_edges)

        for vertex_id in vertex_indices:
            vertex = self.graph.vertices[vertex_id]
            x_coordinates.append(vertex.x)
            y_coordinates.append(vertex.y)
            if vertex_id in edge_start:
                colors_layout.append(connected_color)
            else:
                colors_layout.append(disconnected_color)


        graph_renderer.node_renderer.data_source.add(colors_layout, 'color')
        graph_renderer.node_renderer.glyph = Circle(
            radius=0.5, fill_color='color')

        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end
        )

        graph_layout = dict(
            zip(vertex_indices, zip(x_coordinates, y_coordinates)))
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        label_source = ColumnDataSource(data=dict(x=x_coordinates, y=y_coordinates, names=[
            self.graph.vertices[vertex_id].value for vertex_id in self.graph.vertices]))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', \
        text_align='center', text_baseline='middle', source=label_source, \
        render_mode='canvas', text_color='white')

        plot.add_layout(labels)

        output_file('random.html')
        show(plot)


def main():
    """This function will create parmaters neccessary for a random graph"""
    potential_labels = ["A", "B", "C", "D", "E",
                        "F", "G", "1", "2", "3", "4", "5", "6", "7"]
    # to make it random we shuffle the labels.
    random.shuffle(potential_labels)
    random_number = random.randint(4, len(potential_labels)-1)
    num_vertices = random_number
    num_edges = random_number//2
    graph = Graph()
    vertices_count = 0
    edges_count = 0
    vertices_created = []  # keep track of each creation.
    edge_track = {}
    while vertices_count <= num_vertices:
        new_vertex = potential_labels[vertices_count]

        graph.add_vertex(new_vertex)
        vertices_created.append(new_vertex)
        vertices_count += 1
    # shuffle the vertices_created so that the edges are randomly created
    random.shuffle(vertices_created)
    vertices_index_track = 0
    while edges_count <= num_edges and vertices_index_track + 1 < len(vertices_created):
        from_edge = vertices_created[vertices_index_track]  # starts off at 0.
        to_edge = vertices_created[vertices_index_track+1]
        if from_edge not in edge_track:
            edge_track[from_edge] = set()
            edge_track[from_edge].add(to_edge)
            graph.add_edge_two_way(from_edge, to_edge)
        else:
            edge_track[from_edge].add(to_edge)
            graph.add_edge_two_way(from_edge, to_edge)
        if to_edge not in edge_track:
            edge_track[to_edge] = set()
            edge_track[to_edge].add(from_edge)
            graph.add_edge_two_way(to_edge, from_edge)
        else:
            edge_track[to_edge].add(from_edge)
            graph.add_edge_two_way(to_edge, from_edge)

        edges_count += 1
        vertices_index_track += 1

    bokeh_graph = BokehGraph(graph)
    bokeh_graph.show()


if __name__ == '__main__':
    main()
