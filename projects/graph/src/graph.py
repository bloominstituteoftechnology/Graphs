"""
Simple graph implementation compatible with BokehGraph class.
"""

# Need to store vertices (nodes) and edges
# Each node is an object and each edge is a pointer
# Below the graph class is a basic object with pointers

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add(end)
            self.vertices[end].add(start)
        else:
            return False

graph = Graph()  # Instantiate your graph
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
print(graph.vertices)

class Node:
    def __init__(self):
        self.neighbors = []
    def addNeighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node) # O(1) - constant time
    def getNeighbor(self):
        return self.neighbors # O(1) - constant time
    def isNeighbor(self, node): 
       return node in self.neighbors # O(n) - linear time

# There are more efficient ways of bulding a graph. 
# For example, creating an edge list

# edge_list = [
#     (1,2),
#     (1,4),
#     (1,7),
#     (2,3),
#     (2,5),
#     (3,6),
#     (4,7),
#     (5,6),
#     (6,7),
# ]

# Big O for edge lists:
# Add neighbor: O(1)
# Get neighbor: O(n)
# Is neighbor: O(n)

# adjacency_list = {
#     1: [2, 4, 7]
#     2: [1, 3, 5]
#     3: [2, 6]
#     4: [1, 7]
#     5: [2, 6]
#     6: [3, 5, 7]
#     7: [1, 4, 6]
# }

# Big O for adjacency lists:
# Add neighbor: O(1)
# getNeighbors: O(1)
# Is neighbor: O(n)

