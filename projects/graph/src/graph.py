"""
Simple graph implementation compatible with BokehGraph class.
"""

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

class Vertex:
    def __init__(self, value):
        self.node = value
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            vertex = Vertex(value)
            self.vertices[vertex.node] = vertex.edges
            return True
        else:
            return False

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
            return True
        else:
            if v1 not in self.vertices:
                raise IndexError(
                    f"Vertex {v1} is nonexistent!"
                )  # IndexError more specific than Exception
            elif v2 not in self.vertices:
                raise IndexError(f"Vertex {v2} is nonexistent!")
    
    def bft(self, starting_node):
        # Create an empty Queue
        q = Queue()
        # Create an empty visited list
        visited = set()
        # Add the start node to the queue
        q.enqueue(starting_node)
        # While the Queue is not empty...
        while q.size() > 0:
            # Remove the first node from the Queue
            node = q.dequeue()
            # If it hasn't been visited
            if node not in visited:
                # Mark it as visited
                print(node)
                visited.add(node)
                # Then put all its children in the queue
                for child in self.vertices[node].edges:
                    q.enqueue(child)

    def dft(self, starting_node):
        # Create an empty Stack
        s = Stack()
        # Create an empty visited list
        visited = set()
        # Add the start node to the stack
        s.push(starting_node)
        # While the Stack is not empty...
        while s.size() > 0:
            # Remove the first node from the Stack
            node = s.pop()
            # If it hasn't been visited
            if node not in visited:
                # Mark it as visited
                print(node)
                visited.add(node)
                # Then put all its children in the queue
                for child in self.vertices[node].edges:
                    s.push(child)



graph = Graph()
graph.add_vertex("0")
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_edge("0", "1")
graph.add_edge("0", "3")
graph.add_edge("0", "4")
print(graph.vertices)