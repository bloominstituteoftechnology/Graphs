from util import Queue
#     * The input will not be empty.
#     * There are no cycles in the input.
#     * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
#     * IDs will always be positive integers.
#     * A parent may have any number of children.


# 1. Translate the problem into graph terminology
# 2. Build your graph
# 3. Traverse your graph


class Graph:
    def __init__(self):
        '''
        represents the graph
        '''

        self.vertices = {}

    def add_vertex(self, vertix_id):
        '''
        add parents to the graph
        '''
        self.vertices[vertix_id] = set()

    def add_edge(self, v1, v2):
        '''
        adds the connection between parent and child 
        '''
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exits")

    def get_neighbors(self, vertex_id):
        '''
        return children's parents
        '''
        return self.vertices[vertex_id]


g = Graph()


def earliest_ancestor(ancestors, starting_node):
    '''
    use bfs to find the shortest path from child to ancestors
    '''

    q = Queue()
    # Enqueue path to starting word
    q.enqueue([starting_node])
    visited = set()
    # While queue is not empty...
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab ancestor from path
        a = path[-1]
        # Check if it's ancestors, if so return path
        if a == ancestors:
            return path
        # Check if it's been visited. If not...
        if a not in visited:
            # Mark it as visited
            visited.add(a)
            # Enqueue a path to each neighbor
            for neighbor in g.get_neighbors(a):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
