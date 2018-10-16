

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
    #ability to add to the dict needed 
    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self.vertices[new_vertex] = set()
        return new_vertex
        
    def add_edge_one_way(self, from_vertex, to_vertex):
        new_edge = Edge(to_vertex)
        from_vertex.edges.add(new_edge)#using sets must use add() method 
        # 
        
        
        #self.graph_dict[from_vertex] = from_vertex.edges

        
        #add to the edges then we swap the edges that is there
        #out with self.edges though adding might be quicker.
        #not sure copy o(N)  but add is O(1)

        self.vertices[from_vertex].add(new_edge)
        #went with this out of being unsure of line 35
        #I know adding to the set is O(1) for sure though. 
        # A seperate edge case is needed for if to_vertex
        #links from_vertex   this method only handles 
        #one direction
    def add_edge_two_way(self, vertex1, vertex2):
        """
        This is a bidirectional method to the edges.
        """
        new_edge = Edge(vertex1)
        new_edge2 = Edge(vertex2)
        vertex1.edges.add(vertex2)
        vertex2.edges.add(vertex1)

class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph, color = "blue"):
        self.graph = graph #should be a object. instance of Graph
        self.color = color

    def show(self):
        N = len(self.graph.vertices.keys()) #length of vertices
        vertex_indices = list(self.graph.vertices.keys())

        plot = figure(title="Random Generated Graph", x_range=(-7,7), y_range=(-7,7),
        tools='', toolbar_location=None)

        graph_renderer = GraphRenderer()

        graph_renderer.node_renderer.data_source.add(vertex_indices, 'index')
        # node_colors = ["blue"] * N
        # graph.node_renderer.data_source.add(node_colors, 'color')

        graph_renderer.node_renderer.glyph = Circle(radius=0.5, fill_color= self.color)

        graph_renderer.edge_renderer.data_source.data = dict(
            start=[0]*N,
            end=vertex_indices
        )
        # circ =[i*2*math.pi/len(self.graph.vertices.keys()) for i in vertex_indices]
        # x = [math.cos(i) for i in circ]
        # y = [math.sin(i) for i in circ]
        x = []
        y = []
        for vertex_id in vertex_indices:
            vertex = self.graph.vertices[vertex_id]
            x.append(vertex.x)
            y.append(vertex.y)

        graph_layout = dict(zip(vertex_indices, zip(x,y)))
        graph_renderer.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

        plot.renderers.append(graph_renderer)
        output_file('graph.html')
        show(plot)

test = Graph()
vertex_one = test.add_vertex("0")
vertex_two = test.add_vertex("1")
vertex_three = test.add_vertex("2")
test.add_edge_two_way(vertex_one, vertex_two)
test.add_edge_two_way(vertex_two, vertex_three)
test_Bokeh = BokehGraph(test)

test_Bokeh.show()

def main():
    colors = ["blue", "red", "orange", "yellow"]
    random_color = colors[round(random.random() * len(colors))]
    potential_labels = ["A", "B", "C", "D","E", "F", "G", "1", "2", "3", "4", "5", "6", "7"]
    random.shuffle(potential_labels) #to make it random we shuffle the labels. 
    random_number = random.randint(4,len(potential_labels)+1)
    vertices_count = random_number
    num_edges = random_number
    graph = Graph()
    vertices_count = 0
    edges_count = 0
    while vertices_count < num_vertices and edges_count < num_edges:
        new_vertex = graph.add_vertex(potential_labels[vertices_count])
        vertices_count += 1
        if vertices_count > 0:
            graph.add_edge_two_way(new_vertex, previous_vertex)
            edges_count += 1
        previous_vertex = new_vertex
    bokeh_graph =(graph, random_color)
    bokeh_graph.show()
    


if __name__ == '__main__':
    # TODO - parse argv
    #I chose not to go with arguments since I am making everything i can think of completely random. 
    main()

