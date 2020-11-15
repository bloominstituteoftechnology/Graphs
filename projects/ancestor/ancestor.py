# from graph.graph import Graph
from resources import Queue, Graph
print(Queue)


def earliest_ancestor(ancestors, starting_node):
    pass
    #  ancestors = a list of tuples that establish node/edges find the furthest nodes
    #
    # insertion_set = set()
    graph = Graph()
    for pair in ancestors:  # fill the graph and adding vertex
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(child)
        graph.add_vertex(parent)
        graph.add_edge(child, parent)
    queue = Queue()
    queue.enqueue([starting_node])  # ([1])
    longest_path = 1
    earliest_ancestor = -1
    while queue.size() > 0:
        current_path = queue.dequeue()
        current_node = current_path[-1]
        # if not graph.get_neighbors(current_node):
        # parents = graph.get_neighbors(current_node)
        if len(current_path) >= longest_path and current_node < earliest_ancestor:
            earliest_ancestor = current_node
            longest_path = len(current_path)
        if len(current_path) > longest_path:
            longest_path = len(current_path)
            earliest_ancestor = current_node
        parents = graph.get_neighbors(current_node)
        for parent in parents:
            new_path = current_path.copy()
            new_path.append(parent)  # [6, 3] [6,5]
            queue.enqueue(new_path)  # queue = [[6, 3], [6,5]]
            #[[6,5], [6,3,1], [6,3,2]]
    # print(graph.get_neighbors(8))
    return earliest_ancestor
    # print(insertion_set)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 9))
