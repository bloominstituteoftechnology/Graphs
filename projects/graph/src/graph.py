"""
Simple graph implementation compatible with BokehGraph class.
"""
class Node:
    def __init__(self):
        # storage space for neighboring nodes
        self.neighbors = []
        # method to add an adjoining node
    def addNeighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)
        # method to return a list of adjoining nodes
    def getNeighbors(self):
        return self.getNeighbors
        # method to check if an inputted node is connected to the node
    def isNeighbor(self,node):
        return node in self.neighbors

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO




# Tests for Graph Class
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)