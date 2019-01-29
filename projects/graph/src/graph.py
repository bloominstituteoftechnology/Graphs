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

    def add_edge(self, vertex_1, vertex_2):
        self.vertices[vertex_1].add(vertex_2)

    def bft(self, starting_node):
        # create a queue
        q = deque()
        visited = []
        # Enqueue the starting node
        q.append(starting_node)
        # while the queue is not empty,
        while q:
            # Dequeue a node form the queue
            node = q.popleft()
            # Mark it as visited
            visited.append(node)
            # Enqueue all of its children that have not been visited
            for child in self.vertices[node]:
                if child not in visited and child not in q:
                    q.append(child)
        return visited

    def dft(self, starting_node):
        # Create stack
        s = deque()
        visited = []
        # Push the starting node
        s.append(starting_node)
        # while the stack is not empty,
        while s:
            # Pop a node from the stack
            node = s.pop()
            # Mark it as visited
            visited.append(node)
            # Push all of its children that have not been visited
            for child in self.vertices[node]:
                if child not in visited and child not in s:
                    s.append(child)
        return visited

    def dtf_r(self, starting_node, visited=None):
        if visited is None:
            visited = []
        # Mark the node as visited
        if starting_node not in visited:
            visited.append(starting_node)
        for child_node in self.vertices[starting_node]:
            # Call dft_r on all unvisited children
            if child_node not in visited:
                self.dtf_r(child_node, visited)
        return visited
    
    def bfs(self, starting_node, target_node):
        q = deque()
        visited = set()
        path = []
        q.append(list(starting_node))
       
        while q:
            node = q.popleft()
            end_path = node[-1]
            if end_path not in visited:
                if end_path == target_node:
                    return node
                visited.add(end_path)
                for child in self.vertices[end_path]:
                    copy = list(node)
                    copy.append(child)
                    q.append(copy)
        return f'There is no path'
           
            