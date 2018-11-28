"""
Simple graph implementation
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value) # --> Add value to the queue
    
    def dequeue(self):
        return self.queue.pop() if self.size() > 0 else None # --> Ternary !
    
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value) # --> Add value to the stack
    
    def pop(self):
        return self.stack.pop() if self.size() > 0 else None # --> Ternary !
    
    def size(self):
        return len(self.stack)

class Vertex:
    def __init__(self, vert_id):        
        self.id = vert_id    
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        '''
        there should be a field vertices that contains a dictionary
        mapping vertex labels to edges.
        '''
        self.vertices = {}

    def add_vertex(self, value): # --> Takes in a value
        self.vertices[value] = Vertex(value) # --> Creates a set with given value

    def add_edge(self, vertex_one, vertex_two): # --> vertex_one and vertex_two 
        # --> Need to check first if the vertex exists (If the circles are present)
        # --> To do this, we can use set-methods: get() to check if it is self.vertices
        if vertex_one in self.vertices and vertex_two in self.vertices:
            # --> Connect edges! (The arrows between the circles)
            self.vertices[vertex_one].edges.add(vertex_two)
            self.vertices[vertex_two].edges.add(vertex_one)
        else:
            raise IndexError("That vertex does not exist")  

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].esges.add(v2)
        else:
            raise IndexError("That vertex does not exist")
    
    def bft(self, starting_node):
        new_q = Queue() # --> Instantiate empty queue
        visited = set() # --> Create empty visited list
        new_q.enqueue(starting_node) # --> Add start_node to queue

        while new_q.size() > 0:
            node = new_q.dequeue() # --> Remove first node from Queue
            if node not in visited:                
                visited.add(node) # --> Mark it as visited
                print(self.vertices[node].edges)
                for child in self.vertices[node].edges:
                    new_q.enqueue(child)

    def dft(self, starting_node):
        new_stack = Stack()
        visited = []
        new_stack.push(starting_node)

        while new_stack.size() > 0:
            node = new_stack.pop()
            if node not in visited:
                visited.append(node)
                print(self.vertices[node].edges)
                for child in self.vertices[node].edges:
                    new_stack.push(child)
        
            
                



