"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges"""

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

    def bfs(self, start):
        queue = [start]
        visited = set()

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.vertices[vertex] - visited)

        return visited

    def get_components(self):
        visited = []

        for i in range(len(self.vertices)):
            components = self.dfs(i)
            if components not in visited:
                visited.append(components)

        return visited
