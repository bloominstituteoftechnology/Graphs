"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO

class Node:
    def __init__(self): 
        self.neighbors = []
    def addNeighbor(self, neighbor_node): # O(1)
        self.neighbors.append(neighbor_node) 
    def getNeighbors(self):  # O(1)
        return self.neighbors
    def isNeighbor(self, node): # O(n)
        return node in self.neighbors

# addNeighbor(): O(1)
# getNeighbors(): O(n)
# isNeighbor(): O(n)
# adNode(): O(1)
# removingNode(): O(e)
# how much memory?: O(e)
edge_list = [
    {1,2},
    {1,4},
    {1,7},
    {2,3},
    {2,5},
    {3,6},
    {4,7},
    {5,6},
    {6,7}
]
# addNeighbor(): O(1)
# getNeighbors(): O(1)
# isNeighbor(): O( avg_edges)
# adNode(): O(1)
# removingNode(): O(n^2)
# how much memory?: O(n + e)
adjacency_list = {
    1: [2, 4, 7],
    2: [1, 5, 3],
    3: [2, 6],
    4: [1, 7],
    5: [2, 6],
    6: [3, 5, 7],
    7: [1, 4, 6],
    8: []
}

# addNeighbor(): O(1)
# getNeighbors(): O(n)
# isNeighbor(): O(1)
# adNode(): O(n*2)
# removingNode(): O(n^2)
# how much memory?: O(n^2)
adjacency_matrix = {
    1: [0, 1, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 0, 1, 0, 0, 0],
    3: [0, 1, 0, 0, 0, 1, 0, 0],
    4: [1, 0, 0, 0, 0, 0, 1, 0],
    5: [0, 1, 0, 0, 0, 1, 0, 0],
    6: [0, 0, 1, 0, 1, 0, 1, 0],
    7: [1, 0, 0, 1, 0, 1, 0, 0],
    8: [0, 0, 0, 0, 0, 0, 0, 0]
}
