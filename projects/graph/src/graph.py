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

    # Depth First Traversal with Recursion
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
    def bfs(self, starting_vert, target_vert):
        queue = deque()
        visited = set()
        queue.append(list(starting_vert))
        while queue:
            # -> dequeue a list from queue
            dequeued_list = queue.popleft()
            path_end = dequeued_list[-1]
            # -> mark it as visited
            if path_end not in visited:
                # check if target vert == last item in list
                if path_end == target_vert:
                    return dequeued_list
                visited.add(path_end)
                # -> enqueue all of it's children
                for vert in self.vertices[path_end]:
                    path_copy = list(dequeued_list)
                    path_copy.append(vert)
                    queue.append(path_copy)

        return f"There is no path from {starting_vert} to {target_vert}"

    # Deptg First Search
    def dfs(self, starting_vert, target_vert):
        stack = deque()
        visited = set()
        stack.append(list(starting_vert))
        while stack:
            # -> pop a list from stack
            popped_list = stack.pop()
            path_end = popped_list[-1]
            # -> mark it as visited
            if path_end not in visited:
                # check if target vert == last item in list
                if path_end == target_vert:
                    return popped_list
                visited.add(path_end)
                # stack all of it's children
                for vert in self.vertices[path_end]:
                    path_copy = list(popped_list)
                    path_copy.append(vert)
                    stack.append(path_copy)

        return f"There is no path from {starting_vert} to {target_vert}"
