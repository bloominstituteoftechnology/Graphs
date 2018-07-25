#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vortex(self, vertex, edges=set()):
        if vertex not in self.vertices:
            self.vertices[vertex] = set(edges)
        else:
            raise ValueError("Vertice not found")

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Vertices not connecting in graph")
        else:
            self.vertices[start].add(end)
            if bidirectional:
                self.vertices[end].add(start)

    def breath_First_Search(self, start, reset):
        counter = 0
        component = []
        queue = []
        queue.append(start)

        queue.append(start)

        while counter < len(queue):
            node = queue[0]
            if node.color == 'white':
                node.color = 'gray'
                for edge in node.edges:
                    if edge not in component:
                        queue.append(edge)
                        found.append(edge)
                        counter += 1

            queue.pop(0)
        return found
        
