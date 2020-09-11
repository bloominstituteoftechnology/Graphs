from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for vertex_1, vertex_2 in ancestors:
        graph.add_vertex(vertex_1)
        graph.add_vertex(vertex_2)

    for vertex_1, vertex_2 in ancestors:
        graph.add_edge(vertex_1, vertex_2)

    target_vertex = None

    longest_path = 1

    for vertex in graph.vertices:

        # vertex = starting_vertex and starting_node = destination_vertex
        # from imported Graph class DFS method
        path = graph.dfs(vertex, starting_node)

        if path:
            print(path)

            if len(path) > longest_path:
                longest_path = len(path)
                target_vertex = vertex

        elif not path and longest_path == 1:
            target_vertex = -1

    return target_vertex
