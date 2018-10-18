"""
Simple graph implementation compatible with BokehGraph class.
"""
import random

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
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
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # self.vertices = vertices
        self.vertices = {}
    def add_vertex(self,vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    # def add_vertex(self,vertex):
    #     self.vertices.update({str(vertex): set()})
    #     print(f"Second line -> {self.vertices}")
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v2].edges.add(v2)
            self.vertices[v1].edges.add(v1)
        else:
            raise (IndexError("That vertex doesn't exist"))
    # def add_edge(self, vertex, edge):
    #     self.vertices.update({str(vertex): {str(node) for node in edge} })
    #     print(f"Third line -> {self.vertices}")


    # def dft(self, starting_node, visited=None):
    #     #  mark the node as visited
    #     if visited == None:
    #         visited = []
    #     visited.append(starting_node)
    #     # for each child, the child hasnt been visted it, call dft on that node
    #     # for child in children:
    #     #   if child not in visited:
    #     #       dft(child, visted)


    # def bft(self, starting_node):
    #     # created empty queue
    #     q = Queue()
    #     # put starting vert in queue
    #     q.enqueue(starting_node)
    #     visited = []
    #     while q.size > 0:
    #         # remove the first node form the queue
    #         # if it has not been visited yet
    #         # mark it as visited
    #         # then put all of it's children in the back of the queue
            

    # def dft_s(self, starting_node):
    #     # created empty queue
    #     s = Stack()
    #     # put starting vert in queue
    #     s.enqueue(starting_node)
    #     visited = []
    #     while s.size > 0:
    #         # remove the first node form the queue
    #         # if it has not been visited yet
    #         # mark it as visited
    #         # then put all of it's children in the back of the queue

class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x == None:
            self.x = random.random() * 10-3
        else:
            self.x = x
        if y == None:
            self.y= random.random() * 10-3
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

# graph = Graph({'0': {'1', '3'},'1': {'0'},'2': set(),'3': {'0'}})

# print(f"First line -> {graph.vertices}") First line
# graph.add_vertex(8) Second Line
# graph.add_edge(2, [1,2,3]) #hird line

