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
        self.vertices = {}

    def add_vertex(self, vertex_id):

            self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise IndexError("That vertex does not exist")
        else:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertext does not exist")

    def depth_first_search(self, starting_node):
        visited = []
        #create an empty stack
        s = Stack()
        #put starting vert in the stack
        s.push(starting_node)
        while s.size() > 0: #while stack is not empty
            destacked = s.pop() # Destack the first element
            visited.append(destacked) # Mark it as visited
            print(destacked, "destacked")
            for edge in self.vertices[destacked].edges: 
                if edge not in visited: # If it hasn't been visited
                    s.push(edge) # Add it to the back of the queue
        return visited

    def breadth_first_search(self, starting_node):
        visited = []
        #create and empty queue
        q = Queue()
        #put starting vert in the queue
        q.enqueue(starting_node)
        while q.size() > 0: # while queue is not empty
            dequeued = q.dequeue() # Dequeue the first element
            visited.append(dequeued) # Mark it as visited
            print(dequeued, "dequeued")
            for edge in self.vertices[dequeued].edges: #For each child
                if edge not in visited: # If it hasn't been visited
                    q.enqueue(edge) #Add it to the back of the queue
        return visited


class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
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


# graph = Graph()
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_vertex('5')
# graph.add_edge('0', '1')
# graph.add_edge('0', '2')
# graph.add_edge('0', '3')
# graph.add_edge('0', '4')
# graph.add_edge('0', '5')
# print(graph.verticies)