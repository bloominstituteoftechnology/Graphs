"""
Demonstration of Graph and BokehGraph functionality.
"""
import random
from sys import argv
import math
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Circle, Oval, LabelSet,
                          ColumnDataSource)
from bokeh.palettes import Spectral8
from graph import Graph


class Vertex:
    def __init__(self, value, x=None, y=None):
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
        self.edges.add(vertex)

    def get_edges(self):
        return self.edges.keys()

    def __repr__(self):
        return f"{self.edges}"


class Edge:
    def __init__(self, label, destination, weight=0, color=None):
        self.label = label
        self.destination = destination  # edges
        self.weight = weight
        self.color = color


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self.vertices[value] = new_vertex
        return new_vertex

    def add_edge_one_way(self, from_vertex, to_vertex):

        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].add_edge(to_vertex)
        else:
            raise IndexError("That vertex does not exist!")

        new_edge = Edge(from_vertex, self.vertices[from_vertex].edges)

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
        i = 1
        frontier = [start]
        while frontier:
            next = []
            for u in frontier:
                for v in adj[u].edges:
                    if v not in level:
                        level[v] = i
                        parent[v] = u
                        next.append(v)

            frontier = next
            i += 1
        print("bfs levels")
        print(level)
    #

    def depth_first(self, start):
        """ This is a depth first traversal algorithm"""
        adj = self.vertices
        parent = {start: None}

        def visited(adj, start):
            """ this is a function used inside of depth_first that is recursive"""
            for v in adj[start].edges:
                if v not in parent:
                    parent[v] = start
                    visited(adj, v)
        # end of for loop
        visited(adj, start)
        print("\nParents dfs")
        print(parent)


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""

    def __init__(self, graph, color="blue"):
        self.graph = graph  # should be a object. instance of Graph
        self.color = color

    def show(self):

        N = len(self.graph.vertices)  # length of vertices
        vertex_indices = list(self.graph.vertices.keys())
        print(vertex_indices[0], "starting point")
        self.graph.depth_first(vertex_indices[0])
        self.graph.breadth_first(vertex_indices[0])

        plot = figure(title="Random Generated Graph", x_range=(-7, 7), y_range=(-7, 7),
                      tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(vertex_indices, 'index')

        x = []
        y = []
        valid_chars = '0123456789ABCDEF'

        disconnected_color = f"#{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}"
        connected_color = f"#{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}"

        colors_layout = []

        edge_start = []
        edge_end = []
        for vertex_id in vertex_indices:
            for v in self.graph.vertices[vertex_id].edges:
                edge_start.append(vertex_id)
                edge_end.append(v)

        for vertex_id in vertex_indices:
            vertex = self.graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)
            if vertex_id in edge_start:
                colors_layout.append(connected_color)
            else:
                colors_layout.append(disconnected_color)

        # graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color= self.color)
        graph_renderer.node_renderer.data_source.add(colors_layout, 'color')
        graph_renderer.node_renderer.glyph = Circle(
            radius=0.5, fill_color='color')

        graph_renderer.edge_renderer.data_source.data = dict(
            start=edge_start,
            end=edge_end
        )

        graph_layout = dict(zip(vertex_indices, zip(x, y)))
        graph_renderer.layout_provider = StaticLayoutProvider(
            graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)

        labelSource = ColumnDataSource(data=dict(x=x, y=y, names=[
                                       self.graph.vertices[vertex_id].value for vertex_id in self.graph.vertices]))
        labels = LabelSet(x='x', y='y', text='names', level='glyph', text_align='center',
                          text_baseline='middle', source=labelSource, render_mode='canvas')

        plot.add_layout(labels)

        output_file('random.html')
        show(plot)


def main():
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
    edges_created = []  # keep track avoid duplicates.
    edge_track = {}
    while vertices_count <= num_vertices:
        try:
            new_vertex = potential_labels[vertices_count]
        except:
            print(vertices_count)
            print(len(potential_labels))
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

    valid_chars = '0123456789ABCDEF'
    random_color = f"#{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}{valid_chars[random.randint(0,15)]}"
    bokeh_graph = BokehGraph(graph, random_color)
    bokeh_graph.show()


if __name__ == '__main__':
    # TODO - parse argv
    # I chose not to go with arguments since I am making everything i can think of completely random.
    main()
