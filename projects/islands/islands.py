#!/usr/bin/env python
from typing import Tuple, Set, List

class Graph:
    """ undirected graph with counter of its connected components. """
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, v: Tuple[int, int]):
        """ add vertex. """
        self.vertices[v] = set()

    def add_edge(self, tail: Tuple[int, int], head: Tuple[int, int]):
        """ bidirectional add edge for undirected graph. """
        assert tail in self.vertices.keys(), "passed in tail is not a vertex yet"
        assert head in self.vertices.keys(), "passed in head is not a vertex yet"

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

        components: List[Set[Tuple[int, int]]] = list()
        for vertex in graph.vertices.keys():
            visited: Set[Tuple[int, int]] = set()
            component = get_component(vertex)
            if component not in components:
                components.append(component)
            else:
                continue
           
        return len(components)

if __name__=='__main__':

#   islands = [[0, 1, 0, 1, 0],
#              [1, 1, 0, 1, 1],
#              [0, 0, 1, 0, 0],
#              [1, 0, 1, 0, 0],
#              [1, 1, 0, 0, 0]]
#
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

#   for vertex, vertices in graph.vertices.items():
#       print(vertex, vertices)

    print(f"number of connected components: {graph.connected_components}") # should be 13



        

    #print(len(graph.vertices))
    #print(len(graph.vertices[(0,1)]))
