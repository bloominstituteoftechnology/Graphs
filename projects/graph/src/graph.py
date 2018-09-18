"""
Simple graph implementation compatible with BokehGraph class.
"""

#FROM Class Solutions

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self,vertex_id):
        self.vertices(vertex_id) = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices(v1).add(v2)
            self.vertices(v2).add(v1)
        else:
            raise IndexError("That vertex does not exist!")








# We want something of the form 
# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }
# where the keys are the vertices and the associated values
# (contained in a dictionary) are the edges



#### Graph implementation must be compatible with BokehGraph (see: https://bokeh.pydata.org/en/latest/docs/user_guide/graph.html)
# -The ColumnDataSource associated with the node sub-renderer must have 
# a column named "index" that contains the unique indices of the nodes.
# -The ColumnDataSource associated with the edge sub-renderer has two 
# required columns: "start" and "end". These columns contain the node
# indices of for the start and end of the edges.


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
print(graph.vertices)





# #########ORIGINAL ATTEMPT (DIDNT GET IT WORKING)#######

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}

#     def count(self):
#         #Return the number of vertices in the graph
#         return len(self.vertices)

#     def add_vertex(self, label):
#         v = Vertex(label)
#         self.vertices[v] = set()
#         return v
    
#     def add_edge(self, origin, destination):
#         # Insert and return new Edge from origin to destination 
#         e = self.Edge(origin, destination)
#         origin.edges.add_vertex(destination)
#         destination.edges.add_vertex(origin)


#     #Vertex Class
#     class Vertex:
#         def __init__(self, label):
#             self.label= label
#             self.edges = set()
        
#         def __str__(self):
#             return "Vertex " + str(self.label)

#     #Edge Class
#     class Edge:
#         def __init__(self, origin, destination):
#             self.origin = origin
#             self.destination = destination
        
#         def endpoints(self):
#             return (self.origin, self.destination)
