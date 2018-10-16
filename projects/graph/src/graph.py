"""
Simple graph implementation compatible with BokehGraph class.
"""
from collections import deque


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise Exception('That vertex already exists.')
        else:
            self.vertices[value] = set()

    def add_edge(self, v1, v2):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception('Invalid vertex: one or more of the vertices provided is invalid.')
        else:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)

    def dfs(self, start):
        """
        Should be used as depth first traversal, with a start point
        Note: this dfs implementation is preorder
        """
        stack = [start]
        res = []
        visited = [False] * len(self.vertices)
        visited[start] = True
        while stack:
            curr = stack.pop()
            res.append(curr)
            for next_node in self.vertices[curr]:
                if visited[next_node] is False:
                    stack.append(next_node)
                    visited[next_node] = True
        return res

    def bfs(self, start):
        """
        Should be used as breadth first traversal, with a start point
        """
        queue = deque([start])
        res = []
        visited = [False] * len(self.vertices)
        visited[start] = True
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for next_node in self.vertices[curr]:
                if visited[next_node] is False:
                    queue.append(next_node)
                    visited[next_node] = True

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)