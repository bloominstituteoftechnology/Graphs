"""
Simple graph implementation
"""

from collections import deque

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # add a dictionary of vertices
        self.vertices = {}
    # placeholders for add_vertex and add_edge methods
    # add_vertex needs only a vertex, while add_edge needs both a vertex and edge
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex, edge):
        if vertex in self.vertices:
            self.vertices[vertex].add(edge)
        elif vertex not in self.vertices:
            raise Exception(f'There is no edge to vertex {vertex}! Please try again.') # will revisit this

    # breadth-first traversal method
    def bft(self, start):
        x = deque()
        visited = []
        x.append(start)

        """
        popleft() covers what we need to do for breadth-first, we keep moving along the same level
        the visited node is added to the 'visited' list
        if after the breadth-wide search a node has an unvisited child, we append the child to the list as well
        """

        while len(x) > 0:
            node = x.popleft()
            visited.append(node)
            for child in node:
                if child not in visited:
                    x.append(child)
        return visited

# testing

graph = Graph() 
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
# test case for exception
# graph.add_edge('0', '4') # should cause an error
print(graph.bft(graph.vertices['0']))