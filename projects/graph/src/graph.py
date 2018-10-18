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
        """
        Depth first traversal using recursion
        """
        # Mark the node as visited
        s = Stack()
        s.push(starting_node)
        if visited is None:
            visited = []
            visited.append(starting_node)
        while s
        # elif
        # For each child, if that child hasn't been visited, call dft() on that node
        # for child in children:
        #    if child not in visited:
        # dft(child, visted)

    def bft(self, starting_node):
        """
        Breadth first traversal using a queue
        """
        # create an empty queue
        print(f"STARTING NODE::::::{starting_node}")
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(starting_node)
        visited = []
        while q.size() > 0:
            rude_boy = q.dequeue()
            if rude_boy not in visited:
                visited.append(rude_boy)
                for edgy_kid in self.vertices[rude_boy].edges:
                    if edgy_kid not in visited:
                        q.enqueue(edgy_kid)
        return visited


    """
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
    """

    # Remove the first node from the queue...
    # If it has not been visited yet,...
    # Mark it as visited....
    # Then put all it's children in the back of the queue


class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        self.x = x
        self.y = y
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y
