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
            self.y = 2 * (self.id % 3) + self.id / 5 * (self.id // 3)
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            colorString = '#'
            for i in range(0, 3):
                colorString += hexValues[random.randint(0, len(hexValues)-1)]
            self.color = colorString
        
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        return self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else: None
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        return self.stack.append(value)
    def pop(self):
        if self.size > 0:
            return self.stack.pop()
        else: None
    def size(self):
        return len(self.stack)
        


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices={}):
        self.vertices = vertices
    def add_vertex(self, node):
        if isinstance(node, str):
            self.vertices[node] = Vertex(node)
        elif isinstance(node, int):
            self.vertices[node] = Vertex(node)
        elif isinstance(node, list):
            for i in node:
                self.vertices[i] = Vertex(i)
    def add_edge(self, node, neighbor):
        if node not in self.vertices or neighbor not in self.vertices:
            raise Exception('Error: Vertex does not exist')
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
            
    def bft(self, node):
        q = Queue()
        q.enqueue(node)
        visited = []
        while q.size() > 0:
            n = q.dequeue()
            if n not in visited:
                print(n)
                visited.append(n)
                for next_node in self.vertices[n].edges:
                    q.enqueue(next_node)
        

    def dft(self, node, visited=[]):
        print(node)
        visited.append(node)
        for child_node in self.vertices[node].edges:
            if child_node not in visited:
                self.dft(child_node, visited)


    def dfs(self, start_vert, target_value, visited=[]):
        visited.append(start_vert)
        print(self.vertices[start_vert].value)
        if self.vertices[start_vert].value == target_value:
            print(True)
            return True
        for child_vert in self.vertices[start_vert].edges:
            if child_vert not in visited:
                self.dfs(child_vert, target_value)
        print(False) 
        return False


    def bfs(self, start_vert, target_value):
        q = Queue()
        q.enqueue(start_vert)
        visited = []
        while q.size() > 0:
            n = q.dequeue()
            if n == target_value:
                print(True)
                return True
            visited.append(n)
            
            for next_node in self.vertices[n].edges:
                q.enqueue(next_node)
        print(False)
        return False