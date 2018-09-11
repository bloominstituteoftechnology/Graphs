"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices=4, edges=6, directed=False, probability = None):
        self.vertices = {}
        self.N = vertices
        self.edges = edges
        self.directed = directed
        self.edge_prob = probability

    def add_vertex(self, label):
        #check if an object with label already exists
        if label in self.vertices:
            raise ValueError(f"Duplicate vertex '{label}' found")
        #create new vertex object with the label passed to function
        self.vertices[label] = set()

    def add_directed_edge(self, start, end):
        if start not in self.vertices:
            raise ValueError(f"Vertex '{start}' not found")
        if end not in self.vertices:
            raise ValueError(f"Vertex '{end}' not found")
        self.vertices[start].add(end)

    def add_undirected_edge(self, start, end):
        if start not in self.vertices:
            raise ValueError(f"Vertex '{start}' not found")
        if end not in self.vertices:
            raise ValueError(f"Vertex '{end}' not found")
        if self.vertices[start] == end or self.vertices[end] == start:
            print('Edge already exists.')
            return
        self.vertices[start].add(end)
        self.vertices[end].add(start)

    def generate_vertices(self):
        for i in range(self.N):
            label = 'v'+ str(i)
            self.add_vertex(label)
    
    def generate_edges(self):
        count = 0
        vertices = list(self.vertices.keys())

        for v in vertices:
            for k in [i for i in vertices if i != v]:
                chance = random.random()
                if chance < 0.5:
                    self.add_undirected_edge(v, k)
                    count+=2
                    if(count==self.edges):
                        return