#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
from random import random, randint

class Vertex:
    """Object representation of Vertex"""
    def __init__(self, label=None, coords=None, color='gray'):
        self.label = label
        self.coords = coords
        self.color = color
    
    def __repr__(self):
        return str(self.label)
    
    # def __hash__(self):
    #     return hash(str(self.label))
    
    # def __eq__(self, other):
    #     return self.label == str(other)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, num_of_vertices=0, chance=0.6):
        self.vertices = {}
        self.vertex_keys = []

        if num_of_vertices > 0:
            for i in range(num_of_vertices - 1):
                new_vertex = Vertex(i)
                self.add_vertex(new_vertex)
                self.vertex_keys.append(new_vertex)
        
            for edges in self.vertices.values():
                if random() <= chance:
                    p = randint(0,num_of_vertices - 1)
                    edges.add(self.vertex_keys[p])

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices."""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)
    
    def add_edge(self, start, end, bidirectional=True):
        """Add an edge (default bidirectional) between two vertices."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Vertices to connect not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

        

def main():
    graph = Graph()  # Instantiate your graph

    vl = [
        Vertex('0'),
        Vertex('1'),
        Vertex('2'),
        Vertex('3'),
    ]

    for v in vl:
        graph.add_vertex(v)

    graph.add_edge(vl[0], vl[1])
    graph.add_edge(vl[0], vl[3])
    print(graph.vertices)

if __name__ == '__main__':
    main()
