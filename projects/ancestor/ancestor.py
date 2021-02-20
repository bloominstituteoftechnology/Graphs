
def earliest_ancestor(ancestors, starting_node):

    # my graph will be set to a dictionary
    my_graph = {}

    # loop over over the list
    for pair in ancestors:
        # check if the key exist an
        if pair[1] not in my_graph:
            my_graph[pair[1]] = [pair[0]]
        else:
            my_graph[pair[1]].append(pair[0])
    # if the key isn't in the list then its a parent node
    if starting_node not in my_graph:
        return -1

    #initialzing my my with the starting node
    my_stack = [(my_graph[starting_node], [starting_node])]
    max_length = []
    
    while len(my_stack) > 0:

        # popping off the the path and parent nodes from the stack
        current_node, path = my_stack.pop(0)

        if len(current_node) > 0:

            # loping over neighbors and adding them to the stack
            for neighbor in current_node:

                # adding neighbor to the path
                my_path = path + [neighbor]

                # if the neigh isnt in the graph then its a parent and that the end of the tree
                if neighbor not in my_graph:

                    # checking to see if the current path is longer
                    if len(my_path) > len(max_length):
                        max_length = my_path

                    # Because they are equal, we need to compare the last element
                    elif len(my_path) == len(max_length):
                        if my_path[-1] < max_length[-1]:
                            max_length = my_path

                # the node has parents and we need to evaluate them       
                else:
                    my_stack.append((my_graph[neighbor], my_path))

    return max_length[-1]


if __name__ == '__main__':
    print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6))