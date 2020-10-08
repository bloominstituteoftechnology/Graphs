from util import Stack, Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # pass

    queue = Queue()
    last_vertex = starting_node
    parent_path = {}
    for node in ancestors:
        if node[1] not in parent_path:
            parent_path[node[1]] = set()
        parent_path[node[1]].add(node[0])

    if starting_node in parent_path:
        queue.enqueue(parent_path[last_vertex])
    else:
        return -1

    while True:
        relations = queue.dequeue()
        last_vertex = min(relations)
        if last_vertex not in parent_path:
            return last_vertex
        else:
            queue.enqueue(parent_path[last_vertex])
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 2))
        

