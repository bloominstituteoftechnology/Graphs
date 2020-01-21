from util import Stack, Queue  # These may come in handy
import sys
sys.path.insert(0, '../graph')

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
        # Checking if the to two vertices exist
        if v1 in self.vertices:
            # if true then add them
            self.vertices[v1].add(v2)
        else:
            self.vertices[v1] = set([v2])
        if v2 not in self.vertices:
            self.vertices[v2] = set()


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    #traversal pseudocode:
    # create a queue/stack as appropriate
        # put the starting point in that
        # make a set to keep track of where we’ve been
        # while there is stuff in the queue/stack
        #    pop the first item
        #    if not visited
        #       do the thing!
        #       add to visited
        #       for each edge in the item
        #           add that edge to the queue/stack

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex == destination_vertex:
            return [starting_vertex]
        # #Step 1 Create an empty queue and enqueue a PATH TO the starting vertex ID
        q = Queue()
        q.enqueue( [starting_vertex])
        # #Create an empty Set to store visited vertices
        visited = set()
        # going to need something to keep track of the lenght

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first Path
            path = q.dequeue()
            # Grab the last vertex from the Path
            v = path[-1]
            # if that vertex has not been visited...
            if v not in visited:
                # check to see if It's the target
                if v == destination_vertex:
                # if so return the path
                    return path
                # mark it as visited
                visited.add(v)

                # then add a Path to its neighbors to the back if the qeueue
                for neighbor in self.get_neighbors(v):
                    # Copy path to avoid pass by reference bug
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def earliest_ancestor(ancestors, starting_node):
        pass
