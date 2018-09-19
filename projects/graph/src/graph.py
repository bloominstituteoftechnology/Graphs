"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def vertices(self):
        return self.vertices

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v1].edges.add(v1)
        else:
            raise IndexError("THat vertex does not exist!")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("THat vertex does not exist!")

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color="white"):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = self.id
        if self.y is None:
            self.y = self.id
        if self.value is None:
            self.value = self.id

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

# def dft(adjList, node_id, visited):
#     print(node_id)
#     visited.append(node_id)
#     for child_node in adjList[node_id]:
#         if child_node not in visited:
#             dft(adjList, child_node, visited)

def dft(self, adjList, node_id, visited):
    print(node_id)
    visited.append(node_id)
    for child_node in adjList[node_id]:
        if child_node not in visited:
            self.dft(adjList, child_node, visited)

def dfs(self, adjList, node_id, visited, search_node):
    if node_id == search_node: 
        return True
    visited.append(node_id)
    for child_node in adjList[node_id]:
        if child_node not in visited:
            self.dfs(adjList, child_node, visited, search_node)

def bft(self, adjList, node_id):
    frontier = []
    frontier.append(node_id)
    visited = []
    while len(frontier) > 0:
        n = frontier.pop(0)
        if n not in visited:           
            print(n)
            visited.append(n)
            for next_node in adjList[n]:
                frontier.append(next_node)



