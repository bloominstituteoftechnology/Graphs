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
        visited = []
        queue = []

        queue.append(node)

        while len(queue) > 0:
            current_node = queue.pop()
            visited.append(current_node)
            for i in self.vertices[current_node]:
                if i not in visited:
                    queue.append(i)
            return queue

    def dfs(self, node):
        visited = []
        stack = []
        stack.append(node)
        while len(stack) > 0:
            current_node = stack.pop()
            if node not in visited:
                visited.append(current_node)
                for next_nodes in self.vertices[current_node]:
                    stack.append(next_nodes)

          
        
