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
        self.vertices = {} #nodes
        # vertex: edges

    def add_vertex(self, vertex): #creates nodes
        self.vertices[vertex] = set()

    def add_edge(self, from_vertex, to_vertex): #draws lines between nodes that exist
        if from_vertex in self.vertices and to_vertex in self.vertices:
            self.vertices[from_vertex].add(to_vertex)
            self.vertices[to_vertex].add(from_vertex)
        else: 
            print(f'{from_vertex} and {to_vertex} are not in this graph')

    def breadth_first_traversal(self, start_vertex):
        #empty Queue FIFO
        queue = Queue()
        #keeps track of order to be printed at the end
        visited = set()
        #add start_vertex to Queue
        queue.enqueue(start_vertex)
        # while Queue.length > 0
        while queue.size() > 0:
            #dequeue first item in queue
            #mark node as visited
            vertex = queue.dequeue() #current vertex
            if vertex not in visited:
                visited.add(vertex)
                #if neighbor, add to the queue
                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        queue.enqueue(neighbor) #add neighbor
        return visited

