"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    # def retrieve_set(self, vert):
    #     """
    #     Expects a vertex as an arg and returns connected vertices
    #     """

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # U =>
        # a vertex is an entry in the dictionary self.vertices, where the value at this
        # entry is a set of vertices that this specific vertex connects to
        # P =>
        # the vertex_id will be the key in the self.vertices dictionary
        # the value the key points to will be an emoty set()
        # E =>
        self.vertices[vertex_id] = set()
        # print(self.vertices[key], "empty set")

        # R =>
        # I can fetch the set in the self.vertices dict but it returns the actual function invocation..
        # not sure if it will cause problems later or if it'll change format when we add an edge

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # U =>
        # an edge represents the connection of two vertices
        # these edges will be unweighted (unnamed)
        # adding an edge creates a v1 to v2 connection...
        # to make it a bidirectional graph, invoke this function again but swap v2 and v1 to make the
        # connection mutual
        # P =>
        # use v1 as the key
        # use v2 as the value to be added to the set that v1 key points to
        # use the set method .add() add value
        # E =>
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex nonexistent!")
        # R =>
        # I think maybe the add_edge method should check to see if the connecting vertex (the 2nd arg)
        # is a vertex already and if not, create a new vertex in self.vertices and then continue
        # with the rest of this add_edge() invocation

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        visited = set()
        while plan_to_visit.size() > 0:
            current_vertex = plan_to_visit.dequeue()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for n in self.get_neighbors(current_vertex):
                    if n not in visited:
                        plan_to_visit.enqueue(n)
        # whilw plan_to_visit is not empty
            # dequeue first vertex in queue
            # if it's not been visited:
                # print vertex
                # mark as visited
                # add neighbors to queue

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        visited = set()
        while plan_to_visit.size() > 0:
            current_vertex = plan_to_visit.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for n in self.get_neighbors(current_vertex):
                    if n not in visited:
                        plan_to_visit.push(n)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


# graph = Graph()
# graph.add_vertex("2")
# graph.add_edge("2", "3")
# graph.add_edge("2", "50")

# print(graph.vertices, "important check")

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
