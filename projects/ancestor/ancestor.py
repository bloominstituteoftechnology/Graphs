
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    def get_depth(child, depth):
        parents = g.get_neighbors(child)
        deepest_traveled = depth
        (earliest_ancestor, deepest) = (child, depth)

        for parent in parents:
            (ancestor, total_depth) = get_depth(parent, deepest_traveled + 1)
            if (total_depth > deepest) or (total_depth == deepest and ancestor < earliest_ancestor):
                (earliest_ancestor, deepest) = (ancestor, total_depth)
        return (earliest_ancestor, deepest)
   
    for (parent, child) in ancestors:
        try:
            g.get_neighbors(parent)
        except KeyError:
            g.add_vertex(parent)

        try:
            g.get_neighbors(child)
        except KeyError:
            g.add_vertex(child)
        g.add_edge(child, parent)

    (earliest, depth) = get_depth(starting_node, 0)
    if depth == 0:
        return -1
    else:
        return earliest





