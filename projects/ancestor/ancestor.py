from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    # Create an empty queue
    q = Queue()
    # Create an list called 'path' housing the starting_node
    path = [starting_node]
    # Add that path(just the starting_node) to the queue
    q.enqueue(path)
    # While the queue is not empty
    while q.size() > 0:
        # Create a currentPath variable set to be our dequeued queue
        currentPath = q.dequeue()
        # Create an empty newPath list
        newPath = []
        # Create a changed variable set to False
        changed = False
        # Loop over each node in the currentPath
        for node in currentPath:
            # Loop through its ancestors
            for ancestor in ancestors:
                # If the value of the next ancestor is equal to the node:
                if ancestor[1] == node:
                    # Append the current ancestor to the newPath
                    newPath.append(ancestor[0])
                    # Set its changed value to true
                    changed = True
                    # Add the new path to the queue
                    q.enqueue(newPath)
        # If changed is False
        if changed is False:
            # If it has no parents
            if currentPath[0] == starting_node:
                return -1
            # If it does return it
            else:
                return currentPath[0]