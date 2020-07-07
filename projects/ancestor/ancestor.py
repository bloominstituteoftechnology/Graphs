from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for (parent, child) in ancestors:
        try:
            graph.get_neighbors(parent)
        except KeyError:
            graph.add_vertex(parent)
        try:
            graph.get_neighbors(child)
        except KeyError:
            graph.add_vertex(child)
        graph.add_edge(child, parent)

    def dft_ancestor_depth(child_id, depth):
        parents = graph.get_neighbors(child_id)
        current_depth = depth
        (earliest_id, deepest) = (child_id, current_depth)
        for parent in parents:
            (ancestor_id, total_depth) = \
                dft_ancestor_depth(parent, current_depth + 1)
            if (total_depth > deepest) \
                    or (total_depth == deepest and ancestor_id < earliest_id):
                (earliest_id, deepest) = (ancestor_id, total_depth)
        return (earliest_id, deepest)

    (final, depth) = dft_ancestor_depth(starting_node, 0)
    if depth == 0:
        return -1
    else:
        return final
