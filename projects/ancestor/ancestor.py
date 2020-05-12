from collections import deque

def earliest_ancestor(ancestors, starting_node):
    # Generate a dict to hold the value of the node as the key
    # and a list of that key's parents as the value
    struct = {}

    # Loop through each pair in the ancestors list
    for pair in ancestors:
        # Parent is the first value of pair
        parent = pair[0]
        # Child is the second value of pair
        child = pair[1]

        # If child is not in struct, add it
        if child not in struct:
            struct[child] = []
        
        # Finally add the parents of each child to their list in the dict
        struct[child].append(parent)

    # Create a queue
    q = deque()

    # Append the starting node as a list containing only
    # the starting node
    q.append([starting_node])

    # Set a default longest node to store the largest distance,
    # index 0, and the last node that corresponded with that longest
    # distance
    longest_node = [0,-1]

    # While the queue is not empty
    while len(q) > 0:
        # Pop the first path list from the queue
        curr_path = q.popleft()
        
        # Get the last node in the path
        last_node = curr_path[-1]

        # If the last node has no parents (i.e. is not in the dict),
        # it is at the top
        if last_node not in struct:
            # If the length of the current path is longer than the
            # longest previous path, that will be the new longest path
            # and store the node that corresponds with it
            if len(curr_path) > longest_node[0] and last_node > longest_node[1]:
                longest_node = [len(curr_path), last_node]

        # If the last node does have parents though
        else:
            # Loop through each of those parents and queue up
            # a path from the current path to each parent
            for x in struct[last_node]:
                q.append(curr_path + [x])

    # if the longest node is still the default (starting_node)
    # return -1, as the starting node has no parents
    if longest_node[1] == starting_node:
        return -1

    # Else return the node farthest away (longest_node index 1)
    else:
        return longest_node[1]
