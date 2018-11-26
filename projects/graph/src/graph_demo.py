import random
from sys import argv
from graph import Graph
from draw import BokehGraph

# !/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""


def createDefaultGraph():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex('0')
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('1', '2')
    graph.add_edge('3', '2')

    bg = BokehGraph(graph)
    bg.draw()
    print(graph.vertices)

# O(n^2)
def createRandomGraph(numnodes, num):
    graph = Graph()

    all_edges = []
    # O(n^2)
    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            """
            Append every subsequent pair of nodes into
            all_edges  as a tuple making an edge for each new node
            thus making a dense graph of maximal edges predicted by
            n(n-1)/2
            """
            all_edges.append((i, j))
    # randomnize the edges
    # O(n)
    random.shuffle(all_edges)
    # edges is the array of all edges (which are tuples)
    # that do not exceeed the specifiied user input
    edges = all_edges[:numEdges]
    # O(1)
    if numEdges > len(all_edges):
        print("Too many edges")
    # O(n)
    for edge in edges:
        print(edge)
    # O(n)
    for i in range(numNodes):
        graph.add_vertex(i)
    # O(n)
    for edge in edges:
        print(edge)
        graph.add_edge(edge[0], edge[1])

    print(len(edges))

    bg = BokehGraph(graph)
    bg.draw()


def main(style, numNodes, numEdges):
    # numNodes, numEdges will be  system inputs
    if style == "default":
        createDefaultGraph()
    elif style == "random":
        createRandomGraph(numNodes, numEdges)
    else:
        createDefaultGraph()


if __name__ == '__main__':
    # Default, if run with no inputs.
    style = "default"
    numNodes = 5
    numEdges = 5

    # look at second part of argv onwards
    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "nodes":
                numNodes = int(arg_split[1])
            elif arg_split[0] == "edges":
                numEdges = int(arg_split[1])
            else:
                print("Invalid input.")

    main(style, numNodes, numEdges)


# After Hours with Kelly
# def main(v=7, e=7):
#     graph = Graph()
#     for i in range(v):
#         graph.add_vertex(i)
#     for j in range(e):
#         random_vertex = int(random.random() * v)
#         random_edge = int(random.random() * e)
#         graph.add_edge(random_vertex, random_edge)
#     bg = BokehGraph(graph)
#     bg.draw()
#     print(graph.vertices)
#
#
# if __name__ == '__main__':
#     if len(argv) == 3:
#         v = argv[1]
#         e = argv[2]
#         main(int(v).int(e))
#     else:
#         main()
