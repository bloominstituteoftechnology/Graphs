from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()

    for ancestor in ancestors:
        print("ancestor", ancestor)
        parent = ancestor[0]
        child = ancestor[1]
        if child not in ancestor_graph.vertices:
            ancestor_graph.add_vertex(child)

        ancestor_graph.add_edge(child, parent)

    print(ancestor_graph.vertices)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


earliest_ancestor(test_ancestors, 0)
