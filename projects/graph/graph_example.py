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
​
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
​
class Graph:
    def __init__(self): 
        self.vertices = {}
​
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()   # this will hold edges
​
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)   # there's an edge from v1 to v2
        else:
            raise IndexError("nonexistent vert")
​
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
​
    def bft(self, starting_vertex_id):
        # Create an empty queue
        q = Queue()
​
        # Create a set to store the visited nodes
        visited = set()
​
        # Init: enqueue the starting node
        q.enqueue(starting_vertex_id)
​
        # While the queue isn't empty
        while q.size() > 0:
            # Dequeue the first item
            v = q.dequeue()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)
​
                # Do something with the node
                print(f"Visited {v}")
​
                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
​
    def dft(self, starting_vertex_id):
        # Create an empty stack
        s = Stack()
​
        # Create a set to store the visited nodes
        visited = set()
​
        # Init: push the starting node
        s.push(starting_vertex_id)
​
        # While the stack isn't empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)
​
                # Do something with the node
                print(f"Visited {v}")
​
                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)
​
    def bfs(self, starting_vertex_id, target_vertex_id):
        pass
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
            # Dequeue the first PATH
            # Grab the last vertex from the PATH
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                  # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                  # COPY THE PATH
                  # APPEND THE NEIGHOR TO THE BACK
​
g = Graph()
​
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
​
g.add_edge('A', 'B')
g.add_edge('A', 'C')
​
g.add_edge('B', 'C')
g.add_edge('B', 'A')
g.add_edge('B', 'B')
​
g.add_edge('C', 'D')
g.add_edge('D', 'C')
​
g.bft('B')
g.dft('B')
