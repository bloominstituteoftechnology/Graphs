from util import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    queue = Queue()
    queue.enqueue([starting_node])

    longest_path = 1 
    earliest_ancestor = -1

    while queue.size() > 0:
        path = queue.dequeue()
        current_node = path[-1]

        if len(path) > longest_path or (len(path) >= longest_path and current_node < earliest_ancestor):
            # if (len(path) >= longest_path_length and current_node < earliest_ancestor) or len(path) > longest_path_length:
            longest_path = len(path)
            earliest_ancestor = current_node

        children = graph.vertices[current_node]
        for ancestor in children:
            path_copy = list(path)
            path_copy.append(ancestor)
            queue.enqueue(path_copy)
    return earliest_ancestor
