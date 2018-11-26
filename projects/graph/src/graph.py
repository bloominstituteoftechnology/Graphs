"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise Exception('Vertex already exists!')
        else:
            self.vertices[value] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception('Invalid input: vertices not in graph')
        else:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)

    def dfs(self, start):
        stack = [start]
        res = []
        visited = [False] * len(self.vertices)
        visited[start] = True
        while stack:
            current = stack.pop()
            res.append(current)
            for next_node in self.vertices[current]:
                if visited[next_node] is False:
                    stack.append(next_node)
                    visited[next_node] = True
        return res


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
