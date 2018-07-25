#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Vertex:
    """
    Represent a single vertex that is aware of all existing verrtices
    """
    all_vertices = set()
    all_vertix_labels = set()

    def __init__(self, label):
        if label in Vertex.all_vertix_labels:
            raise Exception('Error: vertex {} already exists'.format(label))

        self.label = label
        self.visited = False
        Vertex.all_vertices.add(self)
        Vertex.all_vertix_labels.add(self.label)

    def __repr__(self):
        return str(self.label)

    def _get_obj_instance(label):
        """
        Return Vertex object instance of string representation
        """
        for vertex in Vertex.all_vertices:
            if vertex.label == label:
                return vertex
        return None


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}
        self.vertex_obj_map = {}

    def add_vertex(self, vertex, edges=()):
        """
        Create Vertex instances and add to graph
        """
        vertex_edges = set()
        for edge in edges:
            if edge not in self.vertex_obj_map.keys():
                raise Exception(
                    'Error: cannot create edge to nonexistent vertex')
            vertex_edges.add(self.vertex_obj_map[edge])

        vertex = Vertex(vertex)
        self.vertex_obj_map[vertex.label] = vertex
        self.vertices[vertex.label] = vertex_edges

    def add_edge(self, start, end, bidirectional=True):
        """
        Add edge to existing vertex
        """
        if start not in self.vertex_obj_map.keys():
            raise Exception('Error: vertex {} does not exist'.format(start))
        if end not in self.vertex_obj_map.keys():
            raise Exception('Error: vertex {} does not exist'.format(end))

        start_vertex = self.vertex_obj_map[start]
        end_vertex = self.vertex_obj_map[end]

        self.vertices[start_vertex.label].add(end_vertex)
        if bidirectional:
            self.vertices[end_vertex.label].add(start_vertex)

    def bfs(self, start):
        """
        Search graph with breadth first algorithm
        """
        queue = []
        trail = []
        start_vertex = self.vertex_obj_map[start]
        queue.append(start_vertex)

        for vertex in self.vertex_obj_map.values():
            vertex.visited = False

        while queue:
            current = queue.pop(0)
            if not current.visited:
                for vertex in self.vertices[current.label]:
                    if not vertex.visited:
                        queue.append(vertex)
                current.visited = True
                trail.append(current.label)

        return trail

    def dfs(self, start):
        """
        Search graph with depth first search
        """
        stack = []
        trail = []
        start_vertex = self.vertex_obj_map[start]
        stack.append(start_vertex)

        for vertex in self.vertex_obj_map.values():
            vertex.visited = False

        while stack:
            current = stack.pop()
            if not current.visited:
                for vertex in self.vertices[current.label]:
                    if not vertex.visited:
                        stack.append(vertex)
                current.visited = True
                trail.append(current.label)

        return trail
