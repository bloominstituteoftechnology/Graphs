from collections import deque

"""
Simple graph implementation
"""


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    Adjacency List!
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        if edge in self.vertices and vertex in self.vertices:
            self.vertices[vertex].add(edge)
        else:
            raise IndexError("That vertex does not exist")

    # Breadth First Traversal

    def bft(self, starting_vert):
        queue = deque()
        visited = set()
        queue.append(starting_vert)
        # Print
        print("BFT NODES VISITED:")
        while queue:
            dequeued = queue.popleft()
            if dequeued not in visited:
                visited.add(dequeued)
                print(dequeued)
                # -> enqueue all of it's children
                for vert in self.vertices[dequeued]:
                    # if vert not in visited:
                    queue.append(vert)
        return visited

    # Depth First Traversal

    def dft(self, starting_vert):
        stack = deque()
        visited = set()
        stack.append(starting_vert)
        # Print
        print("DFT NODES VISITED:")
        while stack:
            popped = stack.pop()
            if popped not in visited:
                visited.add(popped)
                print(popped)
                for vert in self.vertices[popped]:
                    # if vert not in visited:
                    stack.append(vert)
        return visited

    def dft_rec(self, starting_vert, visited=None):
        # create visited
        if visited is None:
            visited = set()
        # Mark the node as visited
        if starting_vert not in visited:
            visited.add(starting_vert)
            print(starting_vert)
            # If the node has not been visited
            for vert in self.vertices[starting_vert]:
                # if vert not in visited:
                self.dft_rec(vert, visited)

    # Breadth First Search
    '''
    q = [ node 4]
    visited = {}

    duplicate list list()
    append children and add to queue
    '''

    def bfs(self, starting_vert, target_vert):
        queue = deque()
        visited = set()
        path = []
        queue.append(list(starting_vert))
        # while queue is not empty
        while queue:
            # -> dequeue a vert from queue
            dequeued = queue.popleft()
            # -> mark it as visited
            if dequeued[-1] not in visited:
                # check if target vert
                if dequeued[-1] == target_vert:
                    path = dequeued
                    return path
                visited.add(dequeued[-1])
                # -> enqueue all of it's children
                for vert in self.vertices[dequeued[-1]]:
                    path_copy = list(dequeued)
                    path_copy.append(vert)
                    queue.append(path_copy)

        return False

    def dfs(self, starting_vert):
        stack = deque()
        visited = set()
        stack.append(starting_vert)
        # Print
        print("DFT NODES VISITED:")
        while stack:
            popped = stack.pop()
            if popped not in visited:
                # check if target vert
                if popped == target_vert:
                    return True
                print(popped)
                visited.add(popped)
                for vert in self.vertices[popped]:
                    # if vert not in visited:
                    stack.append(vert)
        return visited
