"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            # raise an error
            raise KeyError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # initialize a new set to hold neighbors
        neighbors = set()
        # loop through the vertices
        for vertex in self.vertices:
            # if vertex is equal to the id passed in
            if vertex is vertex_id:
                # get the union of the direct edges
                neighbors = neighbors.union(self.vertices[vertex])
            # otherwise, if any of the vertices has the passed in id in its set
            elif vertex_id in self.vertices[vertex]:
                # it must be a neighbor
                neighbors.add(vertex)

        return neighbors

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while not queue.is_empty():
            # Dequeue the first vertex
            v = queue.dequeue()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited and print for traversal visualization
                visited.add(v)
                print(v)
                # then enqueue all of its direct neighbour(s)
                for next_vertex in self.vertices[v]:
                    queue.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while not stack.is_empty():
            # pop the first vertex
            v = stack.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark it as visited and print for traversal visualization
                visited.add(v)
                print(v)
                # then push all of its direct neighbour(s)
                for next_vertex in self.vertices[v]:
                    stack.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visited.add(starting_vertex)
        # print for traversal visualization
        print(starting_vertex)

        # loop through the vertex's neighbours
        for neighbour in self.vertices[starting_vertex]:
            #  check if neighbour has not been visited
            if neighbour not in visited:
                # and call dft_recursive on it
                self.dft_recursive(neighbour, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while not queue.is_empty():
            # dequeue to the path
            path = queue.dequeue()
            # set a vertex to the last item in the path
            vertex = path[-1]
            # if that vertex has not been visited
            if vertex not in visited:
                # if vertex is equal to destination value
                if vertex == destination_vertex:
                    # return path
                    return path
                # mark vertex as visited
                visited.add(vertex)
                # loop over next vertex in the set of vertices for the current vertex
                for next_vertex in self.vertices[vertex]:
                    # set a new path equal to a new list of the path
                    new_path = list(path)
                    # append next vertex to new path
                    new_path.append(next_vertex)
                    # enqueue the new path
                    queue.enqueue(new_path)
        # return None if it breaks out of the while loop
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push a list containing the starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while not stack.is_empty():
            # pop to the path
            path = stack.pop()
            # set a vertex to the last item in the path
            vertex = path[-1]
            # if that vertex has not been visited
            if vertex not in visited:
                # if vertex is equal to target value
                if vertex == destination_vertex:
                    # return path
                    return path
                # mark vertex as visited
                visited.add(vertex)
                # loop over next vertex in the set of vertices for the current vertex
                for next_vertex in self.vertices[vertex]:
                    # set a new path equal to a new list of the path
                    new_path = list(path)
                    # append next vertex to new path
                    new_path.append(next_vertex)
                    # push the new path
                    stack.push(new_path)
        # return None if it breaks out of the while loop
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for vertex in self.vertices[starting_vertex]:
            if vertex not in visited:
                new_path = self.dfs_recursive(
                    vertex, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/BloomInstituteOfTechnology/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
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
