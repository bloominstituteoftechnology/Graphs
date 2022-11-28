from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    family_tree = Graph()

    for tup in ancestors:
        if tup[0] not in family_tree.vertices:
            family_tree.add_vertex(tup[0])
        if tup[1] not in family_tree.vertices:
            family_tree.add_vertex(tup[1])

        family_tree.add_edge(tup[0], tup[1])

    relations = []

    for parent in family_tree.vertices:
        path = family_tree.bfs(parent, starting_node)
        if path is not None:
            relations.append(path)

    if len(relations) > 1:
        oldest = relations[0]
        for path in relations:
            if len(path) > len(oldest):
                oldest = path
            if len(path) == len(oldest):
                if path[0] < oldest[0]:
                    oldest = path
        return oldest[0]
    else:
        return -1
