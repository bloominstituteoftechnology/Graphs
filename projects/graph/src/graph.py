#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class."""
class Vertex:
    """Vertices have a label and a set of edges."""

    def __init__(self, label, color="white"):
        self.label = label
        self.edges = set()
        self.color = color

    def __repr__(self):
       return str(self.label)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        pass  # TODO
        self.vertices = {}
        self.visited = False

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices[v] = set()
        else:
            raise ValueError("vertex already exists in the Graph")

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("%s or %s does not exist" %(start, end))
        else:
            self.vertices[start].add(end)
            if bidirectional == True:
                self.vertices[end].add(start)

     def bfs(self, start):

        queue = []
        trail = []
        start_vertex = self.vertices[start]
        queue.append(start_vertex)

        for vertex in self.vertices.values():
            vertex.visited = False

        while len(queue) > 0:
            current = queue.pop(0)
            if not current.visited:

                        queue.append(vertex)
                current.visited = True
                trail.append(current.label)

        return trail



#     g = Graph()
#     g.add_vertex('2')
#     g.add_vertex('3')
#     g.add_vertex('8')
#     g.add_edge('2','3')
#     g.add_edge('2','8')
#     g.add_edge('8','3')


# # print(g.vertices)





