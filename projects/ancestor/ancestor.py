
def earliest_ancestor(ancestors, starting_node):

    parents = {}
    
    # build a dictionary with every "child" that has "parents"
    for ancestor in ancestors:
        if ancestor[1] in parents:
            #if "child" in parents dict, append parent in position 0
            parents[ancestor[1]].append(ancestor[0])
 
        else:
            # if "child" NOT in parents dict. Add it.
            parents[ancestor[1]] = [ancestor[0]]
    
    # check if our starting node is in parents, if not they don't have ancestors.
    if starting_node not in parents:
        return -1
    
    curr_ancestors = parents[starting_node]
        
    while True:
        new_ancestors = []
        
        # check each ancestor
        for ancestor in curr_ancestors:
            # if that ancestor is also a child in parents
            if ancestor in parents:
                # add them to the list of ancestors
                new_ancestors = new_ancestors + parents[ancestor]
            # if ancestor isn't in parents and new_ancestors is empty.
            if len(new_ancestors) == 0:
                # return the parent of that child.
                return curr_ancestors[0]
            else:
                # loop again until we reach our return case.
                curr_ancestors = new_ancestors