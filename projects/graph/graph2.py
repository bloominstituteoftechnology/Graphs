"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        # empty dictionary for  vertices
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # at vertex_id create an empty set
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if v1 and v2 exist in vertices list
        if v1 in self.vertices and v2 in self.vertices is not None:
            # add v2 at v1 of vertices
            self.vertices[v1].add(v2)

        # otherwise
        else:
            # raise an error
            raise KeyError(f'That vertex does not exist')

    def bft(self, starting_vertex_id):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex_id)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while queue.size() > 0:
            # dequeue the first vertex
            v = queue.dequeue()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited(printing for representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the back of the queue
                for next_vertex in self.vertices[v]:
                    queue.enqueue(next_vertex)

    def dft(self, starting_vertex_id):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex_id)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while stack.size() > 0:
            # pop the first vertex
            v = stack.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited(printing for representation)
                print(v)
                visited.add(v)
                # then add all of it's neighbors to the top of the stack
                for next_vertex in self.vertices[v]:
                    stack.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # if the visited structure is set to None
        if visited is None:
            # create a new set for visited
            visited = set()
        # add a starting vertex to the visited set
        visited.add(starting_vertex)
        # print the start vertex
        print(starting_vertex)
        # loop over every child vertex in vertices set at the start
        for child_vertex in self.vertices[starting_vertex]:
            # if child vertex is not in visited
            if child_vertex not in visited:
                # do a recursive call to dft_recursive
                # using the child vertex and the current visited set as argument
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue to hold the vertex ids
        queue = Queue()
        # enqueue the start vertex id
        queue.enqueue(starting_vertex)
        # create an empty visited set
        visited = set()
        # while the queue is not empty
        while queue.size() > 0:
            # set vertex to the dequeued element
            vertex = queue.dequeue()
            # if vertex not in visisted
            if vertex not in visited:
                # if vertex is target value
                if vertex == destination_vertex:
                    return True
                # add the vertex to the visited set
                visited.add(vertex)
                # loop over next vertex in the vertices st the index of vertex
                for next_vertex in self.vertices[vertex]:
                    # enqueue the next vertex
                    queue.enqueue(next_vertex)
        # return False
        return False

    def dfs(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # if the visited structure is set to None
        if visited is None:
            # create a new set for visited
            visited = set()
            # add a starting vertex to the visited set
            visited.add(starting_vertex)
            # if the start vertex is equal to the target value
            if starting_vertex == destination_vertex:
                # return True
                return True
        # loop over every child vertex in vertices set at the start
        for child_vertex in self.vertices[starting_vertex]:
            # if child vertex is not in visited
            if child_vertex not in visited:
                # if recursive call to dfs
                if self.dft_recursive(child_vertex, visited):
                    # return True
                    return True
        # return false
        return False


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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
