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
        if vert_1 in self.vertices and vert_2 in self.vertices:
            self.vertices[vert_1].add(vert_2)
            self.vertices[vert_1].add(vert_2)
        else:
            raise Exception("No existing vertix")

            
    def bfs(self, node):
        visited = []
        queue = Queue()

        queue.enqueue(node)

        while queue.size() > 0:
            current_node = queue.dequeue()
            if current_node not in visited:
                visited.append(current_node)
                print(f"Visited: {current_node}")
                for i in self.vertices[current_node]:
                    queue.enqueue(i)

    def bfs_search(self, node, target_node):
        visited = []
        queue = Queue()

        queue.enqueue(node)

        while queue.size() > 0:
            current_node = queue.dequeue()
            if current_node not in visited:
                visited.append(current_node)
                if current_node == target_node:
                    return True
                print(f"Visited: {current_node}")
                for i in self.vertices[current_node]:
                    queue.enqueue(i)
      

    def dfs_search(self, node, target_node):
        visited = []
        stack = [node]
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node not in visited:
                if current_node == target_node:
                    return True
                visited.append(current_node)
                for edge in self.vertices[current_node]:
                    stack.append(edge)
        print(visited)