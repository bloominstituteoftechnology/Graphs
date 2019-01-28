"""
Simple graph implementation
"""

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
        self.vertices = { }

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex_a, vertex_b):
        if vertex_a in self.vertices.keys() and vertex_b in self.vertices.keys():
            self.vertices[vertex_a].add(vertex_b)
            self.vertices[vertex_b].add(vertex_a)
        else:
            print("Cannot find all vertices")

    def bft(self, starting_node):
        #create a queue
        q = Queue()
        #markt he first node as visited
        #enqeue starting node
        q.enqueue(starting_node)
        visited = []

        while q.size() > 0:
            dequeued = q.dequeue()
            visited.append(dequeued)
            print(dequeued)
            for edge in self.vertices[dequeued].edges:
                if edge not in visited:
                    q.enqueue(edge)
        return visited
            #remove first node from queue
            #if it h asnt been visited

    def dft(self, starting_node):
        s = Stack()

        visited = []

        s.push(starting_node)

        while stack:
            pass
        






    def dft_r(self, starting_node):
        #mark node as visited
        #call dft_r on all children



graph = Graph() #my graph instance
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('4', '3')

print(graph.vertices)
