#!/usr/bin/python
from draw import BokehGraph
from random import sample
from sys import argv
from graph import *

"""
Simple graph implementation compatible with BokehGraph class.
"""

class Vertex:
    def __init__(self, label, color='white'):
        self.label = str(label)
        self.component = component
    
    def __repr__(self):
        return 'Vertex: ' + self.label

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
    # TODO
        self.vertices = {}
        self.components = 0

    def add_edge(self, start, end, bidirectional=True):
        if start not in self.vertices or end not in self.vertices:
            raise Exception("Start and or end doesn't exist here")
        else:
            self.vertices[start].add(end)
            if bidirectional == True:
                self.vertices[end].add(start)

    def add_vertex(self, vertex, edges=()):
        if vertex not in self.vertices:
            self.vertices[vertex] = set(edges)
        else:
            raise ValueError("that vertex already exists")

    # def bfs(self, start, target=None):
    #     queue = [start]
    #     visited = set()

    #     while queue:
    #         current = queue.pop(0)
    #         if current == target:
    #             break
    #         visited.add(current)
    #         queue.extend(self.vertices[current] - visited)
    #     return visited
    
    # def(self, start, target=None)
    #     stack = [start]
    #     visited = set()

    #     while stack:
    #         current = stack.pop()
    #         if current == target:
    #             break
    #         visited.add(current)
    #         stack.extend(self.vertices[current] - visited)
    #     return visited
    
    def search(self, start, target=None, method='dfs')
        quack = [start]
        pop_index = 0 if method == 'bfs' else -1
        visited = set()

        while quack:
            current = quack.pop(pop_index)
            if current == target:
                break
            visited.add(current)
            quack.extend(self.vertices[current] - visited)
        return visited
    
    def find_components(self):
        visited = set()
        
        for vertex in self.vertices:
            if vertex not in visited:
                reachable = self.search(vertex)
                for other_vertex in reachable:
                    other_vertex.component = current_component
                current_component += 1
                visited.update(reachable)
        self.components = current_component

def main():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')
    graph.add_vertex('H')
    graph.add_edge('B', 'C')
    graph.add_edge('A', 'H')
    graph.add_edge('D', 'G')

    bg = BokehGraph(graph)
    bg.show()

if __name__ == "__main__":
    main()
