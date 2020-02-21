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
        #make queue
        queue = Queue()
        visited = set()
        new_path = list(visited)

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            vertex = queue.dequeue()
        
            if vertex not in visited:
                visited.add(vertex)
                new_path.append(vertex)
                edges = self.get_neighbors(vertex)
                for edge in edges:
                    queue.enqueue(edge)
        print(new_path, 'bft')
                

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        new_list = list(visited)

        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
        
            if vertex not in visited:
                visited.add(vertex)
                new_list.append(vertex)
                edges = self.get_neighbors(vertex)
                for edge in edges:
                    stack.push(edge)
        print(new_list, 'dft')

    def dft_recursive(self, vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # visited = set()
        # new_path = list(visited)

        # def dft_helper(vertex):
        #     if vertex not in visited:
        #         visited.add(vertex)
        #         new_path.append(vertex)
        #         for neighbor in self.vertices[vertex]:
        #             dft_helper(neighbor)
        #         else:
        #             return
        # dft_helper(starting_vertex)
        # print(new_path, 'dft recursive')
        # Works but not what taught ^
    
        visited.add(vertex)

        edges = self.get_neighbors(vertex)

        if len(edges) == 0:
            return
        else:
            for edge in edges:
                if edge not in visited:
                    self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        queue = Queue()
        # make a set for visited
        visited = set()
        # enqueue A PATH TO the starting_vertex
        queue.enqueue([starting_vertex])
        # while the queue isn't empty:
        while queue.size() > 0:
        ## dequeue the next path
            path = queue.dequeue()
        # vertex is the last thing in the path
            vertex = path[-1]
        ## check if its the target, aka the destination_vertix.
            if vertex not in visited:
                if vertex == destination_vertex:
        ## if so, return the path!
                    print(path, 'bfs path')
                    return path
        ## if not, mark this as visited
                visited.add(vertex)
        ## get the neighbors
            for neighbor in self.vertices[vertex]:
        ## copy the path, add the neighbor to the copy
                new_path = list(path)
                new_path.append(neighbor)
        ##  for each one, add a PATH TO IT to our queue
                queue.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        visited = set()

        stack.push([starting_vertex])

        while stack.size() > 0:
            path = stack.pop()

            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    print(path, 'dfs')
                    return path
                visited.add(vertex)
            
            for neighbor in self.vertices[vertex]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.push(new_path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, ):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()
        new_path = list(visited)
        
        def dfs_helper(vertex):

            print(vertex, 'start path recu')
            # print(vertex, 'current path')
            if vertex == destination_vertex:
                print(new_path, 'success path')
                return new_path
            for neighbor in self.vertices[vertex]:
                if vertex not in visited:
                    visited.add(vertex)
                    new_path.append(vertex)
                    dfs_helper(neighbor)
                else:
                    return

        dfs_helper(starting_vertex)        

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