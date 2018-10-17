import random

# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self, value):
#         if (self.size()) > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

# class Stack:
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.push(value)
#     def pop(self):
#         if (self.size()) > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

class Graph:
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {} # dictionary
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph
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
            raise IndexError("That vertex does not exists!") # Stretch goal - ensures that edges to nonexistent vertices are rejected
    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exists!") # Stretch goal - ensures that edges to nonexistent vertices are rejected
    
    def bfs(self, starting_node):
        queue = [starting_node]
        visited = [starting_node]
        while len(queue) > 0:
            cur_node = queue.pop(0)
            for edge in self.vertices[cur_node].edges:
                if edge not in visited:
                    visited.append(edge)
                    queue.append(edge)
        return visited

class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """
        Create an empty vertex
        """
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        if y is None:
            self.y = random.random() * 10 - 5 

    def __repr__(self):
        return f"{self.edges}"