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
    def dftc(self, starting_vertex_id):
        visited =[]
        visited.append(starting_vertex_id)
        def helpers(index_id):
            for neighbor in self.vertices[index_id]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    print(visited)
                    helpers(neighbor)
        helpers(starting_vertex_id)
        print (visited)
    
    def bfs(self, starting_vertex, search_vertex):
        # Create an empty queue
        q = Queue()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Queue
        q.enqueue([starting_vertex])
        # While the queue is not empty....
        while q.size() > 0:
           path=q.dequeue()
           # Dequeue the first node from the queue
           v = path[-1]
           # If that node has not been visted...
           if v not in visited:
              # Mark it as visited
              visited.add(v)
              if v == search_vertex:
                  return path
              # Then, put all of it's children into the queue
              for neighbor in self.vertices[v]:
                  new_path=list(path)
                  new_path.append(neighbor)
                  q.enqueue(new_path)
    def dfs(self, starting_vertex, search_vertex):
        # Create an empty stack
        s = Stack()
        # Create an empty set of visited vertices
        visited = set()
        # Put the starting vertex in our Stack
        s.push(starting_vertex)
        # While the stack is not empty....
        while s.size() > 0:
           # Pop the top node from the stack
           v = s.pop()
           # If that node has not been visted...
           if v==search_vertex:
               print(v)
               break
           if v not in visited:
              # Mark it as visited
              print(v)
              visited.add(v)
              # Then, put all of it's children into the stack
              for neighbor in self.vertices[v]:
                  s.push(neighbor)
    
graph = Graph()  # Instantiate your graph
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('7')
graph.add_directed_edge('5', '3')
graph.add_directed_edge('6', '3')
graph.add_directed_edge('7', '1')
graph.add_directed_edge('4', '7')
graph.add_directed_edge('1', '2')
graph.add_directed_edge('7', '6')
graph.add_directed_edge('2', '4')
graph.add_directed_edge('3', '5')
graph.add_directed_edge('2', '3')
graph.add_directed_edge('4', '6')
# print(graph.vertices)


print(graph.bfs('1','6'))
