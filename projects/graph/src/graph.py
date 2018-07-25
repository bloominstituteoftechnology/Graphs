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
        return "Vertex is {}".format(self.label)
    #I think the __str__ method is more readable than __repr__
    #to see what the properties are

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return str(self.vertices)

    def add_edge(self, start, end, bidirectional=True):
        if isinstance(start, Vertex):
            start = start.label
#isinstance will return True if (in this case) start is an instance of Vertex
#so basically, this part labels the starting point
#using key, if we are passed an object just get the key
        if isinstance(end, Vertex):
            end = end.label

        if start not in list(self.vertices.keys()):
            self.add_vertex(Vertex(start))

        if end not in list(self.vertices.keys()):
            self.add_vertex(Vertex(end))

        self.vertices[start].edges.add(self.vertices[end])
        if bidirectional:
            self.vertices[end].edges.add(self.vertices[start])

    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            vertex= Vertex(vertex)
        if vertex.label in self.vertices:
            return False
        self.vertices[vertex.label] = vertex
        return True


    def create_vertices_and_edges(self, n_verts):
        grid = []
        for i in range(n_verts):
            grid.append(Vertex(str(i)))

#randomly loop through verts, and randomly connect each to the next
        for i in range(n_verts - 1):
            if (random.randrange(n_verts) < n_verts // 2):
                if(random.randrange(n_verts) < n_verts // 2):
                    self.add_edge(grid[i].label, grid[i+1].label, False)
                self.add_edge(grid[i].label, grid[i+1].label)

        for vert in grid:
            self.add_vertex(vert)


#    def bfs(self, start):
#
#        #pick a random color
#        random_color = '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
#
#        #create queue and found lists, and append our start to each 
#        queue = []
#        found = []
#        queue.append(start)
#        found.append(start)
#
#        #add the color
#        start.color = random_color
#
#        #as long as there are items in the queue, for each edge in the edge array, if
#        #destination is not found in the found list, add it to the found list, add it
#        #to the queue, and add the color property. Then dequeue queue[0].
#        while (len(queue) > 0):
#            v = queue[0]
#            for edge in v.edges:
#                if edge not in found:
#                    found.append(edge)
#                    queue.append(edge)
#                    edge.color = random_color
#            queue.pop(0)
#        return found

    def dfs(self, start):
        #pick a random color
        random_color = '#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) 
        
        #create stack and found lists, append start to each
        stack = []
        found = []
        stack.append(start)
        found.append(start)
        
        #add the color
        start.color = random_color
        
        #as long as there are items in the stack, pop the last element. If popped
        #element is not in found, append it. For each edge in the edge array, if
        #destination not in found, assign it v's color and append it to stack.
        while (len(stack) > 0):
            v = stack.pop()
            if v not in found:
                found.append(v)
            for edge in v.edges:
                if edge not in found:
                    edge.color = v.color
                    stack.append(edge)
        return found


    def get_connected_components(self):
        searched = []
        for index, vertex in self.vertices.items():
#find the next vertex that hasn't already been found and run dfs on it
            if vertex not in searched:
                searched.append(self.dfs(vertex))
        return searched

#instantiate
graph=Graph()
graph.create_vertices_and_edges(10)
graph.get_connected_components()
BokehGraph(graph).show()
