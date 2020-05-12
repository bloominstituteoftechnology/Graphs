def earliest_ancestor(ancestors, starting_node, has_parent=False):
    for parent, child in ancestors:
        if child == starting_node:
            # find the parent of the parent
            return earliest_ancestor(ancestors, parent, True)

    return starting_node if has_parent == True else -1