import os
import sys
sys.path.append('../graph')
from graph import Graph

# def process_parents(parents, starting_node, g):
#     for parent in parents:
#         new_parents = g.get_neighbors(parent)
#         if new_parents:
#             process_parents(new_parents, parent, g)
#         else:


def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for each in ancestors:
        g.add_vertex(each[0])
        g.add_vertex(each[1])

    for each in ancestors:
        g.add_edge(each[1], each[0])
    print(g.vertices)
    # init_parents = g.get_neighbors(starting_node)
    # prev_parents = -1

    # return process_parents(init_parents, starting_node, g)
    # if init_parents:
    #     for parent in init_parents:
    #         print(parent)
    #         prev_parents = init_parents
    #         init_parents = g.get_neighbors(parent)
    #         print(init_parents)
    #         if not init_parents:
    #             print(prev_parents)
    # else:
    #     print( prev_parents)

    # while init_parents:

    #     for parent in init_parents:
    #         print(parent)
    #         prev_parents = init_parents
    #         print(prev_parents)
    #         init_parents = g.get_neighbors(parent)
    #         print(init_parents)
    
    # parents = g.bft(starting_node)
    # print(parents)
    # last = -1
    # if len(parents) == 1:
    #     return last
    # for parent in parents:
    #     last = parent
    # print(last)
    # return last
    # parent = g.dft(starting_node)
    # print(parent)
    # if parent == starting_node:
    #     return -1
    # else:
    #     return parent



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),(4,5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 8)