"""
Simple graph implementation
"""
import collections

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = dict()
    
    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, vertex1, vertex2):
        self.vertices[vertex1].add(vertex2)
        self.vertices[vertex2].add(vertex1)
    
 
    """Write a function within your Graph class that takes takes a starting node as an argument, 
    then performs BFT. Your function should print the resulting nodes in the order they were visited."""
    def bft(self, root):
        
        # create a seen set and queue
        seen = [root]
        queue = [root] 
        while queue:
            vertex = queue.pop()
            # print(vertex)
            for node in self.vertices[str(vertex)]:
                if node not in seen:
                    print(f'visited nodes: {seen}')
                    seen.append(node)
                    queue.append(node)