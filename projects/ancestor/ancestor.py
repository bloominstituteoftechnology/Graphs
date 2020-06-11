
from util import Queue 

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    """
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    First value is the data and the second is the value we are looking for.
    * if the value has no ancesestors, return -1
    * 
    """

    g = Graph()

    # Maps the graph of nodes to their immediate ancestors (unidirectional). 
    for i in ancestors:
        if i[0] not in g.vertices:
            g.add_vertex(i[0])
        if i[1] not in g.vertices:
            g.add_vertex(i[1])

        g.add_edge(i[1], i[0])


    print(g.vertices)
    # Create an empty queue and enqueue the starting vertex ID
    q = Queue()

    # push the first path into the queue
    q.enqueue([starting_node])

    potential_ancestors = []

    while q.size() > 0:
        # get the first path from the queue
        path = q.dequeue()
        # get the last node from the path
        node = path[-1]
        # path found
        if g.get_neighbors(node) == set():
            potential_ancestors.append(path)
        # enumerate all adjacent nodes, construct a new path and push it into
        # the queue
        for adjacent in g.get_neighbors(node):
            new_path = list(path)
            new_path.append(adjacent)
            q.enqueue(new_path)

    k = (0, 0)
    # len, last ancestor
    for i in potential_ancestors:
        # iterating over, redefining k everytime there's a new longest list of potential ancestors
        if len(i) > k[0]:
            k = (len(i), i[-1])
        # If two lists are the same len then we keep the ancestor with the lesser node value
        elif len(i) == k[0] and i[-1] < k[-1]:
            k = (len(i), i[-1])
        else:
            pass
    
    # stopping condition, if the starting_node is the final node in the tree
    if starting_node == k[1]:
        return -1
    
    return k[1]

if __name__ == "__main__":

    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

    print(earliest_ancestor(test_ancestors, 6))