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


class Vertex:
    def __init__(self, value):
        self.value = value
        self.color = "white"
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def add_edge(self, vert, value):
        if vert in self.vertices and value in self.vertices:
            self.vertices[vert].edges.add(value)
        else:
            IndexError()

    def add_bidirectional_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("Vertex does not exist")

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

    def dft_recursion(self, start_node, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_node)
        for child in self.vertices[start_node]:
            if child not in visited:
                self.dft_recursion(child, visited)

    def bfs(self, start_node, destination_node):
        queue = Queue()
        visited = set()
        start_path = [start_node]

        queue.enqueue(start_path)

        while queue.size() > 0:
            dequeue_path = queue.dequeue()
            dequeue_node = dequeue_path[-1]

            if dequeue_node not in visited:
                if dequeue_node == destination_node:
                    return dequeue_path

                visited.add(dequeue_node)

                for child in self.vertices[dequeue_node].edges:
                    copied_path = list(dequeue_path)
                    copied_path.append(child)
                    queue.enqueue(copied_path)

        return None


    def dfs(self, start_node, destination_node):
        stack = Stack()
        visited = set()
        start_path = [start_node]

        stack.push(start_path)

        while stack.size() > 0:
            dequeue_path = stack.pop()
            dequeue_node = dequeue_path[-1]

            if dequeue_node not in visited:
                if dequeue_node == destination_node:
                    return dequeue_path

                visited.add(dequeue_node)

                for child in self.vertices[dequeue_node].edges:
                    copied_path = list(dequeue_path)
                    copied_path.append(child)
                    stack.push(copied_path)

        return None