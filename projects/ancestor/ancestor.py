# import graph.py --vertex and edge
from util import Graph, Stack

def earliest_ancestor(ancestors, starting_node):
    # instantiat graph
    graphs = Graph()
    print('graphs1::', graphs.vertices)
    # loop thru to pop graph
    for ancestor in ancestors:
        print('ancestor:', ancestor)
        # graphs.append(ancestor)
        graphs.add_vertex(ancestor)
    print('graphs2::', graphs)
    # dfs
    # stack

    # add starting node to stack



    # UPER
    # FIND OLDEST ANCESTOR
    # The data is formatted as a list of (parent, child) pairs

    # follow the edges - to find - vertex
