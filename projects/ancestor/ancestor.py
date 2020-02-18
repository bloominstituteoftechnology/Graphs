# import graph.py --vertex and edge
from util import Graph, Stack

def earliest_ancestor(ancestors, starting_node):
    print('ancestors', ancestors)
    print('starting_node', starting_node)
    # instantiate graph
    graphs = Graph()
    print('graphs1::', graphs.vertices)
    # loop thru to pop graph
    for ancestor in ancestors:
        print('ancestor:', ancestor)
        for node in ancestor:
            print('node:', node)
            # graphs.append(ancestor)
            graphs.add_vertex(node)
            # graphs.add_edge(ancestor[0], ancestor[1])
            print('graphs.verticesADD::', graphs.vertices)
            for ancestor in ancestors:
                print('forloop-ancestor:', ancestor)
                if ancestor[0] is not None:
                    print('node[0]', ancestor[0])
                    if ancestor[1] is not None:
                        print('ancestor[1]', ancestor[1])
                        graphs.add_edge(ancestor[0], ancestor[1])
                        print('graphsEnd::', graphs.vertices)
    # dfs - DEPTH FIRST SEARCH

    # stack

    # add starting node to stack



    # UPER
    # FIND OLDEST ANCESTOR
    # The data is formatted as a list of (parent, child) pairs

    # follow the edges - to find - vertex
