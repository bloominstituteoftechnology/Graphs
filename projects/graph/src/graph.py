"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, value):
        self.vertices[value] = set()

    def add_edge(self, parent, child):
        if parent in self.vertices and child in self.vertices:
            self.vertices[parent].add(child)
        else:
            print("One or more vertices, not in graph")

    def bft(self, vertex):
        queue = []
        visited = []
        if vertex in self.vertices:
            queue.append(vertex)
            while queue:
                for vertex in self.vertices[queue[0]]:
                    if vertex in visited:
                        continue
                    queue.append(vertex)
                visited.append(queue.pop(0))
            print(visited)
        else:
            print("Vertex not in list")

    def dft(self, vertex):
        queue = []
        visited = []
        if vertex in self.vertices:
            queue.append(vertex)
            while queue:
                print("iteration", queue)
                for vertex in self.vertices[queue[0]]:
                    if vertex in visited:
                        continue
                    queue.insert(0, vertex)
                    print(queue)
                visited.append(queue.pop(-1))
            print(visited)
        else:
            print("Vertex not in list")
