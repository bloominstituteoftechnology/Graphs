"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, node):
        self.vertices[node] = set()
        return self.vertices

    def add_edge(self, from_node, to_node):
        if self.vertices[from_node] != None and self.vertices[to_node] != None:
            self.vertices[from_node].add(to_node)
            self.vertices[to_node].add(from_node)
        else:
            raise IndexError("That vertex doesnt exist")
        return

    def add_directed_edge(self, from_node, to_node):
        if self.vertices[from_node] != None and self.vertices[to_node] != None:
            self.vertices[from_node].add(to_node)
        else:
            raise IndexError("That vertex doesnt exist")
        return

    # def bft(self, target, visited=[]):
    #     # print('self verticles are: ', self.vertices)

    #     for node in self.vertices:
    #         # print("node #: ", node)
    #         # print("node #: ", self.vertices[node])
    #         visited.append(node)
    #         if self.vertices[node] not in visited:
    #             print(node)
    #             self.bft(target, visited)

    def __str__(self):
        return f"Graph {self.vertices}"


# class Node:
#     def __init__(self, number):
#         self.number = number

#     def getnumber(self):
#         return self.number

#     def __str__(self):
#         return f"node #{self.number}"


# graph = Graph()

# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_vertex('4')
# graph.add_vertex('5')
# graph.add_vertex('6')
# graph.add_vertex('7')

# graph.add_directed_edge('0', '1')
# graph.add_directed_edge('0', '3')
# graph.add_edge('0', '9')

# graph.bft(3)

