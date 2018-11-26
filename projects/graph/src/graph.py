"""
Simple graph implementation compatible with BokehGraph class.
"""
from collections import deque
import random


class Vertex:
    def __init__(self, name):
        self.name = name
        self.color = 'blue'
        self.edges = set()


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise Exception('That vertex already exists.')
        else:
            self.vertices[value] = Vertex(value)

    def add_edge(self, v1, v2, bidirectional=True):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception('Invalid vertex: one or more of the vertices provided is invalid.')
        else:
            self.vertices[v1].edges.add(self.vertices[v2])
            if bidirectional:
                self.vertices[v2].edges.add(self.vertices[v1])

    def dfs(self, start):
        """
        Should be used as depth first traversal, with a start point
        Note: this dfs implementation is preorder
        """
        rand_color = "#" + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        start.color = rand_color
        stack = [start]
        visited = [start]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.append(curr)
            for next_node in curr.edges:
                if next_node not in visited:
                    next_node.color = curr.color
                    stack.append(next_node)
        return visited

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
            for next_node in self.vertices[curr].edges:
                if visited[next_node] is False:
                    queue.append(next_node)
                    visited[next_node] = True
        return res

    def connected(self):
        visited = []
        for _, vertex in self.vertices.items():
            if vertex not in visited:
                visited.extend(self.dfs(vertex))
        return visited
