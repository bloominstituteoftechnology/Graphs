# Create helper function
def create_adjacency_list(input_list):
    # create an empty set to store the adjacency list
    adjacency_list = {}
    # create a for loop to go through array of tuples to transform it into an adjacency list
    for tuple in input_list:
        if tuple[1] not in adjacency_list:
            adjacency_list[tuple[1]] = [tuple[0]]
        elif tuple[1] in adjacency_list:
            adjacency_list[tuple[1]].append(tuple[0])
    return adjacency_list

def earliest_ancestor(ancestors, starting_node):
    # Use helper function to convert test_ancestors to an adjacency list
    adjacency_list = create_adjacency_list(ancestors)
    # Write a DFS:
    visited = set()
    stack = []
    stack.append([starting_node])
    possible_paths = []
    while len(stack):
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.add(node)
            if node in adjacency_list.keys():
                # if the key has multiple values, iterate over the keys
                for neighbor in adjacency_list[node]:
                    # if neighbor is none then pass, because we don't want to risk getting it inside the possible path array
                    if neighbor == None:
                        pass
                    # else keep going normally
                    else:
                        # copy the path
                        path_copy = path.copy()
                        # append neighbor to the back of the copy
                        path_copy.append(neighbor)
                        # push copy to stack
                        stack.append(path_copy)
            # else append path to possible_paths
            else:
                possible_paths.append(path)

    correct_path = possible_paths[0]
    for possible_path in possible_paths:
        if len(possible_path) > len(correct_path):
            correct_path = possible_path
        if len(possible_path) == len(correct_path) and possible_path[-1] < correct_path[-1]:
            correct_path = possible_path

    # return the path with the lowest initial value
    if len(correct_path) > 1:
        correct_path = correct_path[-1]
    if type(correct_path) is list:
        correct_path = correct_path[0]
    if correct_path == starting_node:
        correct_path = -1
    return correct_path
