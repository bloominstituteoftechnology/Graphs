#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""
import sys
from graph import Graph
from draw import BokehGraph
from random import randint


def main(vertices=8, edges=8):
    graph = Graph()
    vertices = vertices
    edges = edges

    for n in range(0, vertices):
        graph.add_vertex(n)

    edgesOut = []
    while len(edgesOut) < edges:
        starting = randint(0, vertices - 1)
        ending = randint(0, vertices - 1)
        if starting != ending and (starting, ending) \
                not in edgesOut and (ending, starting) not in edgesOut:
            edgesOut.append((starting, ending))
    print("Edges Out:", edgesOut)
    for edge in edgesOut:
        graph.add_edge(edge[0], edge[1])

    print('NI: ', graph.vertices)
    # start with array of ALL NODES
    # loop through each node and get visited
        # Assign color
    # remove all visited nodes from ALL NODES
    # repeat until done
    
    vertices = list(graph.vertices.keys())[:]
    while vertices:
        group = graph.breadth_first_for_each(vertices[0]) #==> this is visited
        vertices = [i for i in vertices if i not in group]
        graph.groups.append(group)
        print(vertices)
    print(graph.groups)
    print([vertex for subgroup in graph.groups for vertex in subgroup])    
    b_graph = BokehGraph(graph)

    print('visited: ', graph.breadth_first_for_each(0))
    
    print(graph.groups)
    b_graph.show()


if __name__ == '__main__':
    vertices, edges = int(sys.argv[1]), int(sys.argv[2])
    max_edges = 0
    for num in range(vertices):
        max_edges += num
    if edges > max_edges:
        print("Maximum number of edges exceeded!")
    else:
        main(vertices, edges)

        # i.color for i in self.vertices:
        #     if i in visited:
        #         currentcolor = color1
        #     else:
        #         currentcolor = color2
