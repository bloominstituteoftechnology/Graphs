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
    
    def bft(self, start):
        print('BFT')
        if start in self.vertices:
            nextItems = Queue()
            visited = []
            nextItems.put(start)
            while nextItems.empty() is not True:
                first = nextItems.get()
                if first not in visited:
                    visited.append(first)
                    print(first)
                    for num in self.vertices[first]:
                        nextItems.put(num)
                
    
    def dft(self, start):
        print('DFT')
        if start in self.vertices:
            nextItems = []
            visited = []
            nextItems.append(start)
            while len(nextItems) != 0:
                first = nextItems.pop()
                if first not in visited:
                    visited.append(first)
                    print(first)
                    for num in self.vertices[first]:
                        nextItems.append(num)
        print('-----------')

    def dft_recursion(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for num in self.vertices[start]:
            if num not in visited:
                self.dft_recursion(num, visited)

    def bft_path(self, start, target):
        if start in self.vertices:
            nextItems = Queue()
            visited = []
            path = []
            nextItems.put([start])
            while nextItems.empty() is not True:
                print('Visited', visited)
                print('Path', path)
                first = nextItems.get()
                print('First', first)
                
                if first not in visited:
                    path.append(first[-1])
                    if first[-1] == target:
                        path = first
                        return path
                    visited.append(first[-1])
                    for num in self.vertices[first[-1]]:
                        tempPath = path + [num]
                        print(tempPath)
                        nextItems.put(tempPath)
        else:
            return None
        ## Create a store for the path
        ## If first is in the path 

class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()