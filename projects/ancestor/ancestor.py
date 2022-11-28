from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # iterate through every pair of parent, child values passed in
    for pair in ancestors:
        # add vertices for all the values
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # connect them with edges
        graph.add_edge(pair[1], pair[0])
    
    earliest_ancestor = -1
    max_len = 1
    veritces = graph.vertices

    q = Queue()
    q.enqueue([starting_node])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if (len(path) > max_len) or (len(path) == max_len and v < earliest_ancestor):
            earliest_ancestor = v
            max_len = len(path)
        for n in veritces[v]:
            new_path = list(path)
            new_path.append(n)
            q.enqueue(new_path)
        
    return earliest_ancestor