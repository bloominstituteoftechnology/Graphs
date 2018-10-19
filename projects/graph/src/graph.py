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
    def __init__(self):
        self.vertices = dict()
        self.components = 0

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].edges.add(vertex2)
            self.vertices[vertex2].edges.add(vertex1)
        else:
            raise IndexError("That vertex does not exist")

    # def dft(self, current, visited=None):
    #     if visited is None:
    #         visited = []
    #     stack = [current]
    #     while stack:
    #         current_node = stack.pop()
    #         visited.append(current_node)
    #         print(visited)
    #         for next_node in self.vertices[current_node].edges:
    #             if next_node not in visited:
    #                 stack.append(next_node)
    #     return visited

    # recursion
    def dft(self, current, visited=None):
        if visited is None:
            visited = []
        visited.append(current)
        for vertex in self.vertices[current].edges:
            if vertex not in visited:
                self.dft(vertex, visited)
        return visited

    def dfs(self, current, target, visited=None):
        connected = []
        if visited is None:
            visited = []
        visited.append(current)
        if connected == []:
            connected.append([current])
        if current == target:
            return visited
        for vertex in self.vertices[current].edges:
            if vertex not in visited:
                if self.dfs(vertex, target, visited):
                    return connected
        print(connected)

    def bft(self, current):
        visited = []
        random_color = '#'+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
        q = Queue()
        self.vertices[current].color = random_color
        q.enqueue(current)
        while q.size() > 0:  
            dequeued = q.dequeue()
            visited.append(dequeued)
            for edge in self.vertices[dequeued].edges: 
                if edge in visited:
                    self.vertices[dequeued].color = self.vertices[current].color
                if edge not in visited: 
                    self.vertices[dequeued].color = random_color
                    q.enqueue(edge)
        return visited

    def find_connected(self):
        visited = []
        cc = []
        for vertex in self.vertices:
            if vertex not in visited:
                connected = self.bft(vertex)
                cc.append(connected)
                visited.extend(connected)
        return cc
        
    # def bfs(self, current, target, visited=None):
    #     q = Queue()
    #     if visited is None:
    #         visited = []
    #     q.enqueue(current)
    #     if current == target:
    #         return True
    #     visited[current] = True
    #     while q.size() > 0:
    #         node = q.dequeue()
    #         if node not in visited:
    #             visited.append(node)
    #             edges = node.edges
    #             for edge in edges:
    #                 q.enqueue(self.vertices[edge])
    #     return visited

    # def add_directed_edge(self, vertex1, vertex2):
    #     if vertex1 in self.vertices:
    #         self.vertices[vertex1].edges.add(vertex2)
    #     else:
    #         raise IndexError("That vertex does not exist")

class Vertex:
    def __init__(self, vertex_id, x = None, y = None):
        self.id = vertex_id
        self.edges = set()
        self.color = None
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