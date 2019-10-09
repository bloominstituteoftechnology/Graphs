#!/usr/bin/env python
from operator import xor

class Graph:
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, v: int):
        self.vertices[v] = set()

    def add_edge(self, tail: int, head: int):

        self.vertices[tail].add(head)
        self.vertices[head].add(tail)
        pass

if __name__=='__main__':

    islands = [[0, 1, 0, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0],
               [1, 1, 0, 0, 0]]

    n = len(islands)
    m = len(islands[0])

    graph = Graph()
   
    for i in range(n):
        for j in range(m):
            if islands[i][j]==1:
                graph.add_vertex((i,j))

    for (i,j) in graph.vertices.keys():
        for (k,l) in graph.vertices.keys():
            A = abs(i-k)==1
            B = abs(j-l)==1
            if xor(A, B):
                graph.add_edge((i,j), (k,l))

    for vertex, vertices in graph.vertices.items():
        print(vertex, vertices)

    #print(len(graph.vertices))
    #print(len(graph.vertices[(0,1)]))
