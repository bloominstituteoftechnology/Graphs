def find_earliest_ancestor_dfs(adjacency_list, starting_vertex):
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
        count = 0
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
        elif possible_path[0] < correct_path[0]:
            correct_path = possible_path
    # return the path with the lowest initial value
    return correct_path


adjacency_list = {

1: (10, None),
3: (1, 2),
5: (4, None),
6: (5, 3),
7: (5, None),
8: (4, 11),
9: (8, None)

}

find_earliest_ancestor_dfs(adjacency_list, 6)
