"""
Simple graph implementation compatible with BokehGraph class.
"""

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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {

        }
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        
    def add_edge(self, vert_1, vert_2):
        self.vertices[vert_1].add(vert_2)
        self.vertices[vert_2].add(vert_1)
    
    def bfs(self, node):
        visited = []
        queue = Queue()

        queue.enqueue(node)

        while queue.size() > 0:
            current_node = queue.dequeue()
            visited.append(current_node)
            for i in self.vertices[current_node]:
                if i not in visited:
                    queue.enqueue(i)
            return queue

    # def dfs(self, node):
    #     visited = []
    #     visited.push(node)
    #     for current_node in self.vertices[node]:
    #         if current_node not in visited:
    #             self.dfs(current_node)