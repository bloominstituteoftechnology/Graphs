"""
Simple graph implementation
"""
from queue import Queue

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        #Graph is a set of vertices
        self.vertices = dict() # or {} instead of dict()

    def add_vertex(self, vertex):
        if vertex not in self.vertices.keys():
            self.vertices[vertex] = set()
        return 'vertex already exist...'

    def add_edge(self, start_point, end_point):
        if start_point in self.vertices and end_point in self.vertices:
            #graph is bidirectional.. should add edges back and forth
            self.vertices[start_point].add(end_point)
            self.vertices[end_point].add(start_point) 
        return "vertices not in graph"
    
    
    def breadth_first_traversal(self):
        # Create a Queue
        queue = Queue()
        visited = []
        if self.vertices:
            # Enqueue the starting node
            queue.enqueue(self.vertices['0'])

        # While the queue is not empty
        while queue:
            # Dequeue a node from the queue 
            current_vertex = queue.dequeue()
            # Mark it as visited
            visited.append(current_vertex)
            print(current_vertex)

            # Enqueue all of its children that have not been visted
            for edge in self.vertices[str(current_vertex)]: 
                if edge not in visited: 
                    queue.enqueue(edge) 
    
            


