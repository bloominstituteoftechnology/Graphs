import random


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add an vertex to the graph
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
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def dft(self, starting_node=None, visited=None):
        print('starting node', starting_node)
        if visited is None:
            visited = []
        if starting_node is None: 
            verticies = list(self.vertices.keys())
            starting_node = verticies[0]
            print('first starting node', starting_node)
        visited.append(starting_node)
        
        for child in self.vertices[starting_node].edges:
            if child not in visited:
                  self.dft(child, visited)
    def bft(self):
        verticies = list(self.vertices.keys())
        q = [verticies[0]]
        print('first q', q)
        visited = []
        
        while len(q) > 0:
            nextQ = q.pop()
            if nextQ not in visited:
                visited.append(nextQ)
            q.extend(list(self.vertices[nextQ].edges))
            print('q', q)
            print('visited', visited)


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

