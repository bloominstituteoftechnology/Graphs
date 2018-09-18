"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v1].add(v1)
        else:
            raise IndexError("THat vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("THat vertex does not exist!")

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)

class Vertex:
    def __init__(self, id, color="white"):
        self.id
        self.color
        self.edges = []

class Node:
    def __init__(self):
        self.neighbors = []
    def addNeighbor(self, neightbor_node):
        self.neighbors.append(neighbor_node)
    def getNeighbors(self):
        return self.neighbors
    def isNeighbor(self, node):
        return node in self.neighbors


# addNeighbor(): O(1)
# O(n)
# isNeighbor(): O(1)
edge_list = [
    (1, 2),
    (1, 4),
    (1, 7),
    (2, 3),
    (2, 5),
    (3, 6),
    (4, 7),
    (5, 6),
    (6, 7)
]

# addNeighbor()
# getNeighbors(): )(1)
# isNeighbor(): O( evg_edges )
adjacency_list = {
    1: [2, 4, 7],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 7],
    5: [2, 6],
    6: [3, 5, 7],
    7: [ 1, 4, 6]
}


# addNeighbor(): O(1)
# getNeighbors(): O(n)
# isNeighbor(): O(1)

# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)

