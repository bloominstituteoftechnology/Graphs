import math
import random

# !/usr/bin/python
from graph import Graph
from draw import BokehGraph


"""
Demonstration of Graph and BokehGraph functionality.
"""

from sys import argv



def main():

    graph = Graph()
    for i in range(0,13):
        graph.add_vertex(i)
    # print(graph.vertices,'graph vertecies')
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 7)
    graph.add_edge(7, 10)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(2, 8)
    graph.add_edge(8, 9)
    graph.add_edge(8, 11)
    graph.add_edge(9, 5)
    graph.add_edge(5, 12)
    print('graph vertecies ->', graph.vertices)
    
    # BokehGraph(graph).show()
    
    # rando_graph = Graph()
    # verts = math.floor(random.random() * 15) + 2
    # for v1 in range(0, verts+1):
    #     rando_graph.add_vertex(v1)
    #     # print(v2s, 'v2s')
    # keys = list(rando_graph.vertices.keys())
    # for v in keys:
    #     rando_num_edges = math.floor(random.randrange(0, len(keys)))
    #     for v2 in range(0, rando_num_edges):
    #         if v2 != v: #v1 if want to loop on itself
    #             rando_graph.add_edge(v, v2)  

    # BokehGraph(rando_graph).show()
    # rando_graph.dfs_iteration(9)

    print("-------------------------")
    print("bfs_iteration ->", graph.bfs_iteration(9))
    print("-------------------------")
    print("dft_iteration ->", graph.dfs_iteration(9))
    print("-------------------------")
    print("dfs_recursion ->", graph.dfs_recursion(10))
    print("-------------------------")
    # print("bfs_recursion ->", graph.bfs_recursion(2))
    # print("-------------------------")
    # print("dfs_path ->", graph.dfs_path(2))
    # print("-------------------------")
    # print("bfs_path ->", graph.bfs_path(2))
    # print("-------------------------")
    

if __name__ == '__main__':
    # TODO - parse argv
    main()
    
