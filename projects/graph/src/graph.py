import random

"""
Simple graph implementation compatible with BokehGraph class.
"""

# Need to store vertices (nodes) and edges
# Each node is an object and each edge is a pointer
# Below the graph class is a basic object with pointers

class Vertex:
    def __init__(self, vertex_id, x=None, y=None, value=None, color=None):
        self.id = int(vertex_id)
        self.x = x
        self.y = y
        self.value = value
        self.color = color
        self.edges = set()
        if self.x is None:
            self.x = 2 * (self.id // 3) + self.id / 10 * (self.id % 3)
        if self.y is None:
            self.y = 2 * (self.id % 3) + self.id / 10 * (self.id // 3)
        if self.value is None:
            self.value = self.id
        if self.color is None:
            hexValues = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
            colorString = "#"
            for i in range(0, 3):
                colorString += hexValues[random.randint(0,len(hexValues) - 1)]
            self.color = colorString

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = Vertex(vertex_id) # indexing it in a dict by id and setting it to a Vertex object
    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].edges.add(end)
            self.vertices[end].edges.add(start)
        else:
            raise IndexError("This vertex doesn't exist.")
    def add_directed_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.verticies(start).edges.add(end)
        else:
            raise IndexError("This vertex doesn't exist.")

class Node:
    def __init__(self):
        self.neighbors = []
    def addNeighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node) # O(1) - constant time
    def getNeighbor(self):
        return self.neighbors # O(1) - constant time
    def isNeighbor(self, node): 
       return node in self.neighbors # O(n) - linear time

    def dfs(self, start, target=None):
        # create a stack and visited list
        stack = [start]
        visited = set()
        # while there's a stack, pop the last item
        while stack:
            current_node = stack.pop()
            # if found, break
            if current_node == target:
                break
            # otherwise, add the current node to the list of visited notes
            visited.add(current_node)
            # add unvisited nodes to the queue
            stack.extend(self.vertices[current_node] - visited)
        # return visited
        return visited

    def bfs(self, start, target=None):
        # create a queue and visited list
        queue = [start]
        visited = set()
        # while there's a queue, pop the last item
        while len(queue) > 0:
            current_node = queue.pop(0)
            # if found, break
            if current_node == target:
                break
            # otherwise, add the current node to the list of visited notes
            visited.add(current_node)
            # add unvisited nodes to the queue
            queue.extend(self.vertices[current_node] - visited)
        # return visited
        return visited
        