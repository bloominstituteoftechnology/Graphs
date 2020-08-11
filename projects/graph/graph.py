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
        # pass  
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # pass
        # Stretch - edges to nonexistent vertices are rejected
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)  
        else:
            print('Invalid vertex/vertices')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # pass  
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # pass 
        bft_queue = Queue()
        bft_queue.enqueue(starting_vertex)
        visited = {}
        vertices_count = len(self.vertices.keys())

        while len(visited.keys()) < vertices_count:
            # dequeue the node
            vertex = bft_queue.dequeue()
            if vertex not in visited:
                visited[vertex] = None
            # enqueue the children for dequeued node
            if len(self.vertices[vertex]) > 0:
                for v in self.vertices[vertex]:
                    bft_queue.enqueue(v)
        
        # print the list of visited
        # print(list(visited.keys()))
        for v in visited:
            print(v)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # pass  
        dft_stack = Stack()
        dft_stack.push(starting_vertex)
        visited = {}
        vertices_count = len(self.vertices.keys())

        while len(visited.keys()) < vertices_count:
            # pop the node
            vertex = dft_stack.pop()
            if vertex not in visited:
                visited[vertex] = None
            # push the children for popped node
            if len(self.vertices[vertex]) > 0:
                for v in self.vertices[vertex]:
                    dft_stack.push(v)
        
        # print the list of visited
        # print(list(visited.keys()))
        for v in visited:
            print(v)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # pass
        if visited == None:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for v in self.vertices[starting_vertex]:
                self.dft_recursive(v, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass

        q = Queue()
        q.enqueue([starting_vertex])

        visited = set()
        # get minimum distance for each node
        
        while q.size is not 0:
            path = q.dequeue()

            vertex = path[-1]
            
            if vertex not in visited:
                visited.add(vertex)

                if vertex == destination_vertex:
                    return path
                else:
                    for v in self.vertices[vertex]:
                        new_path = list(path)
                        new_path.append(v)
                        q.enqueue(new_path)
        
        return None

        
        



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass 
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size is not 0:
            path = s.pop()

            vertex = path[-1]

            if vertex not in visited:
                visited.add(vertex)
            if vertex is destination_vertex:
                return path
            else:
                for v in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(v)
                    s.push(new_path)
        
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # pass  
        if visited == None and path == None:
            visited = set()
            path = []
        
        if starting_vertex not in visited:
            new_path = list(path)
            new_path.append(starting_vertex)

            visited.add(starting_vertex)

            if starting_vertex is destination_vertex:
                return new_path
            
            for v in self.get_neighbors(starting_vertex):
                next_path = self.dfs_recursive(v, destination_vertex, visited, new_path)
                if next_path:
                    return next_path
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
    # graph.add_edge(4,8) # Test for stretch

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
