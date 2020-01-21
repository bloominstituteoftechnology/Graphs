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
        if v1 not in self.vertices:
            self.vertices[v1] = set()

        if v2 not in self.vertices:
            self.vertices[v2] = set([v1])
        else:
            self.vertices[v2].add(v1)

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

    def bfs(self, starting_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if (starting_vertex not in self.vertices
        or len(self.get_neighbors(starting_vertex)) == 0):
            return -1

        # #Step 1 Create an empty queue and enqueue a PATH TO the starting vertex ID
        q = Queue()
        q.enqueue( [starting_vertex])
        # #Create an empty Set to store visited vertices
        visited = set()
        # going to need something to keep track of the lenght
        longest_path = []
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first Path
            path = q.dequeue()
            # Grab the last vertex from the Path
            v = path[-1]
            # if that vertex has not been visited...
            if v not in visited:
                # do the thing
                # mark it as visited
                visited.add(v)

                # then add a Path to its neighbors to the back if the qeueue
                for neighbor in self.get_neighbors(v):
                    # Copy path to avoid pass by reference bug
                    path_copy = path.copy()
                    # append the neighbor to the back of the copy
                    path_copy.append(neighbor)
                    # need to check the length of the new path
                    if len(longest_path) < len(path_copy):
                        longest_path = path_copy
                    # have to handle if the new path length is equal
                    if len(longest_path) == len(path_copy):
                        if longest_path[-1] > path_copy[-1]:
                            longest_path = path_copy


                    q.enqueue(path_copy)

        return longest_path[-1]

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for a in ancestors:
        graph.add_edge(a[0],a[1])
    return graph.bfs(starting_node)


# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)
#
#     print(graph.vertices)
#     print(graph.bfs(1))
