"""
Simple graph implementation compatible with BokehGraph class.
"""

import random

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack =[]
    def push(self, value):
        self.queue.append(value)
    def pop(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len

"""Represent a graph as a dictionary of vertices mapping labels to edges."""

class Graph:
    def __init__(self):
        """create an empty dictionary for the vertices"""
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """add a vertex to the graph"""
        self.vertices[vertex_id] = Vertex(vertex_id)

    def add_edge(self, v1, v2):
        """add an undirected edge to the graph"""
        if v1 in self.vertices or v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist!")

    def add_directed_edge(self, v1, v2):
        """ add an edge to the graph"""
        if v1 in self.vertices:
            self.vertices[v1].edges.add(v2)
        else:
            raise IndexError("That vertex does not exist!")
#DFT using recursion
    def dft(self, starting_node, visited=None):
        """Mark the node as visited"""
        if visited is None: #cant just have visited = [] in def dft because of weird python thing
            visited = []  # queue of visited nodes
        visited.append(starting_node)
    """For each child, if that child hasnt been visited, call dft() on that node
        for child in children:
            if child not in visited:
                dft (child,visited)"""
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                self.dft(node, visited)
        return visited


#you can implement dfs using stack instead of recursion
#and for bfs if you use queue instead of stack it changes dfs to bfs

    def bft(self, starting_node):
        visited=[]
        """create an empty queue"""
        q = Queue()
        """put starting vert in the queue"""
        q.enqueue(starting_node)
        while q.size() > 0: # while queue is not empty...
            dequeued = q.dequeue() #dequeue the first element
            visited.append(dequeued)
            print(dequeued)
            for edge in self.vertices[dequeued].edges:
                if edge not in visited:
                    q.enqueue(edge) #add it back to the queue
            return visited
            """ remove the first node from the queue...
            If it has not been visited yet...
            Mark it as visited...
            then put all its children in the back of the queue"""


    def dft_s(self, starting_node): #dft as a stack
        visited=[]
        """create an empty stack"""
        s = Stack()
        """put starting vert on top of the stack"""
        s.push(starting_node)
        while s.size() > 0: # while  stack is not empty...
            current = s.pop() #pop the first element
        if current not in visited:
            visited.append(current)
            print(visited)
            for edge in self.vertices[current].edges:#for each child
                    s.push(edge) #add it to the top of the stack


    def bfs(self, starting_node, target_node):
        visited = []
        # create an empty queue
        q = Queue()
        q.enqueue(starting_node)
        while q.size() > 0:
            dequeued = q.dequeue()
            visited.append(dequeued)
            for edge in self.vertices[dequeued].edges:
                if edge not in visited:
                    q.enqueue(edge)
        return False

    def dfs(self, starting_node, target_node, visited=None):
        #Mark the node as visited
        if visited is None:
            #queue of visited nodes
            visited =[]
        visited.append(starting_node)
        if starting_node ==target_node:
            return True
        #for each child, if that child hasnt been visited, call dft() on that node
        for node in self.vertices[starting_node].edges:
            if node not in visited:
                if self.dfs(node,target_node,visited):
                    return True
        return False



class Vertex:
    def __init__(self, vertex_id, x=None, y=None):
        """ Create an empty vertex"""
        self.id = vertex_id
        self.edges = set()
        if x is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = x
        if y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = y

    def __repr__(self):
        return f"{self.edges}"