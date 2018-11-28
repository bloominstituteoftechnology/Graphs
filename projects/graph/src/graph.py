"""
Simple graph implementation compatible with BokehGraph class.
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

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("Vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def bft(self, starting_node):
        # Create an empty Queue
        q = Queue()
        # Create an empty visited list
        visited = set()
        # Add the start node to the queue
        q.enqueue(starting_node)
        print(starting_node)
        # While the Queue is not empty
        while q.size() > 0:
            # Remove the first node from the queue
            node = q.dequeue()
            for child in self.vertices[node].edges:
                if child not in visited:
                    visited.add(child)
                    print(child)
                    q.enqueue(child)

    def dft(self, starting_node):
        # Create an empty Stack
        s = Stack()
        # Create an empty visited list
        visited = set()
        # Add the start node to the Stack
        s.push(starting_node)
        print(starting_node)
        visited.add(starting_node)
        # While the Stack is not empty
        while s.size() > 0:
            # Remove the first node from the Stack
            node = s.pop()
            for child in self.vertices[node].edges:
                if child not in visited:
                    visited.add(child)
                    print(child)
                    s.push(child)

    def bfs(self, starting_node, target_node):
        # Create an array to hold visited nodes
        visited = []
        # Create an empty Queue
        q = Queue()
        q.enqueue(starting_node)
        while q.size() > 0:
            node = q.dequeue()
            visited.append(node)
            for edge in self.vertices[node].edges:
                if edge not in visited:
                    q.enqueue(edge)
        return False


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('3', '4')
graph.add_edge('1', '2')
graph.add_edge('3', '6')
graph.add_edge('6', '7')
graph.add_edge('4', '5')
graph.dft('0')
graph.bft('0')
graph.bfs('0', '5')
