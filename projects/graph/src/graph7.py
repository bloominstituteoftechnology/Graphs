class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size > 0:
            self.queue.pop(0)
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
        if self.size > 0:
            self.stack.pop()
        return None
    def size(self):
        return len(self.stack)

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()

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
            raise IndexError("That vertex does not exist!")
    def bft(self, start_node):
        visited = []
        q = Queue()
        q.enqueue(start_node)
        while q.size() > 0:
            node = q.dequeue()
            if node not in visited:
                print(node)
                visited.append(node)
                for child in self.vertices[node].edges:
                    q.enqueue(child)
    def dft(self, start_node):
        visited = []
        s = Stack()
        s.push(start_node)
        while s.size() > 0:
            node = s.pop()
            if node not in visited:
                print(node)
                visited.append(node)
                for child in self.vertices[node].edges:
                    s.append(child)
    def dft_r(self, start_node):
        visited = []
        print(start_node)
        visited.append(start_node)
        for child in self.vertices[start_node].edges:
            if child not in visited:
                self.dft_r(child)
    def bfs(self, start_node, target):
        visited = []
        q = Queue()
        q.append(start_node)
        while q.size() > 0:
            node = q.dequeue()
            if node not in visited:
                if node == target:
                    return True
                visited.append(node)
                for child in self.vertices[node].edges:
                    q.enqueue(child)
        return False
    def dfs(self, start_node, target):
        visited = []
        s = Stack()
        s.append(start_node)
        while q.size() > 0:
            node = s.pop()
            if node not in visited:
                if node == target:
                    return True
                visited.append(node)
                for child in self.vertices[node].edges:
                    s.append(child)

    def bfs_track(self, starting_node, destination_node):
        visited = []
        q = Queue()
        q.enqueue([starting_node])
        while q.size() > 0:
            print(q.queue)
            node_path = q.dequeue()
            v = node[-1]
            if v not in visited:
                if destination_node == v:
                    return node_path
                visited.append(v)
                for child in self.vertices[v].edges:
                    listN = list(node_path)
                    listN.append(child)
                    q.enqueue(listN)
        return None
    def dfs_track(self, starting_node, destination_node, visited = [], path = []):
        path = path + [starting_node]
        visited.append(starting_node)
        if destination_node == starting_node:
            return path
        for child in self.vertices[starting_node].edges:
            if child not in visited:
                new_path = dfs_track(child, destination_node, visited, path)
                if new_path:
                    return new_path
        return None





