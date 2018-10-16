"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, vertices):
        self.vertices = vertices
        # self.vertices = {}
    # def add_vertex(self,vertex_id):
    #     self.vertices[vertex_id] = Vertex(vertex_id)
    def add_vertex(self,vertex):
        self.vertices.update({str(vertex): set()})
        print(f"Second line -> {self.vertices}")
    # def add_edge(self, v1, v2):
    #     if v1 in self.vertices and v2 in self.vertices:
    #         self.vertices.edges.add(v2)
    #         self.vertices.edges.add(v1)
    #     else:
    #         raise (IndexError("That vertex doesn't exist"))
    def add_edge(self, vertex, edge):
        self.vertices.update({str(vertex): {str(node) for node in edge} })
        print(f"Third line -> {self.vertices}")

# class Vertex:
#     def __init__(self, vertex_id):
#         self.id = vertex_id
#         self.edges = set()
#     def __repr__(self):
#         return f"{self.edges}"

graph = Graph({'0': {'1', '3'},'1': {'0'},'2': set(),'3': {'0'}})

print(f"First line -> {graph.vertices}") #First line
graph.add_vertex(8) #Second Line
graph.add_edge(2, [1,2,3]) #Third line

