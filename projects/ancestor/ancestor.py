

def earliest_ancestor(ancestors, starting_node):
    # set up our graph
    graphy = {}
    for tup in ancestors:
        if tup[1] not in graphy:
            graphy[tup[1]] = set()
        graphy[tup[1]].add(tup[0])

    print(graphy)

    path = [starting_node]
    q = [path]
    result = []

    if get_parents(starting_node, graphy) == []:
        return -1

    while len(q) > 0:
        new_path = q.pop(0)
        vertex = new_path[-1]
        parents = get_parents(vertex, graphy)
        print("parents, vertex", parents, vertex)

        if parents == []:
            result.append(new_path)
        else:
            for i in parents:
                pathy = new_path + [i]
                q.append(pathy)

    size = len(result[0])
    for i in result:
        if len(i) > size:
            size = len(i)
    new_results = list(filter(lambda x: len(x) >= size, result))

    # print("new results", new_results)
    return min([i[-1] for i in new_results])


def get_parents(node, graph):
    if node in graph:
        parents = list(graph[node])
    else:
        parents = []
    return parents


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(ancestors, 6))
