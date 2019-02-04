"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self, vertices=None):
        # includes all vertices
        self.vertices = {} if vertices is None else vertices

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    # adding/creating an edge to a graph between vertices i and j
    def add_edge(self, i, j):
        # check if vertices are connected
        if not (i in self.vertices[j]):
            # makes sure that i is included in the list of vertices that connect to j
            self.vertices[j].add(i)
            # viseversa makes sure that j is included in the list of vertices that connect to i
            self.vertices[i].add(j)

    def bfs(self, target):
        queue = [target]
        visited = set([target])
        while queue:
            current = queue.pop()
            if current == target:
                break
            visited.add(current)
            queue.extend(self.vertices[current] - visited)
            visited.update(self.vertices[current])
        return visited
