from util import Queue


def find_parents(ancestors, value):
    parents = []
    for ancestor in ancestors:
        if (ancestor[1] == value):
            parents.append(ancestor[0])
    return parents

def earliest_ancestor(ancestors, starting_node):
    # Start with empty list of ancestors
    ancestor = []
    # Start with making a Queue
    q = Queue()
    # Enqueue list with starting_node
    q.enqueue([starting_node])
    # Make empty visited set
    visited = set()
    # While queue is not empty
    while q.size() > 0:
        # dequeue list in 
        lineage = q.dequeue()
        # Look at the parent(1st element) in dequeue'd tuple
        p = lineage[-1]
        # See if parent has been visited
        if (p not in visited):
            # Mark as visited
            visited.add(p)
            # check if the value of the parent is a child in other tuples
            # If they aren't, add the path to the ancestor list
            if (find_parents(ancestors, p) == []):
                ancestor.append(lineage)
            # Otherwise, find the new parents and add them to the lineage
            else:
                for parent in find_parents(ancestors, p):
                    new_lineage = lineage + [parent]
                    q.enqueue(new_lineage)
    ''' Once we've found all the ancestors,
    we want to find the earliest ancestor
    '''
    # Start with the first element as the temp earliest
    earliest = ancestor[0]
    # For each path, we've found
    for path in ancestor:
        # Check if one is longer than the rest
        if (len(path) > len(earliest)):
            earliest = path
        # Or the one younger ancestor at the end
        elif (len(path) == len(earliest) and path[-1] < earliest[-1]):
            earliest = path
    # If the earliest list only has one element, we did not move
    # And there is no earliest ancestor
    if (len(earliest) == 1):
        return -1
    # Else, the earliest ancestor is the one at the end of the earliest list
    return earliest[-1]
