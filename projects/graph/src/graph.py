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
        val = self.verticies[value1]
        val.add(value2)
        self.verticies[value1] = val
        val2 = self.verticies[value2]
        val2.add(value1)
        self.verticies[value2] = val2

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
print(graph.verticies)

print(graph.bfs('1'))
