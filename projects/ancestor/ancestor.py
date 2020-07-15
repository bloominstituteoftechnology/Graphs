def earliest_ancestor(ancestors, starting_node):
    pass
    # set up graph of children -> parents
    lookup = {}
    for pair in ancestors:
        if pair[1] not in lookup:
            lookup[pair[1]] = [pair[0]]
        else:
            lookup[pair[1]].append(pair[0])
    # print(lookup)
    # DFT through the nodes to get to the last generation
    def recurse(graph, vertex):
            # endpoints: nowhere left to go
            # print(vertex)
            if vertex not in graph:
                return (1, vertex)
            # work: do nothing
            # recurse: get results of recursing
            results = []
            for val in graph[vertex]:
                results.append(recurse(graph, val))
            # print(results)
            # get oldest ancestor otherwise smallest ID, pass it on

            # only one ancestor
            if len(results) == 1:
                return (results[0][0] + 1, results[0][1])

            # two ancestors, compare them
            if results[0][0] > results[1][0]:
                return (results[0][0] + 1, results[0][1])
            elif results[0][0] < results[1][0]:
                return (results[1][0] + 1, results[1][1])
            else:
                # same age, return lowest ID
                if results[0][1] < results[1][1]:
                    return (results[0][0] + 1, results[0][1])
                else:
                    return (results[1][0] + 1, results[1][1])

    # get earliest ancestor and deal with cases where
    # the one picked is the earliest ancestor
    earliest = recurse(lookup, starting_node)
    if earliest[0] == 1:
        return -1
    else:
        return earliest[1]
