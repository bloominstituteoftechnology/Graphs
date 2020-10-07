from graph import Graph

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    # Using graph object be able to add "nodes" to structure
    # and "edges" between nodes to connect them        
    graph = Graph()

    # Add vertices
    for i in ancestors:
        if i[0] not in graph.vertices:
            graph.add_vertex(i[0])
        if i[1] not in graph.vertices:
            graph.add_vertex(i[1])

    # Add edges
    for i in ancestors:
        graph.add_edge(i[1], i[0])

    # bft returns list of all connected ancestors
    # from closet to fartherest
    path = graph.bft(starting_node)
    # get last connect node or "earlist" connected ancestor
    v = path[-1]

    # if nothing preceeds itself
    if starting_node == v:
        # no index of ancestor
        return -1
    # otherwise, there is
    else:
        # there is
        return v

print(earliest_ancestor(ancestors, 6)) 