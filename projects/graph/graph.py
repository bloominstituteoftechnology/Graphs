"""
Simple graph implementation
"""
from util import Stack, Queue  ## These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set() # <-- set() -- creates a new set -> { }
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2) #adds a value to the set

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        queue = Queue()
        queue.enqueue(starting_vertex)
        
        # Create a Set to store visited vertices
        visited = set()
       
        # While the queue is not empty...
        while queue.size() > 0:
        # Dequeue the first vertex
            v = queue.dequeue() #grab and pop item
        # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                visited.add(v)
                print(v)
                # Then add all of its neighbors to the back of the queue
                
                for i in self.vertices[v]:
                    queue.enqueue(i)
        print('>>>> End of Breadth First')

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print(self.vertices[1])
        # Create an empty stack and push the starting vertex ID
        stack = Stack()
        stack.push(starting_vertex)
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while stack.size() > 0:
        # pop the first vertex
            v = stack.pop()
        # If that vertex has not been visited...
            if v not in visited:
            # Mark it as visited...
                visited.add(v)
                print(v)
            # Then add all of its neighbors to the back of the queue
                for i in self.vertices[v]:
                    stack.push(i)
        print('>>>> End of Depth First')

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor,visited)
        
    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if path is None:
            path = []
        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == target_vertex:
            return path
        
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, target_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None


               
       
              

      


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # print('>>>> End of recursive')
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
       
        # Create a Set to store visited vertices
        visited = set()
         # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Mark it as visited...
            v = path[-1]
            
            if v not in visited:
                if v == destination_vertex:
                    return path
                visited.add(v)
                #for every value in the vertices from the last item in the list
                for neighbor in self.vertices[v]:
                    # CHECK IF IT'S THE TARGET
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)
        


                # if v == destination_vertex:  
                #     # IF SO, RETURN PATH
                #     path.append(v)
                #     return path
                # # If that vertex has not been visited...
                # if v not in visited:
                #     queue.enqueue(list([*path, v]))
            

    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print('>>>> End of bfs')
         # Create an empty queue and enqueue A PATH TO the starting vertex ID
        stack = Stack()
        path = []
        # Create a Set to store visited vertices
        visited = {starting_vertex}
        stack.push(starting_vertex)
        # While the queue is not empty...
        while stack.size() > 0:
            #pop of last item 
            vertex = stack.pop()
            #append that item to vertex
            path.append(vertex)
            #for every value in that vetex's set
            for v in self.vertices[vertex]:
                 # If that vertex has not been visited...
                if v not in visited:
                    stack.push(v)
                    visited.add(v)
                    #if it is vistied
                    if v == destination_vertex:
                         # return path
                        path.append(v)
                        return path





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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)
    print(graph.dfs_recursive(1, 6))
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
