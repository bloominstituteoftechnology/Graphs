class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) > 0:
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
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vert, value):
        if vert in self.vertices and value in self.vertices:
            self.vertices[vert].add(value)
            self.vertices[value].add(vert)
        else:
            IndexError()

    def bft(self, start_node):
        queue = Queue()
        visited = set()
        queue.enqueue(start_node)

        while queue.size > 0:
            node = queue.dequeue()
            if node not in visited:
                print("not visited:", node)
                visited.add(node)
                for next in self.vertices[node]:
                    queue.enqueue(next)

    def dft(self, start_node):
        stack = Stack()
        visited = set()
        stack.push(start_node)
        while stack.size() > 0:
            node = stack.pop()
            if node not in visited:
                print("not visited:", node)
                visited.add(node)
                for next in self.vertices[node]:
                    stack.push(next)

    


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
