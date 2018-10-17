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
        if(self.size()) > 0:
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
        if(self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # dictionary

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()  # initializing a new set

    def add_edge(self, key, value):
        if key not in self.vertices:
            raise Exception(f"No {key} vertex")
        self.vertices[key].add(value)
        if value not in self.vertices:
            raise Exception(f"No {value} vertex")
        self.vertices[value].add(key)
        # self.vertices[key].add(value)

    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist")
        
    def dft(self, starting_node, visited=None):
        """
        Depth first traversal using recursion

        """

        if visited is None:
            visited = []
        visited.append(starting_node)

    def bft(self, starting_node):
        """
        Breath first traversal using a queue
        """

        q = Queue()

        q.enqueue(starting_node)
        visited = []
        while q.size() > 0:
    
    def dft_s(self, starting_node):
        """
        Depth first traversal using stack
        """

        s = Stack()

        s.push(starting_node)
        visited = []
        while s.size() > 0:
            

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


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    graph.add_vertex("0")
    graph.add_vertex("1")
    graph.add_vertex("2")
    graph.add_vertex("3")
    graph.add_edge("0", "1")
    graph.add_edge("0", "3")
    print(graph.vertices)
    # graph.add_edge("0", "4")
