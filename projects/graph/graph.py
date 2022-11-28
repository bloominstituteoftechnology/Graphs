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
        self.vertices[vertex_id] = set() # holds the edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2) # set.add()
        else:
            raise IndexError("vertex doesn't exist")

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
        # This uses a queue, tracks what is visited until completely explored.
        # while the queue is not empty, dequeue and keep going.
        #  Visit, add all neighbors into the queue, order doesn't matter.

        q = Queue()
        visited = set() # instantiate

        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            # check if not visited before
            if v not in visited:
                visited.add(v)
                print("Ya'll done just arrived at {v}")
                # add the neighbors of leaving node
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Only difference here is we push and pop from a Stack
        s = Stack()
        visited = set()

        s.push(starting_vertex)
        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                print("Ya'll just done popped by {v}")
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
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dfs_recursive(v, visited)

        # visited = set()

        # def dft_inner(vertex):
        #     if vertex not in visited:
        #         visited.add(vertex)
        #         print("under you is dat dere {vertex}")
        #     for neighbor in self.get_neighbors(vertex):
        #         dft_inner(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty Q and NQ a PATH TO the starting vertex
        q = Queue()
        q.enqueue([starting_vertex]) # Make it into a list to represent a path
        # Create a set to store visited
        visited = set()
        # while Q not empty:
        while q.size() > 0:
        #   DQ first PATH
            v = q.dequeue()
        #   Grab last vertex from PATH
            last_vertex = v[-1]
        #   if vertext not visited:
            if last_vertex not in visited:
        #       check if its target, if so return path 
                if last_vertex == destination_vertex:
                    return v
        #   mark it as visited,
                visited.add(last_vertex)
        #   add A PATH TO its neghibors to the back of the Q
                for neighbor in self.get_neighbors(last_vertex):
        #       COPY THE PATH
                    path_copy = list(v)
        #       Append to the back  
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty Q and NQ a PATH TO the starting vertex
        s = Stack()
        s.push([starting_vertex]) # Make it into a list to represent a path
        # Create a set to store visited
        visited = set()
        # while Q not empty:
        while s.size() > 0:
        #   DQ first PATH
            v = s.pop()
        #   Grab last vertex from PATH
            last_vertex = v[-1]
        #   if vertext not visited:
            if last_vertex not in visited:
        #       check if its target, if so return path 
                if last_vertex == destination_vertex:
                    return v
        #   mark it as visited,
                visited.add(last_vertex)
        #   add A PATH TO its neghibors to the back of the Q
                for neighbor in self.get_neighbors(last_vertex):
        #       COPY THE PATH
                    path_copy = list(v)
        #       Append to the back  
                    path_copy.append(neighbor)
                    s.pop(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

    #     def dfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     """
    #     visited = set()
    #     path_stack = Stack() 

    #     path_stack.push([starting_vertex])

    #     while path_stack.size() > 0:
    #         path = path_stack.pop()
    #         last_vertex = path[-1]

    #         if last_vertex in visited:
    #             continue
    #         else:
    #             visited.add(last_vertex)

    #         for neighbor in self.get_neighbors(last_vertex):
    #             next_path = path.copy()
    #             next_path.append(neighbor)

    #             if neighbor == destination_vertex:
    #                 return next_path
    #             path_stack.push(next_path)

    # def dfs_recursive(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     This should be done using recursion.
    #     """
    #     visited = set()

    #     def dft_inner(path):
    #         last_vertex = path[-1]
            
    #         if last_vertex in visited:
    #             return None
    #         else:
    #             visited.add(last_vertex)

    #         if last_vertex == destination_vertex:
    #             return path
            
    #         for neighbor in self.get_neighbors(last_vertex):
    #             next_path = path.copy()
    #             next_path.append(neighbor)
            
    #             found = dft_inner(next_path)
    #             if found:
    #                 return found
            
    #         return None

    #     return dft_inner([starting_vertex])

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
