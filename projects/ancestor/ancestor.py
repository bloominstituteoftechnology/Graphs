
def earliest_ancestor(ancestors, starting_node):
    # We'll call our cache parents and make it a set 
    famtree = dict()

    # Now let's make parents into an adjancency list
    for ancestor in ancestors:
        kid = ancestor[1]
        if kid not in famtree:
            famtree[kid] = set()
            famtree[kid].add(ancestor[0])

        else:
            famtree[kid].add(ancestor[0])
    
    kids = list(famtree.keys())
    
    parents = set()
    for ancestor in ancestors:
        parents.add(ancestor[0])
    parents = list(parents) 

    if starting_node not in kids:
        return -1

    s = list()
    s.append(starting_node)

    seen = set()
    rents_ids = list()
    path = list()

    while len(s) > 0:
        # Sorting s forces the smallest value on any particular traversed level to go last
        s.sort()
        current = s.pop()

        if current not in seen:
            seen.add(current)
            path.append(current)
            
            if current in kids:
                rents_ids = list(famtree[current])
                for ids in rents_ids:
                    s.append(ids)
    return path[-1]


trial_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(trial_ancestors, 8))