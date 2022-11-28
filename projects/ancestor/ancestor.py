
def earliest_ancestor(ancestors, starting_node):
    parents = {}

    for ancestor in ancestors:
        if ancestor[1] in parents:
            parents[ancestor[1]].append(ancestor[0])
        else:
            parents[ancestor[1]] = [ancestor[0]]
            # parents[ancestor[1]].add(ancestor[0])
    
    curr_node = starting_node

    if starting_node not in parents:
        return -1 
    
    curr_ancestors = parents[starting_node]
    visited = set()

    while True:
        new_ancestors = []
        for ancestor in curr_ancestors:
            if ancestor in parents:
                new_ancestors = new_ancestors + parents[ancestor]
        if len(new_ancestors) == 0:
            return curr_ancestors[0]
        else:
            curr_ancestors = new_ancestors