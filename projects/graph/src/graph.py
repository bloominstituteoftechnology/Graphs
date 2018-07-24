#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    """Object representation of Vertex"""
    def __init__(self, label=None):
        self.label = label
    
    def __repr__(self):
        return str(self.label)
    
    def __hash__(self):
        return hash(str(self.label))
    
    def __eq__(self, other):
        return self.label == str(other)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
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

    graph.add_vertex(Vertex('0'))
    graph.add_vertex(Vertex('1'))
    graph.add_vertex(Vertex('2'))
    graph.add_vertex(Vertex('3'))
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

if __name__ == '__main__':
    main()
