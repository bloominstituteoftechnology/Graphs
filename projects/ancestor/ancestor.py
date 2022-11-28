from projects.graph.graph import Graph
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # Populate graph
    for pair in ancestors:
        graph.add_edge(pair[0], pair[1])

    # Extract vertices, for easier code comprehension
    stuff = graph.vertices

    # Find all current parents
    parents = [x for x in stuff.keys() if starting_node in stuff[x]]

    if len(parents):
        best = (parents[0], 0)
        parents.reverse()
        for parent in parents:
            finished = False
            current = parent
            count = 1
            while not finished:
                for key in stuff.keys():
                    if current in stuff[key]:
                        current = key
                        count += 1
                        finished = False
                    else:
                        finished = True

            # Handle same distance
            if count > best[1]: best = (current, count)
            elif count is best[1]:
                if current < best[0]:
                    best = (current, count)
        return best[0]

    # If none are found, return -1 outright
    else:
        return -1

def earliest_ancestor_path(dict, starting_node):
    graph = Graph()
    graph.vertices = dict
    # Populate graph
    # for pair in ancestors:
    #     graph.add_edge(pair[0], pair[1])

    # Extract vertices, for easier code comprehension
    stuff = graph.vertices

    # Find all current parents
    parents = [x for x in stuff.keys() if starting_node in stuff[x]]
    # print("Parents")
    # print(parents)
    # print(starting_node)
    if len(parents):
        best = (parents[0], 0)
        parents.reverse()
        for parent in parents:
            finished = False
            current = parent
            count = 1
            while not finished:
                for key in stuff.keys():
                    if current in stuff[key] and key is not starting_node:
                        current = key
                        count += 1
                        finished = False
                    else:
                        finished = True

            # Handle same distance
            if count > best[1]:
                best = (current, count)
            elif count is best[1]:
                if current < best[0]:
                    best = (current, count)
        return best[0]
    # If none are found, return -1 outright
    else:
        return -1
