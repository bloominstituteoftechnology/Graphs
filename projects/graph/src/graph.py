#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

import queue
import random

class Vertex:
    def __init__(self, label):
        self.label = label
        self.color = "#FFFFFF"

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.vertex_labels = []

    def add_vertex(self, v):
        if v not in self.vertex_labels:
            self.vertex_labels.append(v)
            vertex = Vertex(v)
            self.vertices[vertex] = set()
        else:
            raise ValueError("that vertex already exists in the graph")

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertex_labels or end not in self.vertex_labels:
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
        if start not in self.vertex_labels:
            raise Exception("%s is not a vertex in the graph")
        searched = set()
        q = []
        next_node = 0 if search_type == 'bfs' else -1
        if isinstance(start, str):
            for v in self.vertices.keys():
                if v.label == start:
                    start = v
        q.append(start)
        while len(q) > 0:
            current = q.pop(next_node)
            for child in self.vertices[current]:
                if child not in searched:
                    q.append(child)
            current.color = color
            searched.add(current)
        return searched