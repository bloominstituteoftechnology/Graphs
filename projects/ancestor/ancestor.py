
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # queue of current nodes
    q = Queue()
    # add first node to path set
    path = [starting_node]

    q.enqueue(path)

    while q.size() > 0:
        current_path = q.dequeue()
        # list of next layer nodes
        new_path = []
        changed = False

        # get begin node of path
        for node in current_path:
            # loop through ancestors for parents
            for ancestor in ancestors:
                # look into each ancestor parent with start_node as child
                if ancestor[1] == node:
                    new_path.append(ancestor[0])
                    changed = True
                    q.enqueue(new_path)

        if changed is False:
            if current_path[0] == starting_node:
                return -1
            else:
                return current_path[0]


    # loop through final path for largest value