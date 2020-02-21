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
            raise IndexError('That vertex does not exist')

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

        # initialize queue with starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        
        # set to keep track of vertexes already seen
        visited = set()

        # while queue is not empty if we haven't seen the element frome the
        # queue, add to visited, print, and add neighbors to queue
        while q.size() > 0:
            vertex = q.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for edge in self.get_neighbors(vertex):
                    q.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # initialize stack with starting vertex
        s = Stack()
        s.push(starting_vertex)
        
        # set to keep track of vertexes already seen
        visited = set()

        # while queue is not empty if we haven't seen the element frome the
        # queue, add to visited, print, and add neighbors to queue
        while s.size() > 0:
            vertex = s.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for edge in self.get_neighbors(vertex):
                    s.push(edge)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # print current vertex and get edges
        print(starting_vertex)
        edges = self.get_neighbors(starting_vertex)

        # if visited isn't passed, instantiate an empty set
        if visited == None:
            visited = set()

        # add current vertex to visited
        visited.add(starting_vertex)

        # base case is edges is null so this doesn't happen and 
        # method returns
        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # initialize queue with starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        
        # set to keep track of vertexes already seen
        visited = set()

        # while queue is not empty
        while q.size() > 0:
            # get path and vertex
            path = q.dequeue()
            print(path)
            print(type(path))
            vertex = path[-1]
            # if vertex is our target, return path
            if vertex == destination_vertex:
                return path
            # else, add vertex to visited
            elif vertex not in visited:
                visited.add(vertex)      
                # and add paths to the queue for each edge 
                for edge in self.get_neighbors(vertex):
                    q.enqueue(path.append(edge))
        
        raise ValueError('Vertex not found')

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # initialize queue with starting vertex
        s = Stack()
        s.push([starting_vertex])
        
        # set to keep track of vertexes already seen
        visited = set()

        # while queue is not empty
        while s.size() > 0:
            print(s.size())
            # get path and vertex
            path = s.pop()
            print(path)
            print(type(path))
            vertex = path[-1]
            # if vertex is our target, return path
            if vertex == destination_vertex:
                return path
            # else, add vertex to visited
            elif vertex not in visited:
                visited.add(vertex)      
                # and add paths to the queue for each edge 
                for edge in self.get_neighbors(vertex):
                    edge_path = path.copy()
                    edge_path.append(edge)
                    s.push(edge_path)
        
        raise ValueError('Vertex not found')

    def dfs_recursive(self, starting_vertex, target_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        # if visited isn't passed, instantiate an empty set
        if visited == None:
            visited = set()
        
        # if path isn't passed, instantiate with empty list
        if path == None:
            path = []


        if starting_vertex not in visited:
            # add to node to visited and path copy
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # if it's the target, return path
            if starting_vertex == target_vertex:
                return path_copy
            # recursive calls for each edge
            for edge in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(edge, target_vertex, visited=visited, path=path_copy)
                # return if the recursive call found the target
                if new_path is not None:
                    return new_path

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
