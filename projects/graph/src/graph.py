"""
Simple graph implementation
"""

from collections import deque
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    
    def add_edge(self, vertex, edge):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)

    def breadth_first_traversal(self, starting_node):
        q = deque()
        visited = []
        q.append(starting_node)
        while len(q) > 0:
            node = q.popleft()
            visited.append(node)
            for child in node:
                if child not in visited:
                    q.append(child)
        return visited
    def depth_first_traversal(self, starting_node):
        stack = []
        visited = []
        stack.append(starting_node)
        while len(stack) > 0:
            node = stack.pop()
            visited.append(node)
            for child in node:
                if child not in visited:
                    stack.append(child)
        return visited
            


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
# print(graph.vertices)
print(graph.breadth_first_traversal(graph.vertices['0']))
print(graph.depth_first_traversal(graph.vertices['0']))
