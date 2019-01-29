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
        
    def breadth_first_traversal(self, starting_vertex):
        """
        breadth_first_traversal is to just explore vertex from given point.
        Here all vertices will be visited width-wise i.e. level by level
        """
        # Enqueue the starting point and mark it visited
        # while queue is not empty
              # Dequeue the queue (FIFO)
              # PRINT IT
              # enqueue all vertuces adjacent to it
                    # check if visited
        queue = Queue()
        visited = []
        queue.enqueue(starting_vertex)
        visited.append(starting_vertex)
        
        while queue.is_Empty() != True:
            node = queue.dequeue()
            print(node, end = " -> ")
            for edge_node in self.vertices[node]:
                if edge_node not in visited:
                    queue.enqueue(edge_node)
                    visited.append(edge_node)
    
    def breadth_first_search(self, starting_vertex, search_value):
        queue = Queue()
        visited = []
        queue.enqueue(starting_vertex)
        visited.append(starting_vertex)
        
        while queue.is_Empty() != True:
            node = queue.dequeue()
            if node == search_value:
                return True
            for edge_node in self.vertices[node]:
                if edge_node not in visited:
                    queue.enqueue(edge_node)
                    visited.append(edge_node)
        return False
    
          

