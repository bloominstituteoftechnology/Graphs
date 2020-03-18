from util import Stack, Queue

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    # create the queue, most recent parent and the visited set
    q = Queue()
    visited = set()
    most_recent = []
    
    # check if the node has no ancestors
    if has_parents(ancestors,starting_node) is False:
        return -1
    
    # add the starting Node
    q.enqueue(starting_node)

    while q.size() > 0:
        # get the first in line
        v = q.dequeue()
        print(f"Current Node {v}")
        # check if it has been visited or not
        # if so, add it to the visited set
        if v not in visited:
            visited.add(v)
            # check if the node has parents
            # if true
            if has_parents(ancestors,v):
                # clear the most recent parents list
                most_recent.clear()
                # enqueue the parents and add the parents to the most recent
                # parents list
                for parent,child in ancestors:
                    if child == v:
                        q.enqueue(parent)
                        print(f"queueing {parent} as the parents of {v}")
                        # reset the most recent parents
                        most_recent.append(parent)
                        
                print()
            else:
                print(f"{v} has no parents\n")
    # return the smaller of the two parents
    return min(most_recent)
    
def has_parents(ancestors,node):
    children = set()
    for parent, child in ancestors:
        children.add(child)
    if node in children:
        return True
    else:
        return False      

ancestor = earliest_ancestor(test_ancestors,6)           
print(f"The earliest ancestor to the input is {ancestor}")

