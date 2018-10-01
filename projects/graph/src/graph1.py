"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjVertices = set()

    # def getAdjVertices(self):
    #     return self.adjVertices

    def getAdjVertices(self):
        adjVerticesValues = set()
        for i in self.adjVertices:
            adjVerticesValues.add(i.value)
        return adjVerticesValues





# class Edge:
#     def __init__(self, origin, destination):
#         self.origin = origin
#         self.destination = destination


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices = dict()):
        self.vertices = vertices

    def add_vertex(self, vertex):
        self.vertices[vertex] = vertex
    
    def add_edge(self, originVertex, destinationVertex):
        originVertex.adjVertices.add(destinationVertex)
        destinationVertex.adjVertices.add(originVertex)

#to add an edge, the add_edge method should receive an origin Vertex and a destination Vertex
#this method should add a vertex to the adjVertices of the origin and destination vertices

# v1 = Vertex(10)
# v2 = Vertex(5)
# v3 = Vertex(14)

# g1 = Graph()

# g1.add_vertex(v1)
# g1.add_vertex(v2)
# g1.add_vertex(v3)
# # print(g1.vertices[v1].value)

# g1.add_edge(v1,v3)
# g1.add_edge(v1,v2)
# print(v1.getAdjVertices())

# In the file graph.py, implement a Graph class that supports the API expected by draw.py. 
# In particular, this means there should be a field vertices that contains a dictionary 
# mapping vertex labels to edges. For example:

# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }

# The vertex '2' has no edges, while '0' is connected to both '1' and '3'.

# You should also create add_vertex and add_edge methods that add the specified entities to the graph. To test your implementation, instantiate an empty graph and then try to run the following:

graph = Graph()  # Instantiate your graph
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
print(graph.vertices)