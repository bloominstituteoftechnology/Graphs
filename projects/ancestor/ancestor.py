from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # build the family tree
    tree = Graph()

    # for each pair tuple in ancestor, add the nodes 
    for pair in ancestors:
        if pair[0] not in tree.vertices:
            tree.add_vertex(pair[0])
        if pair[1] not in tree.vertices:
            tree.add_vertex(pair[1])

        # add the relationships in tree
        tree.add_edge(pair[0], pair[1])

    # create a list to store the relations
    relations = []

    # for each parent in tree, breadth first search
    for parent in tree.vertices:
        path = tree.bfs(parent, starting_node)
        # add the path to relations
        if path is not None:
            relations.append(path)

    # if there are more than 1 paths in relations
    if len(relations) > 1:
        # get the oldest
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