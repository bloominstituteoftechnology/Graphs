"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

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
        """
        Create the empty graph
        """
        self.vertices = {}
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
            raise IndexError("That vertex does not exist")
            
    
    def bft_queue(self, starting_node):
        q = Queue()
        q.enqueue(starting_node)
        visited = []
        while q.size() > 0:
            current = q.dequeue()
            if current not in visited:
                visited.append(current)
                print(visited)
                self.vertices[current].color = 'red'
                for edge in self.vertices[current].edges:
                    q.enqueue(edge)

    
    def dft_stack(self, starting_node):
         # create an empty stack
        s = Stack()
        # Put starting vert in the stack
        s.push(starting_node)
        visited = []
        while s.size() > 0:
             # Pop the first node off the stack...
            # If it has not been visited yet,...
            # Mark it as visited....
            # Then put all it's children on top of the stack
            current = s.pop()
            if current not in visited:
                visited.append(current)
                print(visited)
                for edge in self.vertices[current].edges:
                    s.push(edge)


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