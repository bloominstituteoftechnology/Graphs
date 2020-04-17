from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    '''
    find earliest ancestor of a graph using dfs
    '''

    graph = Graph()
    paths = []

    # add vertex
    for vertex in range(0, 20):
        graph.add_vertex(vertex)
        # print(graph.vertices)

    # add edge
    for ancestor in ancestors:
        graph.add_edge(ancestor[0], ancestor[1])
        # print(graph.vertices)

    for vertex in graph.vertices:
        if graph.dfs(vertex, starting_node) != None and len(graph.dfs(vertex, starting_node)) > 0:
            paths.append(graph.dfs(vertex, starting_node))
        # print(paths)

    if len(paths) == 1:
        return -1

    # find earliest neighbor
    start_path = paths[0]
    for path in paths:
        if len(path) > len(start_path) or len(path) == len(start_path) and path[0] < start_path[0]:
            start_path = path
        # print(path)
        # print(start_path)

    return start_path[0]