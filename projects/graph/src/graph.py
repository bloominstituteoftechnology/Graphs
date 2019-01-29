"""
Simple graph implementation
"""
from queue import Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}    # empty dictionary
        
    def add_vertex(self, vertex):
        """ Check if the vertex is in vertices; if not, add it. """
        
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
            
    def add_edge(self, vertex_1, vertex_2):
        """ Check if the vertices are in self.vertices; if yes, add the connection. """
        
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            self.vertices[vertex_1].add(vertex_2)    # vertex_1 -> vertex_2
            self.vertices[vertex_2].add(vertex_1)
            
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
                for child_vertex in self.vertices[current_vertex]:
                    if child_vertex is not None:
                        queue.enqueue(child_vertex)
