"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {

        }
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        
    def add_edge(self, vert_1, vert_2):
        self.vertices[vert_1].add(vert_2)
        self.vertices[vert_2].add(vert_1)
    
    def bfs(self, node):
        visisted = set()
        queue = []

        queue.append(node)

        while len(queue) > 0:
            current_node = queue.pop()
            visisted.add(current_node)

            if self.vertices[current_node] is not set():
                for item in self.vertices[current_node]:
                    if item not in visisted:
                        queue.append(item)

        
        
