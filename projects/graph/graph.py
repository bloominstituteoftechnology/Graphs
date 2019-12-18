"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import random


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
        # check to see that v1 is in our dictionary
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex doesn't exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if self.vertices[vertex_id]:
            return self.vertices[vertex_id]
        return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            vertex = q.dequeue()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting_vertex
        s = Stack()
        s.push(starting_vertex)
        # create an empty set to hold visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # Pop the end of the stack
            vertex = s.pop()
            # if it hasn't been visited
            if vertex not in visited:
                # print it and add it to visited
                print(vertex)
                visited.add(vertex)
                # add all of its neighbors to the stack
                for neighbor in self.vertices[vertex]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def dft_helper(vertex):
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for neighbor in self.vertices[vertex]:
                    dft_helper(neighbor)
            else:
                return
        dft_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue
        q = Queue()
        # enqueue a path to the starting_vertex
        q.enqueue([starting_vertex])
        # create a set to to hold visited vertices
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # dequeue the first path
            path = q.dequeue()
            # check if last vertex in path is destination_vertex
            if path[-1] == destination_vertex:
                return path
            # if the last vertex in the path hasn't been visited
            elif path[-1] not in visited:
                # mark it as visited
                visited.add(path[-1])
                # enqueue all of its neighbors as new paths
                for neighbor in self.vertices[path[-1]]:
                    new_path = path[:]
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # instantiate a new stack
        s = Stack()
        # push the path to the starting_vertex
        s.push([starting_vertex])
        # create an empty visited set
        visited = set()
        # while the stack isn't empty...
        while s.size() > 0:
            # pop the last path off the stack
            path = s.pop()
            # if the last vertex in the path is our destination vertex, return it
            if path[-1] == destination_vertex:
                return path
            # else if the last vertex in the path has not been visited
            elif path[-1] not in visited:
                # mark it as visited
                visited.add(path[-1])
                # loop through all of its neighbors
                for neighbor in self.vertices[path[-1]]:
                    # copy the old path
                    new_path = path[:]
                    # append the neighbor to the end
                    new_path.append(neighbor)
                    # push it onto the stack
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        valid_paths = []

        def dfs_helper(path):
            if path[-1] == destination_vertex:
                valid_paths.append(path)
                return
            elif path[-1] not in visited:
                visited.add(path[-1])
                for neighbor in self.vertices[path[-1]]:
                    new_path = path[:]
                    new_path.append(neighbor)
                    dfs_helper(new_path)
            else:
                return
        dfs_helper([starting_vertex])
        return random.choice(valid_paths)


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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
