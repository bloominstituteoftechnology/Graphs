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

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

def earliest_ancestor(ancestors, starting_node):
    # transform the input into a graph
    graph = Graph()
    for pair in ancestors: # (parent, child)
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        # build the edge as well
        graph.add_edge(child, parent)
    # Do a BFS
    visited_neighbors = set()
    neighbors_to_visit = Queue()
    neighbors_to_visit.enqueue(
        {
            'vertex': starting_node, 
            'path_so_far': [starting_node]
        }
    )
    max_path_len = 1
    earliest_ancestor = -1 # we have not found an earliest ancestor
    while neighbors_to_visit.size() > 0:
        vertex_and_path = neighbors_to_visit.dequeue()
        current_vertex = vertex_and_path['vertex']
        current_path = vertex_and_path['path_so_far']
        # check if visited
        if (current_vertex not in visited_neighbors):
            # add to visited
            visited_neighbors.add(current_vertex)
            # Check if this current path is the longest we have seen
            # if it is, update the longest path seen variable
            # also, if its the same length as the longest one we have seen, if the ancestor has smaller ID, use it
            if ((len(current_path) >= max_path_len and current_vertex < earliest_ancestor) 
            or (len(current_path) > max_path_len)):
                earliest_ancestor = current_vertex
                max_path_len = len(current_path)

            for neighbor in graph.vertices[current_vertex]: 
                path_copy = list(current_path)
                path_copy.append(neighbor)
                neighbors_to_visit.enqueue({
                    'vertex': neighbor,
                    'path_so_far': path_copy
                })
    return earliest_ancestor