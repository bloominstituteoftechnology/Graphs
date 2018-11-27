from queue import Queue
from vertex import Vertex

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        new_vertex = Vertex(value)
        self.vertices.update(new_vertex.value)

    def add_edge(self, vertex1, vertex2):
        # if both vertices exist
        if self.vertices.get(vertex1) != None and self.vertices.get(vertex2) != None:
            # connect each to the other
            self.vertices.get(vertex1).add(vertex2)
            self.vertices.get(vertex2).add(vertex1)
        else:
            # if both vertices do not exist, raise an Exception
            raise Exception('Nonexistent vertex.')

    def bfs(self, start_vertex):
        # create a queue
        queue = Queue()
        # create a visited list
        visited = []
        # put the start vertex in the queue
        queue.enqueue(start_vertex)
        # while queue is not empty...
        while queue.len() > 0:
            # remove vertex from queue
            vertex = queue.dequeue()
            # check if it's visited
            if vertex not in visited:
                # if not, mark vertex as visited
                visited.append(vertex)
                # then put all children in queue
                for child in self.vertices.get(vertex):
                    queue.enqueue(child)
        return visited

    def dfs(self, start_vertex):
        # create a stack (as a list)
        stack = []
        # create a visited list
        visited = []
        # put the start vertex in the stack
        stack.append(start_vertex)
        # while stack is not empty...
        while len(stack) > 0:
            # remove vertex from stack
            vertex = stack.pop()
            # check if it's visited
            if vertex not in visited:
                # if not, mark vertex as visited
                visited.append(vertex)
                # then put all children in stack
                for child in self.vertices.get(vertex):
                    stack.append(child)
        return visited


# # Testing implementation
# graph = Graph() # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# print('Graph:', graph.vertices)
# print('BFS:', graph.bfs('0'))
# print('DFS:', graph.dfs('0'))