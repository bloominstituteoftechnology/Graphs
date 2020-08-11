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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

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
        # create an empty queue
        q = Queue()
        # add starting_vertex
        q.enqueue(starting_vertex)
        # create a set for visited vertices
        visited = set()
        
        # while the queue is empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if not visited:
            if v not in visited:
                # visit node
                print(v)
                # mark as visited
                visited.add(v)
                # add node's neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack
        s = Stack()
        # add starting_vertex
        s.push(starting_vertex)
        # create a set for visited vertices
        visited = set()
        
        # while the stack is empty
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if not visited:
            if v not in visited:
                # visit node
                print(v)
                # mark as visited
                visited.add(v)
                # add node's neighbors to the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # check if starting_vertex is in the graph
        if starting_vertex in self.vertices:
            print(starting_vertex)
            # add starting_vertex to visited set
            visited.add(starting_vertex)

            # get the neighbors of starting_vertex
            for neighbor in self.get_neighbors(starting_vertex):
                # if the neighbor is not in the visited set:
                if neighbor not in visited:
                    # perform the dft with the neighbor as the starting_vertex
                    self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            p = q.dequeue()
            # Grab the last vertex from the PATH
            v = p[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                  # IF SO, RETURN PATH
                  return p
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                  # COPY THE PATH
                  p2 = p.copy()
                  # APPEND THE NEIGHBOR TO THE BACK
                  p2.append(neighbor)
                  # ADD PATH TO THE QUEUE
                  q.enqueue(p2)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack and push the starting_vertex
        s = Stack()
        s.push(starting_vertex)
        # create a visited set
        visited = set()

        while s.size() > 0:
            # pop the top vertex in the stack
            v = s.pop()
            # add it to the visited set
            visited.add(v)
            
            for neighbor in self.get_neighbors(v):
                # if the neighbor has not been visited:
                if neighbor not in visited:
                    # add the neighbor to the stack
                    s.push(neighbor)
                # if the neighbor is the destination_vertex:
                if neighbor is destination_vertex:
                    # add the neighbor to visited
                    visited.add(neighbor)
                    # return the visited set as a list -> [PATH]
                    return list(visited)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # create a path with the starting_vertex
        if path is None:
            path = [starting_vertex]

        # create a visited set if there is none
        if visited is None:
            visited = set()

        # get the current vertex from the end of the path
        v = path[-1]

        # if the vertex is the destination_vertex, return the path
        if v == destination_vertex:
            return path
        
        # if vertex has not been visited, mark as visited
        if v not in visited:
            visited.add(v)

            # create a new path from the old path, adding the neighbor vertex to the path
            for neighbor in self.get_neighbors(v):
                next_path = path + [neighbor]
                # perform recursive search
                search = self.dfs_recursive(v, destination_vertex, next_path, visited)

                # if there is a result, return it
                if search:
                    return search

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
    print("-------------graph.vertices-------------")
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7 <-
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
    print("-------------bft-------------")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7 <- dft_recursive
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5 <- dft
        1, 2, 4, 6, 3, 5, 7
    '''
    print("-------------dft-------------")
    graph.dft(1)
    print("-------------dft_recursive-------------")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("-------------bfs-------------")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6] <- dfs <- dfs_recursive
        [1, 2, 4, 7, 6]
    '''
    print("-------------dfs-------------")
    print(graph.dfs(1, 6))
    print("-------------dfs_recursive-------------")
    print(graph.dfs_recursive(1, 6))