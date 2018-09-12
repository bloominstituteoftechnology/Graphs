#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from graph import Graph
from draw import BokehGraph
import random

# def getDefaultGraph():
#     myGraph = BokehGraph2()
#     myGraph.graph.add_vertex(0)
#     myGraph.graph.add_vertex(1)
#     myGraph.graph.add_vertex(2)
#     myGraph.graph.add_vertex(3)
#     myGraph.graph.add_vertex(4)
#     myGraph.graph.add_vertex(5)
#     myGraph.graph.add_vertex(6)
#     myGraph.graph.add_vertex(7)
#     myGraph.graph.add_vertex(8)
#     myGraph.graph.add_vertex(9)
#     myGraph.graph.add_vertex(10)
#     myGraph.graph.add_vertex(11)
#     myGraph.graph.add_vertex(12)
#     myGraph.graph.add_vertex(13)
#     myGraph.graph.add_vertex(14)
#     myGraph.graph.add_vertex(15)
#     myGraph.graph.add_vertex(16)
#     myGraph.graph.add_vertex(17)
#     myGraph.graph.add_vertex(18)
#     myGraph.graph.add_vertex(19)
#     myGraph.graph.add_vertex(20)
#     myGraph.graph.add_vertex(21)
#     myGraph.graph.add_vertex(22)
#     myGraph.graph.add_vertex(23)
#     myGraph.graph.add_vertex(24)
#     myGraph.graph.add_vertex(25)
#     myGraph.graph.add_vertex(26)
#     myGraph.graph.add_vertex(27)
#     myGraph.graph.add_edge(0, 1)
#     myGraph.graph.add_edge(0, 5)
#     myGraph.graph.add_edge(2, 4)
#     myGraph.graph.add_edge(3, 7)
#     myGraph.graph.add_edge(2, 6)
#     myGraph.graph.add_edge(6, 9)
#     myGraph.graph.add_edge(5, 8)
#     myGraph.graph.add_edge(7, 11)
#     myGraph.graph.add_edge(8, 13)
#     myGraph.graph.add_edge(10, 11)
#     myGraph.graph.add_edge(10, 13)
#     myGraph.graph.add_edge(11, 14)
#     myGraph.graph.add_edge(12, 16)
#     myGraph.graph.add_edge(13, 17)
#     myGraph.graph.add_edge(14, 15)
#     myGraph.graph.add_edge(15, 19)
#     myGraph.graph.add_edge(16, 17)
#     myGraph.graph.add_edge(17, 18)
#     myGraph.graph.add_edge(17, 20)
#     myGraph.graph.add_edge(17, 22)
#     myGraph.graph.add_edge(18, 21)
#     myGraph.graph.add_edge(20, 27)
#     myGraph.graph.add_edge(21, 24)
#     myGraph.graph.add_edge(22, 27)
#     myGraph.graph.add_edge(23, 26)
#     myGraph.graph.add_edge(24, 25)
#     myGraph.graph.add_edge(25, 26)
#     return myGraph

# from sys import argv
# from graph import Graph
# from draw import BokehGraph
# import random

def getDefaultGraph():
    graph = Graph()  # Instantiate your graph
    graph.add_vertex(0)
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)

    graph.add_edge(1, 2)
    graph.add_edge(2, 5)
    graph.add_edge(2, 4)
    graph.add_edge(4, 9)
    graph.add_edge(3, 7)
    graph.add_edge(3, 6)

    return graph

    # O(n^2)
def getRandomGraph(numVerts, numEdges):
    graph = Graph()  # Instantiate your graph

    # O(n)
    for vert_id in range(0, numVerts):
        graph.add_vertex(vert_id)

    allEdges = []
    # O(n^2)
    for i in range(0, numVerts):
        for j in range(0, numVerts):
            if i < j:
                allEdges.append( (i, j) )
    # O(n)
    random.shuffle(allEdges)
    # O(1)
    randomEdges = allEdges[:numEdges]
    # O(n^2)
    for edge in randomEdges:
        graph.add_edge(edge[0], edge[1])

    return graph


def main(**kwargs):
    style = kwargs["style"]
    numVerts = kwargs["num_verts"]
    numEdges = kwargs["num_edges"]

    if style == "default":
        graph = getDefaultGraph()
    elif style == "random":
        graph = getRandomGraph(numVerts, numEdges)
    else:
        graph = getDefaultGraph()

    bokeh_graph = BokehGraph(graph)

    bokeh_graph.draw()

if __name__ == '__main__':

    style="default"
    num_verts = 5
    num_edges = 6

    for arg in argv[1:]:
        arg_split = arg.split("=")
        if len(arg_split) == 2:
            if arg_split[0] == "style":
                style = arg_split[1].lower()
            elif arg_split[0] == "verts":
                num_verts = int(arg_split[1])
            elif arg_split[0] == "edges":
                num_edges = int(arg_split[1])

    main(style=style, num_verts=num_verts, num_edges=num_edges)

################################################################

# def main(**kwargs):
#     style = kwargs["style"]
#     numVerts = kwargs["num_verts"]
#     numEdges = kwargs["num_edges"]

#     if style == "default":
#         graph = getDefaultGraph()
#     elif style == "random":
#         graph = getRandomGraph(numVerts,numEdges)
#     else:
#         graph = getDefaultGraph()
    
#     bokeh_graph = BokehGraph2(graph)
#     bokeh_graph.draw()

# if __name__ == '__main__':
#     style="default"
#     num_verts = 5
#     num_edges = 6

#     for arg in argv[1:]:
#         arg_split=arg.split("=")
#         if len(arg_split) == 2:
#             if arg_split[0] == "style":
#                 style = arg_split[1].lower()
#             elif arg_split[0] == "verts":
#                 num_verts = int(arg_split[1])
#             elif arg_split[0] == "edges":
#                 num_edges = int(arg_split[1])

#     main(style=style, num_verts=num_verts, num_edges=num_edges)

# def main(max_vertices):
#     # graph = Graph()
#     graph = BokehGraph()
#     count_vertices = random.randint(1,max_vertices)
#     count_edges = (count_vertices)*(count_vertices-1)//2
#     print(f"Verts:{count_vertices}, Maximum possible edges: {count_edges}")
    
#     current_vertex = 0

#     while count_vertices > 0:
#         graph.add_vertex(str(current_vertex))
#         current_vertex += 1
#         count_vertices -= 1
    
#     if count_vertices == 0:
#         print(graph.vertices)
    
#     while count_vertices == 0 and count_edges > 0:
#         graph.add_edge(random.randint(0,current_vertex), random.randint(0,current_vertex-1))
#         count_edges -= 1
    
#     if count_vertices == 0 and count_edges == 0:
#         return graph