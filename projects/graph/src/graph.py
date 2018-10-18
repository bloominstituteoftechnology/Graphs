"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

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
    #def random_edge(self):
    #    for v in range(0, len(self.vertices)):
    #        print(v)
    #        for i in range(v+1, len( self.vertices)):
    #            self.vertices[v].edges.add[i]
    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def dft(self, starting_node, visited=None):
        # Mark the node as visited
        if visited is None:
            visited = []
        visited.append(starting_node)
        for child in self.vertices[starting_node].edges:
            if child not in visited:
                self.dft(child, visited)
        print(visited)
        return visited
        # For each child, if that child hasn't been visited, call dft() on that node
        # for child in children:
        #    if child not in visited:
                  # dft(child, visted)
    def bft(self, starting_node):
        visited = []
        # create an empty queue
        q = Queue()
        # Put starting vert in the queue
        q.enqueue(starting_node)
        while q.size() > 0:
            dequeued = q.dequeue()
            visited.append(dequeued)
            for edge in self.vertices[dequeued].edges:
                if edge not in visited:
                    q.enqueue(edge)
                print(visited)
        return visited


            # Remove the first node from the queue...
            # If it has not been visited yet,...
            # Mark it as visited....
            # Then put all it's children in the back of the queue


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)  

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def place_stack(self, item):
        self.items.append(item)

    def unstack(self):
        return self.items.pop()

    def size(self):
        return len(self.items) 

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


