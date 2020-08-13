from projects.graph.graph import Graph
from projects.graph.util import Queue



def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for parent, child in ancestors:
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        graph.add_edge(child, parent)

    #print(graph.vertices)

    if starting_node not in graph.vertices:
        return -1

    queue = Queue()
    queue.enqueue([starting_node])

    max_path = 1
    earliest = -1

    while queue.size() > 0:
        #print(queue.queue)

        path = queue.dequeue()

        value = path[-1]
        if (len(path) >= max_path and value < earliest) or (len(path) > max_path):
            earliest = value
            max_path = len(path)

        for next_item in graph.vertices[value]:
            copy = list(path)
            copy.append(next_item)
            queue.enqueue(copy)

    return earliest