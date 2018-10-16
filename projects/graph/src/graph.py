import random
import collections

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """
        Create an empty vertex
        """
        self.id = vertex_id
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


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertext to the graph
        """
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertext does not exist!")

    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertext does not exist!")

    def dfs(self, starting_vertex, visited = None):
        """
        Mark vertex as visited
        """
        if visited is None:
            visited = []
        visited.append(starting_vertex)
        """
        For each child, if that child hasn't been visited, call dft() on that vertex
        """
        for child in self.vertices[starting_vertex].edges:
            if child not in visited:
                self.dfs(child, visited)
        return visited

    def bfs(self, starting_node):
        visited, queue = set(), collections.deque([starting_node])
        while queue:
            print(queue)
            vertex = queue.popleft()
            for neighbor in self.vertices[vertex].edges:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited
                
            
