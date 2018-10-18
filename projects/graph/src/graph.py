"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
           self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise IndexError("That vertex does not exist")
        else:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def depth_first_search(self, starting_node):
        stack = Stack()
        stack.push(starting_node)
        visited = []
        while stack.size() > 0:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
                print(visited)
                for edge in self.vertices[current].edges:
                    stack.push(edge)

    def breadth_first_search(self, starting_node):
        queue = [starting_node]
        collected = []
        if len(self.vertices) == 0:
            visited == False
        while queue:
            current = queue.pop(0)
            collected.append(current)
            for child in self.vertices[current]:
                if visited[child] == False:
                    queue.append(child)
                    visited[child] == True

class Vertex:
    def __init__(self, vertex, x=None, y=None):
        self.id = vertex
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

        
#thegraph = Graph()
#thegraph.add_vertex('0')
#thegraph.add_vertex('1')
#thegraph.add_vertex('2')
#thegraph.add_vertex('3')
#thegraph.add_edge('0', '1')
#thegraph.add_edge('0', '3')
#print(thegraph.vertices)