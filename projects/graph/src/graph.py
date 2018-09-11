"""
Simple graph implementation compatible with BokehGraph class.
"""
from draw import BokehGraph

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, key, value, bidirectional=True):
        if key not in self.vertices or value not in self.vertices:
            raise Exception(f'No {key} vertex')

        self.vertices[key].add(value)

        if bidirectional:
            self.vertices[value].add(key)

    def dfs(self, start):
        stack = [start]
        visited = set()

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.vertices[vertex] - visited)

        return visited

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')

BokehGraph(graph).show()
print(graph.dfs('0'))

