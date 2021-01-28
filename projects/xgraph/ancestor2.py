from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    lineage = Graph()
    for parent in ancestors:
        if parent[0] not in lineage:
            lineage.add_vertex(parent[0])
        if parent[1] not in lineage:
            lineage.add_vertex(parent[1])
        lineage.add_edge(parent[0], parent[1])
    paths = lineage.dft_recursive(starting_node)
    # take the largest length of any sub-array within paths if len(paths) > 0
    max_length_path = max([len(path) for path in paths]) if len(paths) > 0 else 0
    potential_res = []
    for path in paths:
        if len(path) == max_length_path:
            potential_res.append(path)

        if len(potential_res) == 1:
            return potential_res[0][-1]

        elif len(potential_res) > 1:
            current_ancestor = potential_res[0][-1]
            for path_ in potential_res:
                if path_[-1] < current_ancestor:  # last person in sub-path inside of potential_res
                    current_ancestor = path_[-1]  # set current_ancestor to last path

            return current_ancestor

        return -1  # you have no oldest ancestor


def earliest_ancestor_doc(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])

    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    early_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < early_ancestor) or (len(path) > max_path_len):
            early_ancestor = v
            max_path_len = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return early_ancestor
