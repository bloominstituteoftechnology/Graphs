"""
Simple graph implementation
"""
from queue import Queue



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()
    
    def add_vertex(self, label):
        newVertex = Vertex(label)
        self.vertices[newVertex.label] = newVertex.edges

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
    
    def bft(self, start):
        if start in self.vertices:
            nextItems = Queue()
            visited = []
            nextItems.put(start)
            while nextItems.empty() is not True:
                first = nextItems.queue[0]
                for num in self.vertices[first]:
                    if num not in visited:
                        nextItems.put(num)
                nextItems.get()
                visited.append(first)
            print(visited)

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()