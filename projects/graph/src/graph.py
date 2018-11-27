"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}                                  # initialize an empty dictionary of verticies
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)        # key to be vertex_id and value to be Vertex 

    def add_edge(self, v1, v2):                             # undirected graph
        if v1 in self.vertices and v2 in self.vertices:     # if v1 and v2 both exist in the vertex list
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError('Vertex not found')

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError('Vertex not found')

    def bft(self, starting_node):
        # create an empty Queue
        # create an empty visited list
        # add the start node to the queue
        # while the Queue is not empty
            # remove the first node from the Queue
            # if it has not been visited
            # mark it as visited, then put all its children in the queue


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.edges = set()


