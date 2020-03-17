# import graph.py --vertex and edge
from util import Graph, Queue

def earliest_ancestor(ancestors, starting_node):
    print('ancestors', ancestors)
    print('starting_node:', starting_node)
    # instantiate graph
    graphs = Graph()
    print('graphs.vertices', graphs.vertices)
    # loop thru to pop graph
    for ancestor in ancestors:
        print('ancestor:', ancestor)

        graphs.add_vertex(ancestor[0])
        graphs.add_vertex(ancestor[1])
        graphs.add_edge(ancestor[1], ancestor[0])
        print('graphs.vertices-LOOP:', graphs.vertices)

    # dfs - DEPTH FIRST SEARCH -- ??? why queue instead of stack?
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        # last item in list
        v = path[-1]
        print('HERE:', v)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graphs.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor
#
# def earliest_ancestor(ancestors, starting_node):
#     # Build the graph
#     graph = Graph()
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # Build edges in reverse
#         graph.add_edge(pair[1], pair[0])
#     # Do a BFS (storing the path)
#     q = Queue()
#     q.enqueue([starting_node])
#     max_path_len = 1
#     earliest_ancestor = -1
#     while q.size() > 0:
#         path = q.dequeue()
#         v = path[-1]
#         # If the path is longer or equal and the value is smaller, or if the path is longer)
#         if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
#             earliest_ancestor = v
#             max_path_len = len(path)
#         for neighbor in graph.vertices[v]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)
#     return earliest_ancestor
    # stack

    # add starting node to stack



    # UPER
    # FIND OLDEST ANCESTOR
    # The data is formatted as a list of (parent, child) pairs

    # follow the edges - to find - vertex
