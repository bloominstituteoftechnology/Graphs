"""
Simple graph implementation compatible with BokehGraph class.
"""
from collections import deque
from random import random, sample

# If your class is merely a collection of properties, you can
# use a named tuple. This is an alternative: use the one that
# best makes sense for your code and your use cases.


class Vertex:
    """Object representation of Vertex"""
    def __init__(self, label, pos=None, color=None):
        self.label = label
        self.pos = pos
        self.color = color
        self.status = 'new'
        self.edges = set()

    def __repr__(self):
        return str(self.label)

    def __hash__(self):
        return hash(str(self.label))

    def __eq__(self, other):
        return self.label == str(other)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to
       edges."""
    def __init__(self, num_vertices=0, num_edges=0, chance=1):
        self.vertices = {}

        if num_vertices > 0:
            for i in range(0, num_vertices):
                new_vertex = Vertex(i)
                self.add_vertex(new_vertex)

            for _ in range(num_edges):
                if random() <= chance:
                    vertices = sample(list(self.vertices.values()), 2)
                    self.add_edge(vertices[0], vertices[1])

    def add_vertex(self, vertex, edges=()):
        """Add a new vertex, optionally with edges to other vertices."""
        if vertex in self.vertices:
            raise Exception('Error: adding vertex that already exists')
        # TODO: check if the below error condition still works
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: cannot have edge to nonexistent vertices')
        self.vertices[vertex.label] = vertex
        for edge in edges:
            self.vertices[vertex.label].edges.add(edge)

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge (default bidirectional) between two vertices."""
        if start.label not in self.vertices or end.label not in self.vertices:
            raise Exception('Vertices to connect not in graph!')
        self.vertices[start.label].edges.add(end)
        if bidirectional:
            self.vertices[end.label].edges.add(start)

    def find_connected_components(self):
        """Iterates over object's vertices property and finds all
           connected components"""
        connected_components = []

        for vertex in self.vertices.values():
            vertex.status = 'new'
        for vertex in self.vertices.values():
            component = None
            if vertex.status == 'new':
                component = self.find_connections(vertex)
            if component:
                connected_components.append(component)
        return connected_components

    def find_connections(self, startVert):
        """Given a starting vertex, find all vertices connected
           with the vertex."""
        visited = set()

        def add_to_visited(vertex): visited.add(vertex)

        self._bfs(add_to_visited, startVert)
        return visited

    def _bfs(self, cb, startVert):
        """General BFS method which accepts a callback function.
           Think of it as a `forEach` for trees"""
        vert_queue = deque()

        if startVert.status != 'done':
            startVert.status = 'visited'
            cb(startVert)
            vert_queue.append(startVert)
            while len(vert_queue) > 0:
                u = vert_queue[0]
                for vertex in u.edges:
                    if vertex.status == 'new':
                        vertex.status = 'visited'
                        cb(vertex)
                        vert_queue.append(vertex)
                u.status = 'done'
                vert_queue.popleft()


def main():
    graph = Graph()  # Instantiate your graph

    vl = [
        Vertex('0'),
        Vertex('1'),
        Vertex('2'),
        Vertex('3'),
    ]

    for v in vl:
        graph.add_vertex(v)

    graph.add_edge(vl[0], vl[1])
    graph.add_edge(vl[0], vl[3])
    print(graph.find_connected_components())
    print(graph.vertices)


if __name__ == '__main__':
    main()
