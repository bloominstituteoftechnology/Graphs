"""
Simple graph implementation
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
        return (len(self.queue))

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
        return (len(self.stack))


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")
    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue(starting_vertex_id)
        # While the queue is not empty....
        while q.size() > 0:
           # Dequeue the first node from the queue
           v = q.dequeue()
           # If that node has not been visted...
           if v not in visited:
              # Mark it as visited
              print(v)
              visited.add(v)
              # Then, put all of it's children into the queue
              for neighbor in self.vertices[v]:
                  q.enqueue(neighbor)

    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex_id)
        # While the stack is not empty....
        while s.size() > 0:
           # Pop the top node from the stack
           v = s.pop()
           # If that node has not been visted...
           if v not in visited:
              # Mark it as visited
              print(v)
              visited.add(v)
              # Then, put all of it's children into the stack
              for neighbor in self.vertices[v]:
                  s.push(neighbor)


    def dft_r(self, starting_vertex_id, visited=None):
        if visited is None:
            visited = set()
        # Mark the starting node as visited
        visited.add(starting_vertex_id)
        # Then call dft_r() on each unvisited neighbor
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_r(neighbor, visited)


    def bfs(self, starting_vertex_id, target_id):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the path to the starting vertex in our Queue
        q.enqueue( [starting_vertex_id] )
        # While the queue is not empty....
        while q.size() > 0:
           # Dequeue the first path from the queue
           path = q.dequeue()
           # Get the current node from the last element in the path
           v = path[-1]
           # If that node has not been visted...
           if v not in visited:
              # Mark it as visited
              visited.add(v)
              # Check if it's our target
              if v == target_id:
                  # If so, return the path to the target
                  return path
              # Then, put paths to all of it's children into the queue
              for neighbor in self.vertices[v]:
                  # Copy the path into a new instance
                  new_path = list(path)
                  # Append the neighbor to the end of the path
                  new_path.append(neighbor)
                  # Enqueue
                  q.enqueue(new_path)