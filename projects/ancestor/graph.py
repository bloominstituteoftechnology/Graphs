"""
Simple graph implementation
"""
from util import Stack

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist.")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            v = stack.pop()

            if v not in visited:
                visited.add(v)

                for next_vertex in self.get_neighbors(v):
                    stack.push(next_vertex)
        
        last = visited.pop()
        return last

    def dfs(self, starting_vertex, destination_vertex):
        # Create an empty Stack and Push PATH to the Starting Vertex
        stack = Stack()
        stack.push([starting_vertex])

        # Create a set to store visited vertices
        visited = set()

        # While stack is not empty:
        while stack.size() > 0:

            # Pop the first PATH
            path = stack.pop()

            # Grab the last vertex from the PATH
            last_vertex = path[-1]

            # Check if the vertex has not been visited:
            if last_vertex not in visited:

                # Is this vertex the target?
                if last_vertex == destination_vertex:

                    # If it is, return the PATH
                    return path
                
                else:
                    # Mark the vertex as visited
                    visited.add(last_vertex)

                    # Then add a PATH to its neighbors on top of the stack
                    for neighbor in self.get_neighbors(last_vertex):

                        # Make a copy of the PATH
                        newPath = path.copy()

                        # Append the neighbor to the back of the PATH
                        newPath.append(neighbor)

                        # Push out new Path
                        stack.push(newPath)
        return None

    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue and enqueue PATH to the Starting Vertex ID
        queue = Queue()
        queue.enqueue([starting_vertex]) # Enqueue PATH by making SV a List

        # Create a set to store visited vertices
        visited = set()

        # While the queue is not empty:
        while queue.size() > 0:

            # Dequeue the first PATH
            path = queue.dequeue()

            # Grab the last vertex from the PATH
            last_vertex = path[-1]

            # Check if the vertex has not been visited:
            if last_vertex not in visited:

                # Is this the vertex the target?
                if last_vertex == destination_vertex:

                    # If it is, return the PATH
                    return path

                else:
                    # Mark the vertex as visited
                    visited.add(last_vertex)

                    # Then add a PATH to its neighbors to the back of the queue
                    for neighbor in self.get_neighbors(last_vertex):

                        # Make a copy of the PATH
                        newPath = path.copy() # list(path) or [path] Many dif ways

                        # Append the neighbor to the back of the PATH
                        newPath.append(neighbor)

                        # Enqueue out new PATH
                        queue.enqueue(newPath)
        return None