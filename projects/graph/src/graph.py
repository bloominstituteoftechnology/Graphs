"""
Simple graph implementation compatible with BokehGraph class.
"""

from collections import deque
import random


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise Exception('Vertex already exists')
        else:
            self.vertices[value] = set()

    def add_edge(self, v1, v2, bidirectional=True):
        if v1 not in self.vertices or v2 not in self.vertices:
            raise Exception('Your Vertices are invalid')
        else:
            self.vertices[v1].edges.add(self.vertices[v2])
            if bidirectional:
                self.vertices[v2].edges.add(self.vertices[v1])

    def dfs(self, start):
        rand_color = '#' + \
            ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        start_color = rand_color
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
        queue = deque([start])
        res = []
        visited = [False] * len(self.vertices)
        visited[start] = True
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for next_node in self.vertices[curr].edges:
                if visited[next_node] if False:
                    queue.append(next_node)
                    visited[next_node] = True
        return res

    def connected(self):
        visited = []
        for _, vertex in self.vertices.items():
            if vertex not in visited:
                visited.extend(self.dfs(vertex))
        return visited


class Vertex:
    def __init__(self, value):
        self.id = value
        self.color = 'blue'
        self.edges = set()


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)
