#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
class Vertex:
    """Represent a vertex with a label and possible connected component."""
    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component

    def __repr__(self):
        return 'Vertex: ' + self.label
        
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, start, end, bidirectional=True):
        self.vertices[start].add(end)

        if bidirectional:
            self.vertices[end].add(start)

    

def main():
    graph = Graph()  
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('2', '3', False)
    graph.add_edge('2', '1')    
    print(graph.vertices)
    print(graph.BFS('3'))

if __name__ == '__main__':
    main()