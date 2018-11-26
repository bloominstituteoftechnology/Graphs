

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
    """This is a vertex class that features the add edge and get edge methods to be added to vertices for the Graph class"""
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
    """This is a class to create edges/connections between to vertexs """
    def __init__(self, destination, weight = 0):
        self.destination = destination
        self.weight = weight 
    def __repr__(self):
        return f"{self.destination}<< destination. >>>{self.weight}"

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, value):
        """
        This method will use the Vertex class to create a instance and add it to vertices
        """
        new_vertex = Vertex(value)
        self.vertices[value] = new_vertex
        return new_vertex
        
        
    def add_edge_one_way(self, from_vertex, to_vertex):
        """
        this is a one way edge creator.  
        """
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].add_edge(to_vertex)
        else:
            raise IndexError("That vertex does not exist!")

    def add_edge_two_way(self, vertex1, vertex2):
        """
        This is a bidirectional method to the edges.
        it calls on the one way twice using the arguments passed in in all combinations
        """
       
        self.add_edge_one_way(vertex1, vertex2)
        self.add_edge_one_way(vertex2, vertex1)
    
    def breadth_first(self, start):
        """This is a breadth first traversal algorithm"""
        print(start)
        adj = self.vertices
        print(adj)
        print(adj.keys())
        print('\n\n')
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
        print("levels")
        print(level)
    """
    What helped me understand this concept was the following video 
    https://www.youtube.com/watch?v=s-CYnVz-uh4

    I understood the Lambda lecture however I think that the video broke the fact you are searching for 0 moves 
    0 moves is the starting point it takes zero moves to get there.  then 1 move  are its children exactly one vertex 
    from the starting point would be a child of the start.   then 2 moves 3 etc. 

    I think where I was confused out is the levels and how it doesn't appear smooth if you had to start where there is no
    no children. However you would flip flop the graph and while visually it has no children. 
    If you think about it in a zero move one move two move perspective now it does have children. 

    I don't know why i couldn't grasp this the first time maybe its just the way I learn but I think I get it now. 
    """
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
        #end of for loop
        visited(adj, start)
        print("\n\n\nParents")
        print(parent)
    #end of depth first

