
def earliest_ancestor(ancestors, starting_node):
    #pass
    # Construct a table for relationships
    # The key is a child, value is array contains parrents
    geneology = {}
    for birth in ancestors:
        parent = birth[0]
        child = birth[1]
        if child not in geneology:
            geneology[child] = [parent]
        else:
            geneology[child].append(parent)

    # Have a variable with the current shortest paths to iterate through and one
    # if this child is an orphan return negative 1
    if starting_node not in geneology:
        return -1
    children = set([starting_node])
    parents = set()

    # It is true when we reach the end of the line
    furthest_gen = False
    # find the node containing the child
    while not furthest_gen:
        for child in children:
            if child in geneology:
                for parent in geneology[child]:
                    parents.add(parent)
        # Checking to see if set is empty
        if not parents:
            furthest_gen = True
            break
        # Now going to set parents as children and reseting parrents
        children = parents
        parents = set()
    # finding the smallest child and returning it
    return min(children)

