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
        if v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError(f"The second Vertices you provided: {v2} is not in the graph. You can't link to a vertices that isn't in the graph.")

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
        """
        Loop over every vertex in the queue. Print each vertex
        as we come to it. Find all the edges of the current vertex
        and add them to the queue and the cache.
        """ 
        queue = [starting_vertex]
        isQueued = {starting_vertex}
        for vertex in queue:
            print(vertex)
            for edge in self.vertices[vertex]:
                if edge not in queue:
                    queue.append(edge)
                    isQueued.add(edge)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        """
        Loop until the stack is empty. Remove the last added
        vertex and store it's value as the current vertex. 
        Print the current vertex then loop over all it's edges.
        Add them to the stack and the cache.
        """ 
        stack = [starting_vertex]
        stacked = {starting_vertex}
        while len(stack) > 0:
            currentVertex = stack.pop(-1)
            print(currentVertex)
            for edge in self.vertices[currentVertex]:
                if edge not in stacked:
                    stack.append(edge)
                    stacked.add(edge)
            

    def dft_recursive(self, starting_vertex, cache = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        """
        If this is the first repetition create a cache. If the current
        vertex is not in the cache add it and print the vertex. For
        every edge the vertex has run another repetition.
        """
        if not cache:
            cache = set()
        if starting_vertex not in cache:
            cache.add(starting_vertex)
            print(starting_vertex)
        for key in self.vertices[starting_vertex]:
            if key not in cache:
                self.dft_recursive(key, cache)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        paths = [[starting_vertex]]
        """
        For every list in paths. If the last item in the list is 
        the destination return the list. If the last item is not 
        in the visited cache add it and make a new path for all 
        of it's edges. If the last item has been visited remove 
        it from the paths list.
        """
        for path in paths:
            if path[-1] == destination_vertex:
                return path
            if path[-1] not in visited:
                visited.add(path[-1])
                for key in self.vertices[path[-1]]:
                    newPath = path.copy()
                    newPath.append(key)
                    paths.append(newPath)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        paths = [[starting_vertex]]
        """
        While the length of possible paths is not zero. 
        Store the current path and remove it from possible 
        paths. Return the last path if it's the destination. 
        If the path hasn't been visited yet add it to the 
        visited list and loop over it's edges creating paths 
        to check later. 
        """
        while len(paths) > 0:
            path = paths.pop(-1)
            if path[-1] == destination_vertex:
                return path
            if path[-1] not in visited:
                visited.add(path[-1])
                for key in self.vertices[path[-1]]:
                    newPath = path.copy()
                    newPath.append(key)
                    paths.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex, cache = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        """
        Make starting_vertex a list if it isn't one already. Check if 
        the last element in starting vertex is the destination. Check
        if the last element in the path is in the cache. If it's not 
        add all of that vertex's edges to new lists to run new 
        recursions.
        """
        if not type(starting_vertex) is list:
            starting_vertex = [starting_vertex]
        if not cache:
            cache = set()
        currentVertex = starting_vertex[-1]
        if currentVertex == destination_vertex:
            return starting_vertex
        if currentVertex not in cache:
            cache.add(currentVertex)
            for edge in self.vertices[currentVertex]:
                newPath = starting_vertex.copy()
                newPath.append(edge)
                result = self.dfs_recursive(newPath, destination_vertex, cache)
                if result:
                    return result
        else:
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
    print("graph.vertices", graph.vertices)

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
    print("\nBFT Path")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\nDFT Path")
    graph.dft(1)
    print("\nDFT Recursive Path")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\nBFS Path")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\nDFS Path")
    print(graph.dfs(1, 6))
    print("\nDFS Recursive Path")
    print(graph.dfs_recursive(1, 6))
