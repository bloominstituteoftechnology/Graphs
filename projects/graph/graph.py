"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # this is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2.
        """
        # check if edges exist
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else:
            print('error adding edge vertex not found')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None  # might want to crash program here

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to the store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            vert = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if vert not in visited:
                # Mark it as visited
                print(vert)
                visited.add(vert)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(vert):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Add starting to the set and print
        visited.add(starting_vertex)
        print(starting_vertex)
        # Get children of starting and if child not in visited already then RECURSION
        for child in self.vertices[starting_vertex]:
            if child not in visited:
                self.dft_recursive(child, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        qq = Queue()
        # Create an empty set to store visited nodes
        visited = set()
        # Add A PATH TO the starting vertex_id to the queue
        qq.enqueue([starting_vertex])
        # While the queue is not empty...
        while qq.size() > 0:
            # Dequeue, the first PATH
            path = qq.dequeue()
            # Grab the LAST VERTEX FROM THE PATH
            last_vertex = path[-1]
            # CHECK IF IT"S THE TARGET
            if last_vertex == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            else:
                # If it has not been visited...
                if last_vertex not in visited:
                    # Mark it as visited
                    visited.add(last_vertex)
                    neighbor = self.get_neighbors(last_vertex)
                    # Then add A PATH TO all neighbors to the back of the queue
                    for n in neighbor:
                        # Make a copy of the path before adding
                        copy_path = list(path)
                        # Add n to our copy
                        copy_path.append(n)
                        # Add new copy to our queue
                        qq.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack
        s = Stack()
        # Create an empty set to store visited nodes
        visited = set()
        # Add A PATH TO the starting vertex_id to the queue
        s.push([starting_vertex])
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue, the first PATH
            path = s.pop()
            # Grab the LAST VERTEX FROM THE PATH
            last_vertex = path[-1]
            # CHECK IF IT"S THE TARGET
            if last_vertex == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            else:
                # If it has not been visited...
                if last_vertex not in visited:
                    # Mark it as visited
                    visited.add(last_vertex)
                    neighbor = self.get_neighbors(last_vertex)
                    # Then add A PATH TO all neighbors to the back of the queue
                    for n in neighbor:
                        # Make a copy of the path before adding
                        copy_path = list(path)
                        # Add n to our copy
                        copy_path.append(n)
                        # Add new copy to our queue
                        s.push(copy_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # Add starting to visited
        visited.add(starting_vertex)
        # Add path and starting
        path = path + [starting_vertex]
        # If starting is the target then return path
        if starting_vertex == destination_vertex:
            return path
        # If not
        # Get neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            # If neighbors are not visited
            if neighbor not in visited:
                # Copy path and pass it to dfs_recursive
                copy_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path)
                # Return that path
                if copy_path is not None:
                    return copy_path
        # If not found return None
        return None


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
