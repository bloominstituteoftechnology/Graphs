"""
Simple graph implementation
"""


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None


class Stack:
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()
        else:
            return None


class Graph:
    """Represent a graph as a dictionary of
    vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vert, value):
        if vert in self.vertices and value in self.vertices:
            self.vertices[vert].add(value)
        else:
            print(f'{value} is not a vertex')

    def bft(self, starting_node):
        print('Breadth First Traversal')
        # Create a Queue
        q = Queue()
        visited = set()
        # Enqueue the starting node
        q.enqueue(starting_node)
        # While the queue is not empty
        while len(q.storage) > 0:
            # Dequeue a node from the queue
            node = q.dequeue()
            # Mark it as visited
            visited.add(node)
            print(node)
            # Enqueue all of its children that have not been visted
            for child in self.vertices[node]:
                if child not in visited and child not in q.storage:
                    q.enqueue(child)

        print('--------')

    def dft(self, starting_node):
        print('Depth First Traversal')
        # Create a Stack
        s = Stack()
        visited = set()
        # Push the starting node
        s.push(starting_node)
        # While the stack is not empty
        while len(s.storage) > 0:
            # Pop a node from the stack
            node = s.pop()
            # Mark it as visited
            visited.add(node)
            print(node)
            # Push all of its children that have not been visted
            for child in self.vertices[node]:
                if child not in visited and child not in s.storage:
                    s.push(child)

        print('--------')

    def dft_r(self, starting_node, visited=None):
        if visited is None:
            visited = set()
        # If the node has not been visited
        if starting_node not in visited:
            visited.add(starting_node)
            print(starting_node)
            # Mark the node as visted
            # Call dft_r on all children
            for child in self.vertices[starting_node]:
                if child not in visited:
                    self.dft_r(child, visited)

    def bfs(self, starting_node, target_node):
        q = Queue()
        visited = set()
        path = []
        q.enqueue(list(starting_node))

        while len(q.storage) > 0:
            node = q.dequeue()
            path = node
            vnode = node[-1]
            if vnode == target_node:
                return path
            visited.add(vnode)
            for child in self.vertices[vnode]:
                if child not in visited:
                    dup_node = node[:]
                    dup_node.append(child)
                    q.enqueue(dup_node)

        return False

    def dfs(self, starting_node, target_node):
        s = Stack()
        visited = set()
        path = []
        s.push(list(starting_node))

        while len(s.storage) > 0:
            node = s.pop()
            path = node
            vnode = node[-1]
            if vnode == target_node:
                return path
            visited.add(vnode)
            for child in self.vertices[vnode]:
                if child not in visited:
                    dup_node = node[:]
                    dup_node.append(child)
                    s.push(dup_node)

        return False
