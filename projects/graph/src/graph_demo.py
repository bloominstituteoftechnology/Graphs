#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

import random
from sys import argv
from draw import BokehGraph
from graph import Graph, Vertex

def createDefaultGraph():
    graph = Graph()  # Instantiate your graph
    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_vertex('4')
    # graph.add_vertex('5')
    # graph.add_vertex('6')
    # graph.add_edge('0', '1')
    # graph.add_edge('2', '3')
    # graph.add_edge('2', '4')
    # graph.add_edge('3', '5')
    # graph.add_edge('5', '6')

    graph.add_vertex(5)
    graph.add_vertex(2)
    graph.add_vertex(6)
    graph.add_vertex(1)
    graph.add_vertex(4)
    graph.add_vertex(7)
    graph.add_vertex(3)
    graph.add_edge(5, 2)
    graph.add_edge(5, 6)
    graph.add_edge(2, 1)
    graph.add_edge(2, 4)
    graph.add_edge(4, 3)
    graph.add_edge(6, 7)

    print(graph.dfs_path(5, 7))

    bg = BokehGraph(graph)
  #  print(graph.bfs(5))
    bg.draw()

#def main(num_vertices=8, num_edges=8, draw_components=True):
"""Build and show random graph.
"""
def createRandomGraph(numNodes, numEdges):

    graph = Graph()

    all_edges = []

    for i in range(numNodes):
        for j in range(i + 1, numNodes):
            all_edges.append( (i,  j) )
        
    random.shuffle(all_edges(i))
    edges = all_edges[:numEdges]

    if numEdges > len(all_edges):
        print("Warning: Too many edges")

    # for edge in edges:
        # print(edge)

    # Add appropriate number of vertices

    for num in range(numNodes):
    # for num in range(num_vertices):
        # graph.add_vertex(Vertex(label=str(num)))
        graph.add_vertex(num)
    # Add random edges between vertices
    #for _ in range(num_edges):

    for edge in edges:
        # print(edge)
        graph.add_edge(edge[0], edge[1])

       # vertices = sample(graph.vertices.keys(), 2)
        # TODO check if edge already exists
        # rand_vert = int(random.random() * num_vertices)
        # rand_edge = int(random.random() * num_edges)
        # print(rand_vert, rand_edge)
        # graph.add_edge(vertices[0], vertices[1])

    # bokeh_graph = BokehGraph(graph, draw_components=draw_components)
    # bokeh_graph._get_connected_component_colors()
    # bokeh_graph.show()
    bg = BokehGraph(graph)
    bg.draw()

# if __name__ == '__main__':
#     # TODO - parse argv
#     if len(argv) == 4:
#         NUM_VERTICES = int(argv[1])
#         print(NUM_VERTICES)
#         NUM_EDGES = int(argv[2])
#         DRAW_COMPONENTS = bool(int(argv[3]))
#         #main(NUM_VERTICES, NUM_EDGES, DRAW_COMPONENTS)
#     else:
#         main()

def main(style, numNodes,  numEdges):
    if style  == "default":
        createDefaultGraph()
    elif style  == "random":
        createRandomGraph(numNodes, numEdges)
    else:
        createDefaultGraph()




if __name__ == '__main__':
    style = "default"
    numNodes = 20
    numEdges = 20

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
                print("I don't understand that command.\n")

    main(style, numNodes, numEdges)
        # print('Expected arguments: num_vertices num_edges draw_components')
        # print('Both numbers should be integers, draw_components should be 0/1')
