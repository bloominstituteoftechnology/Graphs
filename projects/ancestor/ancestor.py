from util import Queue

def earliest_ancestor(ancestors, starting_node):
    
    queue = Queue()
    current_node = starting_node
    relationships = {}
    
    for ancestor in ancestors: 
        if ancestor[1] not in relationships:
            relationships[ancestor[1]] = set()
        relationships[ancestor[1]].add(ancestor[0])

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