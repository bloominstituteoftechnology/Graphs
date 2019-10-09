#!/usr/bin/env python
from typing import Tuple, Set, Dict

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size > 0:
            return self.queue.pop(0)
        else:
            return None

    @property
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, v: int):
        self.vertices[v] = set()

    def add_edge(self, tail: int, head: int):


        if tail==head:
            print("do not add edge to yourself")
        else:
            self.vertices[tail].add(head)
            self.vertices[head].add(tail)
        pass

    @property
    def connected_components(self) -> int:
        """ get number of connected components """
        # visited = set()
        def get_component(vert: Tuple[int, int]) -> Set[Tuple[int, int]]:
            """ """
            nonlocal visited
            visited.add(vert)
            if graph.vertices[vert]:
                for neighbor in graph.vertices[vert]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        neighbor_components = get_component(neighbor)
                        visited = visited.union(neighbor_components)
                    else:
                        continue

                return visited
            else:
                return visited

        components = list()
        for vertex in graph.vertices.keys():
            visited = set()
            component = get_component(vertex)
            if component not in components:
                components.append(component)
            else:
                continue
           
        return len(components)

if __name__=='__main__':

    islands = [[0, 1, 0, 1, 0],
               [1, 1, 0, 1, 1],
               [0, 0, 1, 0, 0],
               [1, 0, 1, 0, 0],
               [1, 1, 0, 0, 0]]

    islands = [
        [1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    ]

    n = len(islands)
    m = len(islands[0])

    graph = Graph()

    # load in vertices
    for i in range(n):
        for j in range(m):
            if islands[i][j]==1:
                graph.add_vertex((i,j))
    # load in edges
    for (i,j) in graph.vertices.keys():
        for (k,l) in graph.vertices.keys():
            A = abs(i-k)==1 and j==l
            B = abs(j-l)==1 and i==k
            if A or B:
                graph.add_edge((i,j), (k,l))

    # num of connected cmponetns

    for vertex, vertices in graph.vertices.items():
        print(vertex, vertices)

    print(f"number of connected components: {graph.connected_components}")



        

    #print(len(graph.vertices))
    #print(len(graph.vertices[(0,1)]))
