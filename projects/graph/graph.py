from collections import deque

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
        if vertex_id not in self.vertices:
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
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    queue.append(neighbor)
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    stack.append(neighbor)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                print(neighbor)
                self.dft_recursive_helper(neighbor, visited)
        
    def dft_recursive_helper(self, starting_vertex, visited):
        visited.add(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                print(neighbor)
                self.dft_recursive_helper(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        path = [starting_vertex] # starts path with starting verting
        #call helper function
        self.bfs_recursive_helper(starting_vertex, destination_vertex, path) 
        path.append(destination_vertex)
        return path
                
    def bfs_recursive_helper(self, starting_vertex, destination_vertex, path):
        # base case 
        if starting_vertex == destination_vertex:
            return
        # neighbors appends all neighbors of each vertex but resets everytime the function recurses
        neighbors = [] 
        for n in self.get_neighbors(starting_vertex):
            if n == destination_vertex:
                return
            neighbors.append(n) # this is where we append all the neighbors of each starting point
        starting_vertex = neighbors[-1] # here we set the starting point to the last item in neighbors
        path.append(starting_vertex) # we add this to the path to represent depth-ward
        self.bfs_recursive_helper(starting_vertex, destination_vertex, path)                

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        # Each element in the stack is the current path e.g [1, 2, 3..]
        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0:
            currPath = stack.pop() # [1, 2, 3]
            currNode = currPath[-1] # 3
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        path = [starting_vertex] # starts path with starting verting
        #call helper function
        self.dfs_recursive_helper(starting_vertex, destination_vertex, path) 
        
        return path
                
    def dfs_recursive_helper(self, starting_vertex, destination_vertex, path):
        # base case 
        if starting_vertex == destination_vertex:
            return
        # neighbors appends all neighbors of each vertex but resets everytime the function recurses
        neighbors = [] 
        for n in self.get_neighbors(starting_vertex):
            neighbors.append(n) # this is where we append all the neighbors of each starting point
        starting_vertex = neighbors[-1] # here we set the starting point to the last item in neighbors
        path.append(starting_vertex) # we add this to the path to represent depth-ward
        self.dfs_recursive_helper(starting_vertex, destination_vertex, path)

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
