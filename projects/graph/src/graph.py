"""
Simple graph implementation compatible with BokehGraph class.
"""
import random


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, vertex):
        self.queue.append(vertex)
    def dequeue(self)
        if len(self.queue) > 0:
            self.queue.pop(0)

class Stack:
    def __init__(self):
        self.stack = []
    def append(self, vertex):
        self.stack.append(vertex)
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()
    

class Vertex:
    def __init__(self, v_id, x=None, y=None, value=None, color='white'):
        self.id = int(v_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.visited = False
        self.edges = set()
        if self.x is None:
            self.x = self.id
        if self.y is None:
            self.y = self.id
        if self.value is None:
            self.value = self.id


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, v_id):
        if v_id not in self.vertices:
            self.vertices[v_id] = Vertex(v_id)
        else:
            print('Please input a different vertex')
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            print("The edge could not be created")
    def randomize(self):
        num = random.random() * 10
        for i in range(int(num)):
            self.add_vertex(i)
        for vert in self.vertices:
            for otherVert in self.vertices:
                if vert is not otherVert:
                    if random.random() > .7:
                        self.add_edge(vert, otherVert)
    def dft:


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
print(graph.vertices)


# def DFT(adjList, node_id, visited):
#     visited.append(node_id)
#     for child_node in adjList[node_id]:
#         if child_node not in visited:
#             DFT(adjList, child_node, visited)
