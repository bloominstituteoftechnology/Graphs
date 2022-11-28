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
            self.vertices[v1].add(v2)   # there's an edge from v1 to v2
        else:
            raise IndexError("nonexistent vert")

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
        # Create an empty queue
        qq = Queue()
        qq.enqueue([starting_vertex])
        visited = set()
        while qq.size() > 0:
            path = qq.dequeue()
    
            if path[-1] not in visited:
                print(path[-1])
                visited.add(path[-1])
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
        # s = Stack()
        # # Create a set to store the visited nodes
        # visited = set()
        # # Init: push the starting node
        # s.push(starting_vertex)
        # # While the stack isn't empty
        # # print(s.size())
        # while s.size() > 0:
        #     # pop the first item
        #     v = s.pop()
        #     # print(v)
        #     # If it's not been visited:
        #     if v not in visited:
        #         # Mark as visited (i.e. add to the visited set)
        #         visited.add(v)
        #         # Do something with the node
        #         print(f"Visited {v}")
        #         # Add all neighbors to the stack
        #         for next_vert in self.get_neighbors(v):
        #             s.push(next_vert)
        qq = Stack()
        qq.push([starting_vertex])
        visited = set()
        while qq.size() > 0:
            path = qq.pop()
    
            if path[-1] not in visited:
                print(path[-1])
                visited.add(path[-1])
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Need an initial case
        if visited is None:
            visited = set()
        # Base cased: how do we know we are done???  We are done when we have no more neighbors
        # Need to track visited nodes
        visited.add(starting_vertex)
        print(starting_vertex)
        # In order for it to be recursive we need to call the function recursively on the neighbors of the NOT visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        # While the queue is not empty...
        qq = Queue()
        qq.enqueue([starting_vertex])
        visited = set()
        while qq.size() > 0:
            # Dequeue the first PATH
            path = qq.dequeue()
            # Grab the last vertex from the PATH
            if path[-1] not in visited:
                                # This is what needed to be changed for this bfs
                if path[-1] == destination_vertex:
                    return path  # This is what needed to be changed for this bfs
                visited.add(path[-1])
            # If that vertex has not been visited...
                # CHECK IF IT'S THE TARGET
                  # IF SO, RETURN PATH
                # Mark it as visited...
                # Then add A PATH TO its neighbors to the back of the queue
                  # COPY THE PATH
                  # APPEND THE NEIGHOR TO THE BACK
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        ss = Stack()
        ss.push([starting_vertex])
        visited = set()
        while ss.size() > 0:
            path = ss.pop()
            if path[-1] not in visited:
                if path[-1] == destination_vertex:
                    return path
                visited.add(path[-1])
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Need an initial case
        if visited is None:
            visited = set()

        if path is None:
            path = []
        # Base cased: how do we know we are done???  We are done when we have no more neighbors
        # Need to track visited nodes
        visited.add(starting_vertex)
        new_path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return new_path
        # In order for it to be recursive we need to call the function recursively on the neighbors of the NOT visited
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(
                    neighbor, destination_vertex, visited, new_path)
                if neighbor_path:
                    return neighbor_path

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
    Valid BFT(breadth-first traversal) paths:
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
    Valid DFT paths: searching
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    graph.dft_recursive(1)

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
