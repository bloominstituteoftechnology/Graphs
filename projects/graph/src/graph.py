"""
Simple graph implementation compatible with BokehGraph class.
"""

##### Implementation of the graph class with a seperate vertex class (from Graphs Day 3 lecture) #########
class Vertex: 
    def __init__(self, vertex_id, x = None, y = None, value = None, color = "white"):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.edges = set()
        self.color = color
        if self.x is None:
            self.x = self.id
        if self.y is None:
            self.y = self.id
        if self.value is None:
            self.value = self.id

class Graph: 
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        #we index vertex into dictionary by id  and we set the value to a vertex object
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")  
    def directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")        



# graph = Graph()
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)













# ########## Graph class code from Graphs Day 2 lecture (this implementation doesn't have the seperate Vertex class) #########
# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}
#     def add_vertex(self,vertex_id):
#         self.vertices[vertex_id] = set()
#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#             self.vertices[v2].add(v1)
#         else:
#             raise IndexError("That vertex does not exist!")
#     def directed_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError("That vertex does not exist!")






# #########  ORIGINAL ATTEMPT (DIDNT GET IT WORKING)  #######

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
