"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    # Initialize an empty set when adding a vertex to the graph
    def add_vertex(self,vertex_id, color="white"):
        self.vertices[vertex_id] = set()
    # def get_edges(self,vertex_id):
    #     self.vertices[vertex_id]
    
    # When adding an edge, assume its undirected and check for membership
    def add_edge(self,v1,v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError('That vertex value is not available. please add it first')
    
    # When adding an directed edge, only check source node/vertex for membership
    def add_directed_edge(self,v1,v2):
        if v1 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex value is not available. please add it first')
            

# class Vertex:
#     def __init__(self, vertex_id, value, color="white"):
#         self.id = vertex_id
#         self.value = value
#         self.color = color
#         self.edges = []


# Testing
# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# print(graph.vertices)
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print(graph.vertices)
# graph.add_edge('10', '3')