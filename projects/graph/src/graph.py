#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
from draw import BokehGraph

class Vertex:
    def __init__(self, label, color='gray', **pos):
        self.label = label
        self.color = color
        self.pos = pos
        self.edges = set()

    def __str__(self):
        if not self.pos:
            pos = dict(x=None, y=None)
        else:
            pos = self.pos
        return self.edges

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return str(self.vertices)


    def add_vertex(self,vertex):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)

        if vertex in self.vertices:
            raise ValueError('oops, vertex already there') 

        self.vertices[vertex.label] = vertex
        return True

    def add_edge(self, start, end, bidirectional=True):
        if isinstance(start, Vertex):
            start = start.label

        if isinstance(end, Vertex):
            end = end.label

        if start not in list(self.vertices.keys()):
            self.add_vertex(Vertex(start))

        if end not in list(self.vertices.keys()):
            self.add_vertex(Vertex(end))

        self.vertices[start].edges.add(self.vertices[end])
        if bidirectional:
            self.vertices[end].edges.add(self.vertices[start])

    def create_vertices_and_edges(self, n_verts):
        grid = []
        for i in range(n_verts):
            grid.append(Vertex(str(i)))

        for i in range(n_verts - 1):
            if (random.randrange(n_verts) < n_verts // 2):
                if(random.randrange(n_verts) < n_verts // 2):
                    self.add_edge(grid[i].label, grid[i+1].label, False)
                self.add_edge(grid[i].label, grid[i+1].label)

        for vert in grid:
            self.add_vertex(vert)

    def debug(self):
        self.add_edge('0', '1')
        self.add_edge('5', '1')


    def bfs(self, start):
        random_color = '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        queue = []
        found = []
        queue.append(start)
        queue.append(start)

        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                if edge not in found:
                    found.append(edge)
                    queue.append(edge)
                    edge.color = random_color
            queue.pop(0)
        return found

    def get_connected_components(self):
        searched = []
        for index, vertex in self.vertices.items():
            if vertex not in searched:
                searched.append(self.bfs(vertex))
        return searched

graph=Graph()
graph.create_vertices_and_edges(10)
graph.get_connected_components()
BokehGraph(graph).show()
