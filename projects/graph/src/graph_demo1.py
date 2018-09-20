
#!/usr/bin/python

"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv
from draw2 import BokehGraph
from graph3 import Graph
import random

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
                allEdges.append((i, j))
    # O(n)
    random.shuffle(allEdges)
    # O(1)
    randomEdges = allEdges[:numEdges]
    # O(n^2)
    for edge in randomEdges:
        graph.add_edge(edge[0], edge[1])
    
    return graph

    return graph

def main(**kwargs):
    print(kwargs) # *kwargs vs **kwargs (tuple vs dict)

    style = kwargs['style']
    numVerts = kwargs['num_verts']
    numEdges = kwargs['num_edges']

    graph = Graph()  # Instantiate your graph
    if style == 'default':
        graph = getDefaultGraph()
    elif style == 'random':
        graph = getRandomGraph(numVerts, numEdges)
    else:
        graph = getDefaultGraph()

    # graph.dft(0)
    # print(graph.dfs(0, 4))
    # print(graph.dfs(0, 9))
    # print(graph.bfs(0, 4))
    # print(graph.bfs(0, 8))
    # print(graph.dfs_path(0, 1))
    # print(graph.dfs_path(0, 2))
    # print(graph.dfs_path(0, 3))
    # print(graph.dfs_path(0, 4))
    # print(graph.dfs_path(0, 5))
    # print(graph.dfs_path(0, 6))
    # print(graph.dfs_path(0, 7))
    # print(graph.dfs_path(0, 8))
    print(graph.bfs_path(0, 5))
    # graph.dft_stack(0)
    # graph.bft(4)

    bokeh_graph = BokehGraph(graph)

    bokeh_graph.draw()

if __name__ == '__main__':
    # TODO - parse argv
    # passing custom style
    print(argv)
    style='default'
    num_verts = 5
    num_edges = 6

    for arg in argv[1:]:
        arg_split = arg.split('=')
        if len(arg_split) == 2:
            if arg_split[0] == 'style':
                style = arg_split[1].lower()
            elif arg_split[0] == 'verts':
                num_verts = int(arg_split[1])
            elif arg_split[0] == 'edges':
                num_edges = int(arg_split[1])
            
    
    print(style)

    main(style=style, num_verts=num_verts, num_edges=num_edges)
