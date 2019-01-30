"""
Simple graph implementation
"""

class Stack():

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


class Queue():

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


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
        else:
            raise IndexError("That vertex does not exist!")

    def bft(self, starting_node):
        q = Queue()
        visited = set()

        q.enqueue(starting_node)

        while q.size() > 0:
            node = q.dequeue()

            if node not in visited:
                print(node)
                visited.add(node)

                for next_node in self.vertices[node]:
                    q.enqueue(next_node)
      
    def dft(self, starting_node):
        s = Stack()
        visited = set()

        s.push(starting_node)

        while s.size() > 0:
            node = s.pop()

            if node not in visited:
                print(node)
                visited.add(node)

                for next_node in self.vertices[node]:
                    s.push(next_node)

    def bfs(self, starting_node, destination_node):
        
        queue = [(starting_node, [starting_node])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in graph[vertex] - set(path):
                if next == destination_node:
                    return path + [next]
                else:
                    queue.append((next, path + [next]))
