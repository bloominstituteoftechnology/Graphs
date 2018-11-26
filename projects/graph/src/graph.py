"""
Simple graph implementation compatible with BokehGraph class.
"""

from queue import *

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, value):
        self.verticies[value] = set()

    def add_edge(self, value1, value2):
        # Check's if the node exists, if not, return
        if value2 not in self.verticies:
            return

        val = self.verticies[value1]
        val.add(value2)
        self.verticies[value1] = val

        val2 = self.verticies[value2]
        val2.add(value1)
        self.verticies[value2] = val2

    def dfs(self, start):
        # Keep track of all the visited nodes and setup a stack
        visited, stack = set(), [start]

        # Keep looping until there are nodes still to be checked
        while stack:
            vertex = stack.pop()
            # Add the node if it is not in visited
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.verticies[vertex] - visited)
        return visited

    # Recursive solution
    def dfs_recursive(self, start, visited=None):
        # Set visited as a new set if not already
        if visited is None:
            visited = set()

        # Add the node
        visited.add(start)

        # Repeat until no more nodes left
        for next in self.verticies[start] - visited:
            self.dfs_recursive(next, visited)
        return visited

    def bfs(self, start):
        # Keep track of all visited nodes
        explored = []
        # Keep track of nodes to be checked
        queue = [start]

        # Keep looping until there are nodes still to be checked
        while queue:
            # Pop shallowest node (first node) from queue
            node = queue.pop(0)
            if node not in explored:
                # Add node to list of checked nodes
                explored.append(node)
                neighbours = self.verticies[node]

                # Add neighbors of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)
        return explored


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '5')
print(graph.verticies)

print(graph.bfs('1'))
print(graph.dfs('1'))
print(graph.dfs_recursive('1'))
