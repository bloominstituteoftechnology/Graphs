from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        graph.add_vertex(ancestor[0])
        graph.add_vertex(ancestor[1])
        graph.add_edge(ancestor[1], ancestor[0])
    
    solution = graph.bfs_longest_route(starting_node)
    if starting_node == solution:
        return -1
    else:
        return solution