"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
import math

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if x is None:
            self.x = random.uniform(-1, 1)
        if y is None:
            self.y = random.uniform(-1, 1)
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            colorString = "#"
            for i in range(0,3):
                colorString += hexValues[random.randint(0,len(hexValues) - 1)]
            self.color = colorString

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self, circle_radius=.08, labels=True, x_range=(-1.1,1.1), y_range=(-1.1,1.1)):
        self.vertices = {}
        self.circle_radius = circle_radius
        self.labels = labels
        self.x_range = x_range
        self.y_range = y_range
        self.groups = []

    def add_vertex(self, vertex_id, x=None, y=None, value=None, color=None):
        if vertex_id in self.vertices:
            print("That vertex already exists")
            return False
        else:
            self.vertices[vertex_id] = Vertex(vertex_id, x, y, value, color)        

    def add_edge(self, startpoint, endpoint):
        if startpoint in self.vertices and endpoint in self.vertices:
            self.vertices[startpoint].edges.add(endpoint)
            self.vertices[endpoint].edges.add(startpoint)
        else:
            print("Invalid start or endpoint")
            return False

    def breadth_first_for_each(self, start):
        queue = [] # setup a que to check nodes
        queue.append(start) # first/root node
        visited = []
        while len(queue) > 0:
            current = queue.pop(0) # first in que pulled out
            visited.append(current) #push into visited
            for edge in self.vertices[current].edges:  #look at connections,  
                if edge not in visited and edge not in queue:    # if the connected node isn't visited,
                    queue.append(edge)   # then enqueue it
        return visited

    def depth_first_for_each(self, start):
        stack = [] # setup a que to check nodes
        stack.append(start) # first/root node
        visited = []
        while len(stack) > 0:
            current = stack.pop() # first in que pulled out
            visited.append(current) #push into visited
            for edge in self.vertices[current].edges:  #look at connections,  
                if edge not in visited and edge not in stack:    # if the connected node isn't visited,
                    stack.append(edge)   # then enqueue it
        return visited

