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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            # directed edges are only 1 way
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex doesn't exist")
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            # undirected edges go both ways
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("vertex doesn't exist")
    def bft(self, starting_vertex):
        # create an empty queue
        q = Queue()
        # create an empty set of visited vertices
        visited = set()
        # put the starting vertex in our queue
        q.enqueue(starting_vertex)
        # while queue isn't empty
        while q.size() > 0:
           # dequeue first node from queue 
            v = q.dequeue()
            # if that node hasn't been visited
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # print node
                print(v)
                # put all of it's neighbors in the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
