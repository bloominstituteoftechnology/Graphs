#!/usr/bin/python
import random
from random import choice
"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """Vertices have a label and a set of edges."""
    def __init__(self, label, color="white", **pos):
        self.label = label
        self.edges = set()
        self.color = color
        self.pos = pos

''' def __str__(self):
        if not self.pos:
            pos = dict(x=None, y=None)
        else:
            pos = self.pos
        return """Vertex is {}, position at ({}, {}), color is {} and has
                edges{}  """.format(self.label, pos['x'],
                                    pos['y'], self.color, self.edges)
'''


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges"""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return str(self.vertices)

    """def add_edge(self, start, end, bidirectional=True):
        Add an edge from start to end.
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        else:
            self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)"""

    def add_edge(self, start, end, bidirectional=True):
        """ And an edge (default bidirectional) between two vertices"""

        # Change this so that if not in vertices, just add it
        '''
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Vertices to connect not in graph!")
        self.vertices[start].add(end)
        '''
        # using the key, if we are passed an object just get the key

        if isinstance(start, Vertex):
            start = start.get('label')

        if isinstance(end, Vertex):
            end = end.label

        # add start if not in vertices
        if start not in list(self.vertices.keys()):
            self.add_vertex(Vertex(start))

        # add end if not in vertices
        if end not in list(self.vertices.keys()):
            self.add_vertex(Vertex(end))

        self.vertices[start].edges.add(self.vertices[end])
        if bidirectional:
            self.vertices[end].edges.add(self.vertices[start])

    def add_vertex(self, vertex):

        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)

        if vertex.label in self.vertices:
            return False  # ignores it

        self.vertices[vertex.label] = vertex
        return True  # added

    """def add_vertex(self, vertex, edges=()):
        if vertex in self.vertices:
            raise Exception("Error: trying to add vertex that already exists")
        if not set(edges).issubset(self.vertices):
            raise Exception("Error:: cannot have edge to nonexistent vertex")
        if vertex not in self.vertices:
            self.vertices[vertex] = set(edges)"""

    def create_vertices_and_edges(self, n_verts):
        # create verts and put them in a grid
        grid = []
        for i in range(n_verts):
            grid.append(Vertex(str(i)))

        # randomly loop through verts and randomly
        # connect it to the next one, passing in the random bidirection
        for i in range(n_verts - 1):
            if (random.randrange(n_verts) < n_verts // 2):
                if (random.randrange(n_verts) < n_verts // 2):
                    self.add_edge(grid[i].label, grid[i+1].label, False)
                self.add_edge(grid[i].label, grid[i+1].label)

        for vert in grid:
            self.add_vertex(vert)

    def breadth_first_search(self, start):
        checked_color = '#' + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        que = []
        checked = []

        que.append(start)
        checked.append(start)

        start.color = checked_color

        while len(que):
            vert = que[0]
            for edge in vert.edges:
                if edge not in checked:
                    checked.append(edge)
                    que.append(edge)
                    edge.color = checked_color
            que.pop(0)
        return checked

    def depth_first_search(self, start):
        checked_color = '#' + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        stack = []
        checked = []

        stack.append(start)
        checked.append(start)

        start.color = checked_color

        while len(stack):
            vert = stack[-1]
            for edge in vert.edges:
                if edge not in checked:
                    checked.append(edge)
                    stack.append(edge)
                    edge.color = checked_color
            stack.pop()
        return checked

    def get_connected_components(self):
        checked = []

        for index, vertex in self.vertices.items():
            if vertex not in checked:
                checked.append(self.breadth_first_search(vertex))
                # checked.append(self.depth_first_search(vertex))
        print(type(checked))
        return checked
"""t = [1, 2, 3]

t.append(["6"])
x = Vertex("6")
y = Vertex("6")
if "6" in t:
    print('yes')
"""
