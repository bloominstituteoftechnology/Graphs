

# create a BFS w/ cache and add conditions to earliest_ancestor()


# ultils because import was not working
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


# graph


def earliest_ancestor(ancestors, starting_node):
    # the one at the farthest distance
    # from the input individual.
    #  If there is more than one ancestor
    # tied for "earliest", return the one
    # with the lowest numeric ID. If the
    # input individual has no parents,
    # the function should return -1.

    # turn the ancestors list into a adjacency list
    adj_list = {}
    for anc_pair in ancestors:
        # add both vertices to adj_list
        if anc_pair[0] not in adj_list:
            adj_list[anc_pair[0]] = set()
        if anc_pair[1] not in adj_list:
            adj_list[anc_pair[1]] = set()
        # add the edge  between the 2 vertices
        adj_list[anc_pair[1]].add(anc_pair[0])
        print(adj_list)

    # build the graph
    # starting_node = []
    queue = [ [starting_node] ]
    visited = set()
    max_path_length = 1
    current_earliest_ancestor = -1

    # traverse the graph BFS
    while len(queue) > 0:
        # dequeue the the current path  + vertex
        # get the current vertex out of the path
        cur_path = queue.pop(0)  # pop the "first" item
        cur_vertex = cur_path[-1]
        print(cur_path)
        
        # if the vertex has not been visited
        if cur_vertex not in visited:
            # add the vertex to the visited set
            visited.add(cur_vertex)

        if len(cur_path) > max_path_length or len(cur_path) >= max_path_length and cur_vertex < current_earliest_ancestor:
            max_path_length = len(cur_path)
            current_earliest_ancestor = cur_vertex

        for neighbors in adj_list[cur_vertex]:
            # copy the current path
            n_path = list(cur_path)
            # add the neighbor to the queue
            n_path.append(neighbors)
            queue.append(n_path)
    return current_earliest_ancestor



# print(earliest_ancestor(ancestors_list, 5))
