"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id %3)
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id / 10 * (self.id // 3)
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            colorString = '#'
            for i in range(0, 3):
                colorString += hexValues[random.randint(0, len(hexValues)-1)]
            self.color = colorString
        
        


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices={}):
        self.vertices = vertices
    def add_vertex(self, node):
        if isinstance(node, str):
            self.vertices[node] = Vertex(node)
        elif isinstance(node, list):
            for i in node:
                self.vertices[i] = Vertex(i)
    def add_edge(self, node, neighbor):
        if node not in self.vertices or neighbor not in self.vertices:
            raise Exception('Error: Vertex does not exist')
        elif self.vertices[node] != Vertex(node):
            self.vertices[node].edges.add(neighbor)
            self.vertices[neighbor].edges.add(node)
        else:
            self.vertices[node].edges.add(neighbor)
            self.vertices[neighbor].edges.add(node)

    def add_edges(self, edges):
        for i, j in edges:
            if self.vertices[i] != Vertex(i):
                self.vertices[i].add(j)
                self.vertices[j] = {i}
            else:
                self.vertices[i] = {j}
                self.vertices[j] = {i}

    def add_d_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].edges.add(end)
        else: 
            raise Exception('Error: Vertex does not exist')
            
    def bfs(adjList, node):
        frontier = []
        frontier.append(node)
        visited = []
        while len(frontier) > 0:
            n = frontier.pop()
            visited.append(n)
            print(n)
            for next_node in adjList[n]:
                frontier.append(next_node)

    def dft(adjList, node, visited):
        print(node)
        visited.append(node)
        for child_node in adjList[node]:
            if child_node not in visited:
                dft(adjList, child_node, visited)
