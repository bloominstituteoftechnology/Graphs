"""
Simple graph implementation compatible with BokehGraph class.
"""
# http://interactivepython.org/courselib/static/pythonds/Graphs/Implementation.html

# the vertex class will create a single object with a key and an attached array of connections
    # vertex = {'A': ['B', 'C']}


# the Graph Class should create an object with vertices, each of which has a corresponding collection of neighbors
    # graph = {'A': ['B', 'C'],
    #          'B': ['C', 'D'],
    #          'C': ['D'],
    #          'D': ['C'],
    #          'E': ['F'],
    #          'F': ['C']}


class Vertex:
    def __init__(self, key):
        # storage space for neighboring nodes
        self.id = key
        self.neighbors = []
    def _repr__(self):
        return 'Vertex: ' + self.key
        # method to add an adjoining node
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor_node)
        # method to return a list of adjoining nodes
    def getNeighbors(self):
        return self.getNeighbors
        # method to check if an inputted node is connected to the node
    def isNeighbor(self, node):
        return node in self.neighbors

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.vertCount = 0

    def add_vertex(self)
        self.vertCount =+ 1
        newVertex = Vertex(key)
        self.vertCount[key] = newVertex
        return newVertex
    
    def get_vertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertices

    def add_edge(self, f, t)
        if f not in self.vertices:
            nv = self.add_vertex(f)
        if t not in self.vertices:
            nv = self.add_vertex(t)
        self.vertices[f].add_neighbor(t)

    def vertices(self):
        return self.vertices.keys()


# Tests for Graph Class
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)