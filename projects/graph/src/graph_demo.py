# #!/usr/bin/python

# """
# Demonstration of Graph and BokehGraph functionality.
# """

# from sys import argv
# from graph import Graph
# from draw import BokehGraph
# import random


# def createDefaultGraph():
#     graph = Graph()  # Instantiate your graph
#     graph.add_vertex(5)
#     graph.add_vertex(2)
#     graph.add_vertex(6)
#     graph.add_vertex(1)
#     graph.add_vertex(4)
#     graph.add_vertex(7)
#     graph.add_vertex(3)
#     graph.add_edge(5, 2)
#     graph.add_edge(5, 6)
#     graph.add_edge(2, 1)
#     graph.add_edge(2, 4)
#     graph.add_edge(4, 3)
#     graph.add_edge(6, 7)

#     print(graph.dfs(5, 7))

#     # bg = BokehGraph(graph)
#     # bg.draw()


# # O(n^2)
# def createRandomGraph(numNodes, numEdges):
#     graph = Graph()  # Instantiate your graph

#     all_edges = []

#     # O(n^2)
#     for i in range(numNodes):
#         for j in range(i + 1, numNodes):
#             all_edges.append( (i,  j) )

#     # O(n)
#     random.shuffle(all_edges)
#     edges = all_edges[:numEdges]

#     # O(1)
#     if numEdges > len(all_edges):
#         print("Warning: Too many edges")

#     # O(n)
#     for edge in edges:
#         print(edge)

#     # O(n)
#     for i in range(numNodes):
#         graph.add_vertex(i)

#     # O(n)
#     for edge in edges:
#         print(edge)
#         graph.add_edge(edge[0], edge[1])

#     print(len(edges))

#     bg = BokehGraph(graph)
#     bg.draw()


# def main(style, numNodes,  numEdges):
#     if style  == "default":
#         createDefaultGraph()
#     elif style  == "random":
#         createRandomGraph(numNodes, numEdges)
#     else:
#         createDefaultGraph()


# if __name__ == '__main__':
#     style = "default"
#     numNodes = 5
#     numEdges = 5

#     for arg in argv[1:]:
#         arg_split = arg.split("=")
#         if len(arg_split) == 2:
#             if arg_split[0] == "style":
#                 style = arg_split[1].lower()
#             elif arg_split[0] == "nodes":
#                 numNodes = int(arg_split[1])
#             elif arg_split[0] == "edges":
#                 numEdges = int(arg_split[1])
#             else:
#                 print("I don't understand that command.\n")

#     main(style, numNodes, numEdges)

######################################################
######################################################
from random import sample
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex


def main(num_vertices=8, num_edges=8, draw_components=True):
    graph = Graph()

    for num in range(num_vertices):
        graph.add_vertex(Vertex(label=str(num)))

    for _ in range(num_edges):
        vertices = sample(graph.vertices.keys(), 2)
        graph.add_edge(vertices[0], vertices[1])

    bokeh_graph = BokehGraph(grahp, draw_components=draw_components)
    bokeh_graph.show()


if __name__ == "__main__":
    if len(argv) == 4:
        NUM_VERTICES = int(argv[1])
        NUM_EDGES = int(argv[2])
        DRAW_COMPONENTS = bool(int(argv[3]))
        main(NUM_VERTICES, NUM_EDGE, DRAW_COMPONENTS)
    else:
        print("Expected arguments: num_vertices num_edges draw_components")
        print("Both numbers should be integers, draw_components should be 0/1")
