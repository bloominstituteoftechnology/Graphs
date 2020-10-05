"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
       self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v2 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        visited = set()
        # initialize
        q.enqueue(starting_vertex)

        while q.size() > 0:
            v= q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        s = Stack()
        visited = set()
        # initialize
        s.push(starting_vertex)

        while s.size() > 0:
            v= s.pop()

            if v not in visited:
                print(v)
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if not visited:
            visited = set()
        # if visited
        if vertex in visited:
            # return
            return
        # add to visited
        visited.add(vertex)
        # print this value
        print(vertex)
        # for each vertice
        for found_vertex in self.vertices[vertex]:
            # call dft_recursive on this vertice, with this visited
            self.dft_recursive(found_vertex, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()

        # initialize
        q.enqueue([starting_vertex])

        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # save last element from the path
            v = path[-1]
            # check that vertex has not been visited
            if v not in visited:
                # check if vertex is destination
                if v == destination_vertex:
                    # if so, return path
                    return path
                # set as visited
                visited.add(v)
                # Then add path to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = path.copy()
                    # append neighbor to the end of queue
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()

        # initialize
        s.push([starting_vertex])

        while len(s.stack) > 0:
           # pop off the first path
            path = s.pop()
            # save last element from the path
            v = path[-1]
            # check that vertex has not been visited
            if v not in visited:
                # check if vertex is destination
                if v == destination_vertex:
                    # if so, return path
                    return path
                # set as visited
                visited.add(v)
                # Then add path to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    # make a copy of the path
                    path_copy = path.copy()
                    # append neighbor to the end of queue
                    path_copy.append(neighbor)
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    print("______")
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
    print("______")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("______")
    graph.dft_recursive(1)
    print("______")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    print("______")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print("______")
    print(graph.dfs_recursive(1, 6))
