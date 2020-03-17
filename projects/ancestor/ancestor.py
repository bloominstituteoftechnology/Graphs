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
        if vertix_id not in self.vertices:
            self.vertices[vertix_id] = set()

    def add_edge(self, v1, v2):
        '''
        adds the connection between parent and child
        '''
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError(f"that vertex does not exits {v1}, {v2}")

    def get_ancestor(self, vertex_id):
        '''
        return children's parents
        '''
        # if vertex_id in self.vertices
        return self.vertices[vertex_id]


g = Graph()


def create_vertex(ancestors):
    '''
    Build the graph
    '''
    for i in ancestors:
        # make tuple in to list
        a_list = list(i)
        # create vertex in each list
        g.add_vertex(a_list[0])
        g.add_vertex(a_list[1])


def create_edges(ancestors):
    '''
    create edges
    '''
    for i in ancestors:
        # create  edge
        a_list = list(i)
        g.add_edge(a_list[1], a_list[0])


def earliest_ancestor(ancestors, starting_node):
    '''
    use bfs to find the shortest path from child to ancestors
    '''
    # create helper function for adding vertex and edges
    create_vertex(ancestors)
    create_edges(ancestors)

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
        # Check if it's been visited. If not...
        if a not in visited:
            # Mark it as visited
            visited.add(a)
            # Enqueue a path to each ancestor
            for neighbor in g.get_ancestor(a):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
            #   if a not in ancestors return -1
    if len(visited) == 1:
        return -1
    else:
        return a


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 2))
