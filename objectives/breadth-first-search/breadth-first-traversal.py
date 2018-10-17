

"""
In this module I will create a algorithm for breadth-first-traversal 
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
    
    def breadth_first(self, start):
        adj = self.vertices
        level = {start: 0}
        parent = {start : None}
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
        print(level)
