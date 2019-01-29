"""
Simple graph implementation
"""
from queue import Queue

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):    # O(1)
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
        
#class Queue():
#    def __init__(self):
#        self.queue = []
#    def enqueue(self, value):
#        self.queue.append(value)
#    def dequeue(self):        # O(n)
#        if self.size() > 0:
#            return self.queue.pop(0)
#        else:
#            return None
#    def size(self):
#        return len(self.queue)
    
    ## Here, the dequeue method is O(n), because if we're removing something from the beginning, we need to move the rest of the list over, so its costly.
    ## The best way is to implement queue using linked list
    ## But for this case, our list isn't too big so its fine.

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}    # empty dictionary
        
    def add_vertex(self, vertex):
        """ Check if the vertex is in vertices; if not, add it. """
        
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
            
    def add_edge(self, vertex_1, vertex_2):
        """ 
        Want directed edges. 
        Check if the vertices are in self.vertices; if yes, add the connection.
        """
        
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)    # vertex_1 -> vertex_2
        else:
            raise IndexError("The vertex does not exist!")
            
    def add_undirected_edge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)    # vertex_1 -> vertex_2
            self.vertices[vertex_2].add(vertex_1)
        else:
            raise IndexError("The vertex does not exist!")
            
    def breadth_first_traversal(self, starting_node):  # O(n)
        """ 
        Create a queue, the queue is implemented in a separate class.
        Add the start_node to the queue.
        Mark the first node as visited.
        Enqueue the starting node
        While the queue is not empty,
            Dequeue a node from the queue
            Mark it as visited
            Enqueue all of its children
        """
        
        queue = Queue()    # O(1)
        visited = set()
        queue.enqueue(starting_node)	# O(1)
    
        while queue.len() > 0: # O(n)
 
            current_vertex = queue.dequeue()	# O(1)
            
            if current_vertex is None:
                return
            
            if current_vertex not in visited:
                visited.add(current_vertex)	# O(1)
                print(current_vertex)
                for child in self.vertices[current_vertex]:
                    if child is not None:
                        queue.enqueue(child)

    