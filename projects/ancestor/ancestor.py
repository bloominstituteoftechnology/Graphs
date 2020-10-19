class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)



def earliest_ancestor(ancestors, starting_node):
    parents_for_child = {}

    # Build graph where IDs = vertices & relationships = edges
    for relationship in ancestors:
        parent = relationship[0]
        child = relationship[1]
        if child not in parents_for_child:
            parents_for_child[child] = set()
        parents_for_child[child].add(parent)

    earliest_ancestor = -1

    # Run BFS n graph and return last ancestor found
    queue = Queue()
    queue.enqueue(starting_node)
    while queue.size() > 0:
        curr_vertex = queue.dequeue()
        if curr_vertex in parents_for_child:
            parent_with_lowest_ID = None
            for parent in parents_for_child[curr_vertex]:
                if parent_with_lowest_ID is None:
                    parent_with_lowest_ID = parent
                elif parent < parent_with_lowest_ID:
                    parent_with_lowest_ID = parent
                queue.enqueue(parent)
            if parent_with_lowest_ID is not None:
                earliest_ancestor = parent_with_lowest_ID


    return earliest_ancestor

