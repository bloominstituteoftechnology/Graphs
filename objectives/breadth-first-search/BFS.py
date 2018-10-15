"""Graph representation using adjacency list."""
from random import randint


class Vertex:

    def __init__(self, label, component=-1):
        self.label = str(label)
        self.component = component


class Graph:

    """Adjacency list graph."""
    def __init__(self):
        self.vertices = {}
        self.components

    def __str__(self):
        return str(self.vertices)

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices.add(vertex)

    def search(self, start, target=None, method='dfs'):
        quack = [start]
        pop_index = 0 if method == 'bfs' else -1
        visited = set()
        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            quack.extend(self.vertices[current] - visited)
        return visited

    def find_components(self):
        ''' Identify components and updtae vertex component ids'''
        visited = set()
        current_component = 0

        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component
