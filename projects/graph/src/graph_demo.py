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

    b_graph = BokehGraph(graph)

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
