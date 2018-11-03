"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, value = None, x = None, y = None):
        self.value = value
        self.x = x
        self.y = y
        self.adjVertices = set()

        if self.x is None:
            self.x = self.value
        if self.y is None:
            self.y = self.value

    def getAdjVertices(self):
        adjVerticesValues = set()
        for i in self.adjVertices:
            adjVerticesValues.add(i.value)
        return adjVerticesValues

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices = dict()):
        self.vertices = vertices

    def add_vertex(self, vertexValue):
        vertex = Vertex(vertexValue)
        self.vertices[vertex] = vertex
    
    def add_edge(self, originVertexValue, destinationVertexValue):
        inVertices1 = False
        inVertices2 = False

        for vertex in self.vertices:
            if originVertexValue == vertex.value:
                inVertices1 = True
                originVertex = vertex
            if destinationVertexValue == vertex.value:
                inVertices2 = True
                destinationVertex = vertex
        
        if inVertices1 == True and inVertices2 == True:
            originVertex.adjVertices.add(destinationVertex)
            destinationVertex.adjVertices.add(originVertex)
        else:
            raise IndexError("That vertex does not exist!")


# ### Test ###
# # To test, instantiate empty graph and run the following:
# graph = Graph()  # Instantiate your graph
# graph.add_vertex(0)
# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)
# graph.add_edge(0, 1)
# graph.add_edge(0, 3)
# # print(graph.vertices)

# for i in graph.vertices:
#     print("Value: ", i.value, " ; AdjVertices: ", i.getAdjVertices())















# ######### Initial Attempt ###########

# """
# Simple graph implementation compatible with BokehGraph class.
# """

# class Vertex:
#     def __init__(self, value):
#         self.value = value
#         self.adjVertices = set()

#     def getAdjVertices(self):
#         adjVerticesValues = set()
#         for i in self.adjVertices:
#             adjVerticesValues.add(i.value)
#         return adjVerticesValues

# # The code for the graph data structure below is different than that above in 
# # that it first requires that you instantiate vertex objects before adding them
# # as vertices to the graphs. Thebetter approach is to instantiate the vertex object 
# # within the Graph class by passing in the desired value of the vertex to the add 
# # vertex method in the Graph data structure. 
# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self, vertices = dict()):
#         self.vertices = vertices

#     def add_vertex(self, vertex):
#         self.vertices[vertex] = vertex
    
#     def add_edge(self, originVertex, destinationVertex):
#         originVertex.adjVertices.add(destinationVertex)
#         destinationVertex.adjVertices.add(originVertex)

# # To add an edge, the add_edge method should receive an origin Vertex and a destination Vertex.
# # This method should add a vertex to the adjVertices of the origin and destination vertices

# # v1 = Vertex(10)
# # v2 = Vertex(5)
# # v3 = Vertex(14)

# # g1 = Graph()

# # g1.add_vertex(v1)
# # g1.add_vertex(v2)
# # g1.add_vertex(v3)
# # # print(g1.vertices[v1].value)

# # g1.add_edge(v1,v3)
# # g1.add_edge(v1,v2)
# # print(v1.getAdjVertices())


# # The code below yields errors because my initial approach to the graph class first required that 
# # one instantiate the vertices before passing them in to the graph class. The initial graph code passes 
# # the desired vertex values to the graph class instead of passing in a vertex object. 

# # graph = Graph()  # Instantiate your graph
# # graph.add_vertex(0)
# # graph.add_vertex(1)
# # graph.add_vertex(2)
# # graph.add_vertex(3)
# # graph.add_edge(0, 1)
# # graph.add_edge(0, 3)
# # print(graph.vertices)