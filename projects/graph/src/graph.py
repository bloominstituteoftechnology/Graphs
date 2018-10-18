"""
Simple graph implementation compatible with BokehGraph class.
"""

import random
from collections import defaultdict

# http://interactivepython.org/courselib/static/pythonds/Graphs/Implementation.html
# https://www.python.org/doc/essays/graphs/
# https://www.programiz.com/python-programming/methods/built-in/hash
# https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/

# the vertex class will create a single object with a key and an attached array of connections
    # vertex = {'A': ['B', 'C']}

# the Graph Class should create an object with vertices, each of which has a corresponding collection of neighbors
    # graph = {'A': ['B', 'C'],
    #          'B': ['C', 'D'],
    #          'C': ['D'],
    #          'D': ['C'],
    #          'E': ['F'],
    #          'F': ['C']}

class Queue: #FIFO
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack: #LIFO
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if (self.size()) > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Vertex:
    def __init__(self, id, x = None, y = None):
        # storage space for neighboring nodes
        self.id = id
        self.edges = set()
        # add a color property for the DFS 

        if x is None:
            self.x = random.random() * 10-5
        else:
            self.x = x

        if y is None:
            self.y = random.random() * 10-5
        else:
            self.y = y
    # method to retrieve the key associated with a vertex
    def __repr__(self):
        return f"{self.edges}"



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.vertCount = 0

    def add_vertex(self, vertex, edges = ()):
        if vertex in self.vertices:
        #  https://realpython.com/python-exceptions/            
            raise Exception('Error: that vertex already exists')
            # https://www.programiz.com/python-programming/methods/set/issubset
        if not set(edges).issubset(self.vertices):
            raise Exception('Error: that vertex does not exist')
            #https://docs.python.org/2/library/sets.html
        self.vertices[vertex] = set(edges)
    
    def get_vertex(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertices

    def add_edge(self, start, end, bothWays = True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('These vertices are not in the graph')
        self.vertices[start].add(end)
        if bothWays:
            self.vertices[end].add(start)

    def vertices(self):
        return self.vertices.keys()

    # Breadth First Traversal

    # def bft(self, starting_node):
    #     q = Queue() # use the Queue class to build an empty queue

    #     #initialize the queue with a starting node, using the enqueue method
    #     q.enqueue(starting_node)

    #     #set up an empty array to track visited vertices
    #     visited = []

    #     while q.size() > 0:
    #         # remove the first node from the queue
    #         # if it has not been visited, 
    #         # mark it as visited
    #         # but the child nodes in the back of the queue


    def BFS(self, start, target):
    # https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
        # mark all of the vertices as not visited
        visited = []
        # create a queue for BFS
        queue = Queue()
        # mark the source node as visited and enqueue
        queue.enqueue(start)
        while queue.size() > 0: # when the queue is not empty
            # Dequeue a vertex from the queue and print it
            removed = queue.dequeue() # remove the first element from the queue
            visited.append(removed) # mark the removed node as visited
            print(removed)
            if removed == target:
                return True
            # Get all adjacent vertices of the dequeued vertex.  If adjacent has not been visited, then mark it visited and enqueue it
            for i in self.vertices[removed].edges: # for each child node
                if i not in visited: # if the node has not been visited
                    queue.enqueue(i) # place the node in the back of the queue
        return False


# Tests for Graph Class
graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('1', '2')
graph.add_edge('1', '4')
print(graph.vertices)
print(graph.vertices['0'])
graph.BFS(0,2)


