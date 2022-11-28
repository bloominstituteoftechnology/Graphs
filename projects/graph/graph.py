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
            raise IndexError("nonexisten vertex")

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
        queue = Queue()
        visited = set()

        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            vertice = queue.dequeue()

            if vertice not in visited:
                visited.add(vertice)
                print(vertice)

                for next_vertice in self.get_neighbors(vertice):
                    queue.enqueue(next_vertice)
        


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                print(v)
            
                for neighbor in self.get_neighbors(v):
                    stack.push(neighbor)
        


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # we keep running the each next neighbour the loop 
        visited = set()
        def dft_recurse_inner(recurse_vertex):
            if recurse_vertex in visited:
                return
            else:
                visited.add(recurse_vertex)
            print(recurse_vertex)
            for neighbor in self.get_neighbors(recurse_vertex):
                dft_recurse_inner(neighbor)
            
        dft_recurse_inner(starting_vertex)
        


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        ## make a queue
        
        q = Queue()
        q.enqueue([starting_vertex])
        # make the set 
        visited = set()
        # check if the size of queue is greater than 0 
        # if yes we will get the deque and give it a variable
        while q.size() > 0:
            v = q.dequeue()
            last_v = v[-1]
            if last_v not in visited:
                visited.add(last_v)
       #check if the dequed v in the visited set # while the v is not destination vertex keep appending 
            for neighbor in self.get_neighbors(last_v):
                new_path = v.copy() # v copy because it's going to be modified 
                new_path.append(neighbor)
                if neighbor == destination_vertex:
                    return new_path
                q.enqueue(new_path)
                
       
            
       # and then check the neighbors if in the self get neighbours
       # if yes enqueue that vertex from that neighbour to the 

    def dfs(self, starting_vertex, destination_vertex):
        
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            v = stack.pop()
            last_v = v[-1]
            if last_v not in visited:
                visited.add(last_v)
            for neighbor in self.get_neighbors(last_v):
                new_path = v.copy()
                new_path.append(neighbor)
                if neighbor == destination_vertex:
                    return new_path
                stack.push(new_path)

                
        # make an array 
    
        # add the start-vertex to that array 

        #
        # for loop on the neighbors

    def dfs_recursive(self, starting_vertex, destination_vertex, visited= None, path= None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        #last_vertex = vertex_path[-1]
        if path is None:
            path = []
        visited.add(starting_vertex)
        new_path = path + [starting_vertex] # this makes the copy of the path.
        
        print(new_path)
        
    
        if starting_vertex == destination_vertex:
            return new_path
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
               found = self.dfs_recursive(neighbor, destination_vertex, visited, new_path) 
               if found:
                   return found
        

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
    print("graph.dft(1)")
    graph.dft(1)
    print("graph.dft_recursive(1)")
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