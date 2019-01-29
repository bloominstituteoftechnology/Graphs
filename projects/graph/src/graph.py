"""
Simple graph implementation
"""


class Graph:
    "Represent a graph as a dictionary of vertices mapping labels to edges."

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.vertices:
            self.vertices[vertex1].add(vertex2)
            self.vertices[vertex2].add(vertex1)
        else:
            print('Graph does contain both of those vertices')

    def bft(self, start_vertex):
        if start_vertex not in self.vertices:
            print('Graph does not contain that vertex')

        else:
            visited = {}
            queue = [start_vertex]
            i = 0

            for vertex in self.vertices.keys():
                visited[vertex] = 0

            while i < len(queue):
                vertex = queue[i]
                visited[vertex] = 1

                for neighbor in self.vertices[vertex]:
                    if not visited[neighbor]:
                        queue.append(neighbor)

                i += 1

            return queue

    def dft(self, start_vertex):
        if start_vertex not in self.vertices:
            print('Graph does not contain that vertex')

        else:
            visited = {}
            stack = [start_vertex]
            order = []

            for vertex in self.vertices.keys():
                visited[vertex] = 0

            while len(stack):
                vertex = stack.pop()
                visited[vertex] = 1

                for neighbor in self.vertices[vertex]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

                order.append(vertex)

            return order
