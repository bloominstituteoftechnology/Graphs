"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []
        else:
            raise ValueError(f'Vertex {vertex} already exists')
    
    def add_edge(self, edge, vertex):
        if vertex in self.vertices:
            if edge not in self.vertices[vertex]:
                self.vertices[vertex].append(edge)
            else:
                raise ValueError(f'Edge {edge} already exists with Vertex {vertex}')
        else:
            raise ValueError(f'Vertex {vertex} does not exist')
        
class Node:
    def __init__(self):
        self.neighbors = []
    # O(1)
    def addNeigbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
    # O(1)
    def getNeighbors():
        return self.neighbors
    # O(n)
    def isNeighbor(self, node):
        return node in self.neighbors

edge_list = [(1,2), (1,4), (1,7), (2,3), (2,5), (3,6), (4,7), (5,6), (6,7)]
# time: addNeighbor = O(1), getNeighbor = O(n), isNeighbor = O(n), addNode = O(1), removeNode = O(e)
# space: O(n+e)

adjacency_list = {
    1: [2,4,7],
    2: [1,3,5],
    3: [2,6],
    4: [1,7],
    5: [2,6],
    6: [3,5],
    7: [1,4,6]
}
# addNeighbor = O(1), getNeighbor = O(1), isNeighbor = O(avg_edges), addNode = O(1), removeNode = O(n^2)
# space: O(e)

adjacency_matrix = {
    1: [0,1,0,1,0,0,1],
    2: [1,0,1,0,1,0,0],
    3: [0,1,0,0,0,1,0],
    4: [1,0,0,0,0,0,1],
    5: [0,1,0,0,0,1,0],
    6: [0,0,1,0,1,0,1],
    7: [1,0,0,1,0,1,0],
}
# addNeighbor = O(1), getNeighbor = O(n), isNeighbor = O(1), addNode = O(n^2), removeNode = O(n^2)
# space: O(n^2)
