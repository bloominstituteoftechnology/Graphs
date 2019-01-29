"""
Simple graph implementation
"""

class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)
    
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else: 
            return None

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else: 
            return None



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {
        }

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist.')

    def bft(self, start_node):
        queue = Queue()
        visited = set()
        queue.enqueue(start_node)
        while queue.size() > 0:
            node = queue.dequeue()
            if node not in visited:
                print(node)
                visited.add(node)
            for next_node in self.vertices[node]:
                queue.enqueue(next_node)

    def dft(self, start_node):
        stack = Stack()
        visited = set()
        stack.push(start_node)
        while stack.size() > 0:
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
            for next_node in self.vertices[node]:
                stack.push(next_node)

    def dft_r(self, start_node, visited = None):
        if visited == None:
            visited = set()
        visited.add(start_node)
        print(start_node)
        for child_node in self.vertices[start_node]:
            if child_node not in visited:
                self.dft_r(child_node, visited)

    def bfs(self, start_node, target_node):
        queue = Queue()
        visited = set()
        queue.enqueue(start_node)
        while queue.size() > 0:
            node = queue.dequeue()
            if node not in visited:
                if node == target_node:
                    return True
                print(node)
                visited.add(node)
            for next_node in self.vertices[node]:
                queue.enqueue(next_node)
        return False
    
    # modify to return a path of search

    def dfs(self, start_node, target_node):
        stack = Stack()
        visited = set()
        stack.push(start_node)
        while stack.size() > 0:
            node = stack.pop()
            if node not in visited:
                if node == target_node:
                    return True
                print(node)
                visited.add(node)
            for next_node in self.vertices[node]:
                stack.push(next_node)
        return False

    def bfs_path(self, start_node, target_node):
        queue = Queue()
        visited = set()
        queue.enqueue([start_node])
        while queue.size() > 0:
            path = queue.dequeue()
            node = path[-1]
            if node not in visited:
                visited.add(node)
                if node == target_node:
                    return path
            for next_node in self.vertices[node]:
                dupl_path = list(path)
                dupl_path.append(next_node)
                queue.enqueue(dupl_path)
            
        return None
    
    # modify ^ to return a path of search