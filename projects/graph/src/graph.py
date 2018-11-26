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


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

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
    def dft(self, starting_node, visited=None):        
        if visited is None:            
            visited = []
        visited.append(starting_node)  
        print(starting_node)      
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                self.dft(node, visited)
        return visited
    def bft(self, starting_node):
        visited = []
        q = Queue()
        q.enqueue(starting_node)
        while q.size() > 0:  
            dequeued = q.dequeue() 
            visited.append(dequeued)  
            print(dequeued)
            for edge in self.vertices[dequeued].edges: 
                if edge not in visited:  
                    q.enqueue(edge) 
        return visited


class Vertex:
    def __init__(self, vertex_id, x = None, y = None):
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
