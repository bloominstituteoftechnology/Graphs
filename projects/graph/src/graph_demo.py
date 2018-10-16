

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
    def __init__(self,value, x=None, y=None):
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
    def __init__(self, destination, weight = 0):
        self.destination = destination
        self.weight = weight 

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

    def add_edge_two_way(self, vertex1, vertex2):
        """
        This is a bidirectional method to the edges.
        """
       
        self.add_edge_one_way(vertex1, vertex2)
        self.add_edge_one_way(vertex2, vertex1)

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, color = "blue"):
        self.graph = graph #should be a object. instance of Graph
        self.color = color

    def show(self):
        N = len(self.graph.vertices) #length of vertices
        print(self.graph.vertices)
        vertex_indices = list(self.graph.vertices.keys())

        plot = figure(title="Random Generated Graph", x_range=(-7,7), y_range=(-7,7),
        tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(vertex_indices, 'index')
        

        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color= self.color)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=[vertex_indices[0]] * N,
            end= vertex_indices
        )
        d = dict(
            start=[vertex_indices[0]] * N,
            end=vertex_indices
        )
        print(d)
        
        x = []
        y = []

        for vertex_id in vertex_indices:
            vertex = self.graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(vertex_indices, zip(x,y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)
        output_file('random.html')
        show(plot)


def main():
    colors = ["blue", "red", "orange", "yellow"]
    color_index = round(random.random() * len(colors))-1
    random_color = colors[color_index]
    potential_labels = ["A", "B", "C", "D","E", "F", "G", "1", "2", "3", "4", "5", "6", "7"]
    random.shuffle(potential_labels) #to make it random we shuffle the labels. 
    random_number = random.randint(4,len(potential_labels))
    num_vertices = random_number
    num_edges = random_number
    graph = Graph()
    vertices_count = 0
    edges_count = 0

    while vertices_count <= num_vertices and edges_count <= num_edges:
        new_vertex = potential_labels[vertices_count]
        graph.add_vertex(new_vertex)
        if vertices_count > 0:
            graph.add_edge_two_way(new_vertex, previous_vertex)
            edges_count += 1
        previous_vertex = new_vertex
        vertices_count += 1
    bokeh_graph = BokehGraph(graph, random_color)
    bokeh_graph.show()
    


if __name__ == '__main__':
    # TODO - parse argv
    #I chose not to go with arguments since I am making everything i can think of completely random. 
    main()

