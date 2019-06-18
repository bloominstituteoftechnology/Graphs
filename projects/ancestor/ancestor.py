def make_adjacency_list(input_list):
    # create an empty set to store the adjacency list
    adjacency_list = {}
    # create a for loop to go through array of tuples to transform it into an adjacency list
    for tuple in input_list:
        # take second element of tuple and check to see if it has a corrsponding key in adjacency_list. If not in the adjacency list, put it in.
        if tuple[1] in adjacency_list:
        # take first element of tuple and put it inside the "neighbors" array in the second tuple corresponding key's value
            adjacency_list[tuple[1]].append(tuple[0])
        elif tuple[1] not in adjacency_list:
            adjacency_list[tuple[1]] = [tuple[0]]
    # return adjacency list
    return adjacency_list

def earliest_ancestor(test_ancestors, starting_vertex):
    # Use helper function to convert test_ancestors to an adjacency list
    adjacency_list = make_adjacency_list(test_ancestors)
    # Write a DFS:
    # empty set to store visited nodes
    visited = set()
    #create an empty stack and push a path to the start
    stack = []
    stack.append([starting_vertex])
    # create an empty set of possible paths
    possible_paths = []
    # run the following code while stack size > 0
    while len(stack) > 0:
        # pop first path from the stack and store it into a variable
        path = stack.pop()
        # grab the vertex from the end of the path
        vertex = path[-1]
        # if vertex is equal to destination_vertex then the path is stored into `possible_paths`
        # if vertex == destination_vertex:
            # possible_paths.add(path)
        # If the vertex has not been visited
        if vertex not in visited:
            # Mark vertex as visited
            visited.add(vertex)
            # add A PATH TO all of its neighbors if vertex is a key in adjacency list
            if vertex in adjacency_list.keys():
                # if the key has multiple values, iterate over the keys
                for neighbor in adjacency_list[vertex]:
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
    # out of the while loop now, we compare the first values from each opposite path. First declare a property to hold the first value of each possible path so that we can compare
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
    if correct_path == starting_vertex:
        correct_path = -1
    return correct_path


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

make_adjacency_list(test_ancestors)

earliest_ancestor(test_ancestors, 6)
