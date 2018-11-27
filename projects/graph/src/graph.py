"""
Simple graph implementation compatible with BokehGraph class.
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def enqueue(self, value):
        # add to tail
        self.storage.append(value)
        self.size += 1

    def dequeue(self):
        # remove from head
        if self.size:
            self.size -= 1
            return self.storage.pop(0)

    def len(self):
        return self.size

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # store vertices in dictionary
        self.vertices = {}

    # add a vertex
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    # add a bidirectional edge 
    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].edges.add(to_vertex)
            self.vertices[to_vertex].edges.add(from_vertex)

    # add a unidirectional edge 
    def add_directed_edge(self, from_vertex, to_vertex):
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].edges.add(to_vertex)

    # breadth first traversal
    def bft(self, start_vertex):
        # create a queue
        q = Queue()
        # create a visited list
        visited = []
        # put start vertex in the queue
        q.enqueue(start_vertex)
        # while queue is not empty
        while q.len() > 0:
            # remove vertex from queue
            vertex = q.dequeue()
            #print(vertex)
            # check if it has been visited
            if vertex not in visited:
                # if not, mark as visited
                visited.append(vertex)
                #print(visited)
                # then put all children in queue
                for child in self.vertices[vertex].edges:
                    q.enqueue(child)           
        return visited

    # depth first traversal
    def dft(self, start_vertex):
        # create a stack
        stack = []
        # create a visited list
        visited = []
        # put start vertex in the stack
        stack.append(start_vertex)
        # while queue is not empty
        while len(stack) > 0:
            # remove vertex from stack
            vertex = stack.pop()
            # check if it has been visited
            if vertex not in visited:
                # if not, mark as visited
                visited.append(vertex)
                # then put all children in queue
                for child in self.vertices[vertex].edges:
                    stack.append(child)           
        return visited


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()

    def __repr__(self):
        return f"{self.edges}"

