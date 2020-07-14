from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    current_node = starting_node
    relationships = {}
    for node in ancestors:
        if node[1] not in relationships:
            relationships[node[1]] = set()
        relationships[node[1]].add(node[0])

    if starting_node in relationships:
        queue.enqueue(relationships[current_node])
    else:
        return -1

    while True:
        relations = queue.dequeue()
        current_node = min(relations)
        if current_node not in relationships:
            return current_node
        else:
            queue.enqueue(relationships[current_node])

