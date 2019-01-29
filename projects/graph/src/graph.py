"""
Simple graph implementation
"""
from queue import Queue
from stack import Stack

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
    
    def depth_first_traversal(self, starting_vertex):
        """
        depth_first_traversal is to just explore vertex from given point.
        Here all vertices will be visited depth first top-to-bottom
        """
        # push the starting point and mark it visited to stack
        # while stack is not empty
              # pop the TOP  (LIFO)
              # PRINT IT
              # if not visited mark it visited..
              # push all edge-vertex adjacent to it
                    # check if visited
        stack = Stack()
        visited = []        
        stack.push(starting_vertex)

        while stack.size() != 0:
            node = stack.pop_1()
            if node not in visited:
                print(node,end = " -> ")
                visited.append(node)
                for edge_node in self.vertices[node]:
                    #if edge_node not in visited:
                        stack.push(edge_node)
    
    def depth_first_search(self, starting_vertex, search_value):
        
        stack = Stack()
        visited = []        
        stack.push(starting_vertex)

        while stack.size() != 0:
            node = stack.pop_1()
            if node == search_value:
                return True

            if node not in visited:
                visited.append(node)
                for edge_node in self.vertices[node]:
                    #if edge_node not in visited:
                        stack.push(edge_node)
        return False

    # depth first traversal RECURSIVE-WAY
    def DFT_recursive(self, starting_vertex, visited = None):
        if visited is None:
            visited = []        
            
        visited.append(starting_vertex)
        print(starting_vertex, end = " -> ")

        for edge_node in self.vertices[starting_vertex]:
            if edge_node not in visited:
                self.DFT_recursive(edge_node, visited)
    
    def BFS_path(self, start, end):
        pass