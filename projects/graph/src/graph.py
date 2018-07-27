#!/usr/bin/python
"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    def __init__(self, label, color='white'):
        self.label = label
        self.color = color


from collections import namedtuple
Vertex = namedtuple('Vertex', ['label', 'color'])


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex, edges=()):
        # Add a new vertex, optionally with edges to other vertices.
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    def add_edge(self, start, end, bidirectional=True):
        # Add a edge (default bidirectional) between two vertices.
        if start not in self.vertices:
            raise Exception('Error: The start vertice is not in the graph.')
        elif end not in self.vertices:
            raise Exception('Error: The end vertice is not in the graph.')

        self.vertices[start].add(end)

        if bidirectional:
            self.vertices[end].add(start)

    def search(self, start, target=None, method='dfs'):
        # Search the graph using BFS or DFS.
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            quack.extend(self.vertices[current] - visited)

        return visited

    def find_components(self):
        # Identify components and update vertex component ids.
        visited = set()
        for vertex in self.vertices:
            if vetex not in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

    def search(self, start, target=None, method='dfs'):
        quack = [start]  # Queue or stack, depending on method
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            # Add possible (unvisited) vertices to queue
            queue.extend(self.vertices[current] - visited)

        return visited


def main():
    pass  # TODO write a demo that tests the graph class


if __name__ == '__main__':
    main()