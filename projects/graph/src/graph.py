"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color='yellow'):
        self.id = int(vertex_id)
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

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
       self.vertices = {}

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise Exception('Sorry!!! Vertices are not in the graph!!!')

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = Vertex(vertex_id)
        else:
            print('Provide vertex')

    def depth_first(self, start_vert, visited=[]):
        # Visited checks if we've visited the node before
        visited.append(start_vert)
        # Touch visited node
        print(self.vertices[start_vert].value)
        # Call DFS on each child (that has not been visited)
        for child_vert in self.vertices[start_vert].edges:
            # Check if child has been visited
            if child_vert not in visited:
                # If not, call DFS
                self.depth_first(child_vert)

    def breadth_first(self, start_vert_id):
        q = Queue()
        q.enqueue(start_vert_id)
        visited = []
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                print(self.vertices[v].value)
                visited.append(v)
                for next_vert in self.vertices[v].edges:
                    q.enqueue(next_vert)

    def randomize(self):
        num = random.random() * 15
        for i in range(int(num)):
            self.add_vertex(i)
        for vert1 in self.vertices:
            for vert2 in self.vertices:
                if vert1 is not vert2:
                    if random.random() > 0.8:
                        self.add_edge(vert1, vert2)


graph = Graph()
""" graph.add_vertex("0")
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_edge("0", "1")
graph.add_edge("0", "3")
print(graph.vertices)
 """