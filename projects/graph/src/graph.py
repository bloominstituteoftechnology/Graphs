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

    def dft(self, start):
        stack = []
        stack.append(start)
        visited = []
        while(len(stack) > 0):
            current = stack.pop()
            visited.append(current)
            for edge in self.vertices[current]:
                if edge not in stack and edge not in visited:
                    stack.append(edge)
        print(visited)

        # def helper(adjlist, node_id, visited):
        #     visited.append(node_id)
        #     for child_node in adjlist[node_id]:
        #         if child_node not in visited:
        #             dft(adjlist, child_node, visited)

        # print('self verticles are: ', self.vertices)

        # if visited is None:
        #     visited.add(start)
        # else:
        #     node = self.vertices[0]
        #     if node not in visited:
        #         visited.add(node)
        # for node in self.vertices:

        # print("node #: ", node)
        # print("node #: ", self.vertices[node])
        # visited.append(node)

        # if node not in visited:
        #     print(node)
        #     self.bft(target, visited)

    def __str__(self):
        return f"Graph {self.vertices}"


# class Node:
#     def __init__(self, number):
#         self.number = number

#     def getnumber(self):
#         return self.number

#     def __str__(self):
#         return f"node #{self.number}"


graph = Graph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')


graph.add_directed_edge('A', 'B')
graph.add_directed_edge('A', 'C')
graph.add_directed_edge('B', 'D') #2
graph.add_directed_edge('B', 'E') #1
graph.add_directed_edge('E', 'F')
graph.add_directed_edge('C', 'F')
graph.add_directed_edge('F', 'A')
# graph.add_edge('0', '9')  # checking wrong index

graph.dft('B')
