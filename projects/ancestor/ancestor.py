def earliest_ancestor(ancestors, starting_node):

    # Create an empty dictionary
    lookup = {}

    # loop through our list
    for pair in ancestors:
        # If the 2nd index is not in our dictionary
        if pair[1] not in lookup:
            # Assign the 2nd index to the first
            lookup[pair[1]] = [pair[0]]
        else:
            # otherwise append it
            lookup[pair[1]].append(pair[0])

    # Depth first to get to the last generation
    def recursion(graph, vertex):

        # if the vertex is not in our graph
        if vertex not in graph:
            # return a value of 1, along with the vertex
            return (1, vertex)

        # Create an empty list
        results = []

        # Recurse through our graph
        for value in graph[vertex]:
            results.append(recursion(graph, value))

        # If there is only 1 ancestor
        if len(results) == 1:
            return (results[0][0] + 1, results[0][1])

        # If we have more than 1 ancestor, we'll have to compare them
        if results[0][0] > results[1][0]:
            return (results[0][0] + 1, results[0][1])
        elif results[0][0] < results[1][0]:
            return (results[1][0] + 1, results[1][1])
        else:
            # If the age is the same, we have to return the lowest ID
            if results[0][1] < results[1][1]:
                return (results[0][0] + 1, results[0][1])
            else:
                return (results[1][0] + 1, results[1][1])

    # Grab the earliest ancestor and deal with situations where the one that was picked is the earliest ancestor
    earliest = recursion(lookup, starting_node)
    if earliest[0] == 1:
        return -1
    else:
        return earliest[1]
