import random

class Graph:
    def __init__(self):
        """
        Create an empty graph
        """
        self.vertices = {} # dictionary
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph
        """
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        """
        Add an undirected edge to the graph
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exists!") # Stretch goal - ensures that edges to nonexistent vertices are rejected
    def add_directed_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exists!") # Stretch goal - ensures that edges to nonexistent vertices are rejected


class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """
        Create an empty vertex
        """
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        if y is None:
            self.y = random.random() * 10 - 5 

    def __repr__(self):
        return f"{self.edges}"

# g = Graph()
# g.add_vertex('0')
# g.add_vertex('1')
# g.add_vertex('2')
# g.add_vertex('3')
# g.add_edge('0', '3')
# g.add_edge('0', '1')
# print(g.vertices)

# class Vertex:
#     def __init__(self, n):
#         self.name = n
#         self.neighbors = list()
#     def add_neighbor(self, vertex):
#         if vertex not in self.neighbors:
#             self.neighbors.append(v)
#             self.neighbors.sort()

# class Graph:
#     vertices = {}
#     def add_vertex(self, vertex):
#         if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
#             self.vertices[vertex.name] = vertex
#             return True
#         else:
#             return False
#     def add_edge(self, v1, v2):
#         if v1 in self.vertices and v2 in self.vertices:
#             for key, value in self.vertices.items():
#                 if key == v1:
#                     value.add_neighbor(v2)
#                 if key == v2:
#                     value.add_neighbor(v1)
#             return True
#         else:
#             return False
#     def print_graph(self):
#         for key in sorted(list(self.vertices.keys())):
#             print(key + str(self.vertices[key].neighbors))

# graph = Graph()
# graph.add_vertex(Vertex('0'))
# graph.add_vertex(Vertex('1'))
# graph.add_vertex(Vertex('2'))
# graph.add_vertex(Vertex('3'))
# graph.add_edge('0', '3') still not working
# graph.add_edge('0', '1') still not working
# print(graph.vertices)