"""
Simple graph implementation compatible with BokehGraph class.
"""
from collections import deque
import random


class Vertex:
    def __init__(self, name):
        self.name = name
        self.color = "blue"
        self.edges = set()


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise Exception('That V already exists.')
        else:
            self.vertices[value] = Vertex(value)

    def add_edge(self, v1, v2, bidirectional=True):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception(
                'Invalid vertex: one or more of the vertices  is invalid.')
        else:
            self.vertices[v1].edges.add(self.vertices[v2])
            if bidirectional:
                self.vertices[v2].edges.add(self.vertices[v1])

    def dfs(self, start):
        rand_color = "#" + \
            ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        start.color = rand_color
        stack = [start]
        visited = [start]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
            for next_node in current.edges:
                if next_node not in visited:
                    next_node.color = current.color
                    stack.append(next_node)
        return visited

    def bfs(self, start):
        queue = deque([start])
        result = []
        visited = [False] * len(self.vertices)
        visited[start] = True
        while queue:
            current = queue.popleft()
            result.append(current)
            for next_node in self.vertices[current].edges:
                if visited[next_node] is False:
                    queue.append(next_node)
                    visited[next_node] = True
        return result

    def connected(self):
            visited = []
            for _, vertex in self.vertices.items():
                if vertex not in visited:
                visited.extend(self.dfs(vertex))
        return visited
