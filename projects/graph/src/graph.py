import queue
import random

# class Vertex:
#     """Vertices have a label and a set of edges."""

#     def __init__(self, label, color="white"):
#         self.label = label
#         self.edges = set()
#         self.color = color

#     def __repr__(self):
#        return str(self.label)

class Vertex:
    def __init__(self, label):
        self.label = label
        self.color = "#FFFFFF"

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.vert_labels = []

    def add_vertex(self, v):
        if v not in self.vert_labels:
            self.vert_labels.append(v)
            vertex = Vertex(v)
            self.vertices[vertex] = set()
        else:
            raise ValueError("that vertex already exists in the graph")

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vert_labels or end not in self.vert_labels:
            raise Exception("%s or %s is not a vertex in the graph" %(start, end))
        else:
            for v in self.vertices.keys():
                if v.label == start:
                    start_vertex = v
                if v.label == end:
                    end_vertex = v
            self.vertices[start_vertex].add(end_vertex)
            if bidirectional == True:
                self.vertices[end_vertex].add(start_vertex)

    def search(self, start, color, search_type='bfs'):
        if start not in self.vert_labels:
            raise Exception("%s is not a vertex in the graph")
        searched = set()
       queue = []
        next_node = 0 if search_type == 'bfs' else -1
        if isinstance(start, str):
            for v in self.vertices.keys():
                if v.label == start:
                    start = v
       queue.append(start)
        while len(queue) > 0:
            current = queue.pop(next_node)
            for child in self.vertices[current]:
                if child not in searched:
                   queue.append(child)
            current.color = color
            searched.add(current)
        return searched