from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    gr = Graph()
    for ancestor in ancestors:
        parent = ancestor[0]
        child = ancestor[1]
        gr.add_vertex(parent)
        gr.add_vertex(child)
        gr.add_edge(child, parent)
    return gr.get_ancestor(starting_node)
