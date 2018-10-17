"""
Simple graph implementation compatible with BokehGraph class.
"""

import random

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].edges.add(vertex2)
            self.vertices[vertex2].edges.add(vertex1)
        else:
            raise IndexError("That vertex does not exist")

    # def dfs(self, starting_node, visited=None):
    #     if visited is None:
    #         visited = [False] * len(self.vertices)
    #     stack = [starting_node]
    #     results = []
    #     visited[starting_node] = True
    #     while stack:
    #         current_node = stack.pop()
    #         results.append(current_node)
    #         for next_node in self.vertices[current_node]:
    #             if visited[next_node] == False:
    #                 stack.append(next_node)
    #                 visited[next_node] = True
    #     return results

    #recursion
    def dfs(self, current, target, visited=None):
        if visited is None:
            visited = []
        visited.append(current)
        if current == target:
            return True
        for vertex in self.vertices[current]:
            if vertex not in visited:
                if self.dfs(vertex, target):
                    return True
        return False

    def bfs(self, current, target):
        q = Queue()
        q.enqueue(current)
        visited = []
        while q.size() > 0:
            if q.dequeue() == target:
                return True
            else:
                visited.append(q.dequeue())
        return False
        


    # def add_directed_edge(self, vertex1, vertex2):
    #     if vertex1 in self.vertices:
    #         self.vertices[vertex1].edges.add(vertex2)
    #     else:
    #         raise IndexError("That vertex does not exist")

class Vertex:
    def __init__(self, vertex_id, x = None, y = None):
        self.id = vertex_id
        self.edges = set()
        if x == None:
            self.x = random.random() * 10
        else:
            self.x = x
        if y == None:
            self.y = random.random() * 10
        else:
            self.y = y
    
    def __repr__(self):
        return f"{self.edges}"