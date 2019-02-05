"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = {}
    # Part 1    
    def add_vertex(self, value):
        if not value in self.vertices:
            self.vertices[value] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print(f"Vertex '{v2}' does not exist.")

    # Breadth First Traversal
    def bft(self, vertex):
        queue = [vertex]
        visited = set(vertex)
        while len(queue) > 0:
            for i in self.vertices[queue[0]]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

            print(queue.pop(0))

    # Depth First Traversal
    def dft(self, vertex):
        stack = [vertex]
        visited = set(vertex)
        while len(stack) > 0:
            current_vertex = stack.pop()
            print(current_vertex)
            for i in self.vertices[current_vertex]:
                if i not in visited:
                    visited.add(i)
                    stack.append(i)

    def dft_r(self, vertex, cache = set()):
        print(vertex)
        cache.add(vertex)
        for i in self.vertices[vertex]:
            if i not in cache:
                self.dft_r(i, cache)


graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '4')  # No '4' vertex, should raise an Exception!
print(graph.vertices)
graph.bft('0')
graph.dft('2')
graph.dft_r('0')

