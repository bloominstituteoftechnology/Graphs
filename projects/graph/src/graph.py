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
            visited = set()
            queue = [start_vertex]
            i = 0

            while i < len(queue):
                vertex = queue[i]
                visited.add(vertex)

                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

                i += 1

            return queue

    def dft(self, start_vertex):
        if start_vertex not in self.vertices:
            print('Graph does not contain that vertex')

        else:
            visited = set()
            stack = [start_vertex]
            order = []

            while len(stack):
                vertex = stack.pop()
                visited.add(vertex)

                for neighbor in self.vertices[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)

                order.append(vertex)

            return order

    def recursive_dft(self, vertex, stack=None):
        if stack is None:
            if vertex not in self.vertices:
                print('Graph does not contain that vertex')

                return None

            else:
                stack = []

        stack.append(vertex)

        for neighbor in self.vertices[vertex]:
            if neighbor not in stack:
                self.recursive_dft(neighbor, stack)

        return stack
