"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
import math
"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = random.randint(1,6) * (self.id+1) // 4
        if self.y is None:
            self.y = random.randint(1,6) * (self.id+1) % 4
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            colorString = "#"
            for i in range(0, 6):
                colorString += hexValues[random.randint(0,len(hexValues) - 1)]
            # Algorithm for bright colors
            # colorArray = ["F"]
            # for i in range(0, 2):
            #     colorArray.append(hexValues[random.randint(0,len(hexValues) - 1)])
            # random.shuffle(colorArray)
            # colorString = "#" + "".join(colorArray)
            # print(colorString)
            self.color = colorString


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")
    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")


##############################################################
# {
# '0': {'1', '3'},
# '1': {'0'},
# '2': set(),
# '3': {'0'}
# }     


# class Edge:
#     """Edges in the adjacency list are just a destination."""
#     # Using simple classes for illustrative purposes
#     # pylint: disable=too-few-public-methods
#     def __init__(self, destination):
#         self.destination = destination




# class Graph:
#     """The graph itself is simply a set of vertices."""
#     # pylint: disable=too-few-public-methods
#     def __init__(self):
#         self.vertices = set()

# class Vertex:
#     """Vertices have a label and a set of edges."""
#     # pylint: disable=too-few-public-methods
#     def __init__(self, vertex_id, x=None, y=None, value=None, color="white"):
#         self.id = int(vertex_id)
#         self.x = x
#         self.y = y
#         self.value = value
#         self.color = color
#         self.edges = set()
#         if self.x is None:
#           self.x = (self.id // 3) + self.id / 10  * (self.id % 3)
#         if self.y is None:
#           self.y = (self.id // 3) + self.id / 10  * (self.id % 3)
#         if self.value is None:
#           self.value = self.id
#         if self.color is None:
#           hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#           colorString = '#'
#           for in range(0,6):
#             colorString += hexValues[random.randint(0,len(hexValues)-1)]
#           self.color = colorString
#           # Algorithm for bright colors
#           # colorArray = ["F"]
#           # for i in range(0,2):
#           #   colorArray.append(hexValues[random.randint(0,len(hexValues)-1)])
#           # random.shuffle(colorArray)
#           # colorString = "#" + "".join(colorArray)
#           # print(colorString)
#           self.color = colorString

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#   def __init__(self):
#     self.vertices = {}
#   def add_vertex(self, vertex_id):
#     self.vertices[vertex_id] = Vertex(vertex_id)
#   def add_edge(self, v1, v2):
#     if v1 in self.vertices and v2 in self.vertices:
#       self.vertices[v1].edges.add(v2)
#       self.vertices[v2].edges.add(v1)
#     else:
#       raise IndexError("That vertex does not exist!")
#   def add_directed_edge(self, v1, v2):
#     if v1 in self.vertices and v2 in self.vertices:
#       self.vertices[v1].edges.add(v2)
#     else:
#       raise IndexError("That vertex does not exist!")

# class Graph2:
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.vertices:
#             self.vertices[vertex] = set()
#         else:
#             sys.exit("Vertex {} already exists.".format(vertex))

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 not in self.vertices:
#             sys.exit("No '{}' vertex!".format(vertex1))
#         elif vertex2 not in self.vertices:
#             sys.exit("No '{}' vertex!".format(vertex2))
#         else:
#             self.vertices[vertex1].add(vertex2)
#             self.vertices[vertex2].add(vertex1)x