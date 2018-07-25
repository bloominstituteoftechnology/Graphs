#!/usr/bin/python

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    def __init__(self):
        self.vertices = dict()

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        self.vertices[start].add(end)
        if bidirectional:
            self.vertices[end].add(start)

    def add_vertex(self, vertex, edges=()):
        if not set(edges).issubset(self.vertices):
            raise Exception('Error no edges to nonexistent vertices')
        self.vertices[vertex] = set(edges)

    # def depth_first_search(self, start):
    #     visited, stack = set(), [start]
    #     while stack:
    #         vertex = stack.pop()
    #         if vertex not in visited:
    #             visited.add(vertex)
    #     current = start
    #     if self.vertices[current].keys() is search_value:

def main():
    graph = Graph()
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    print(graph.vertices)

if __name__ == "__main__":
    main()