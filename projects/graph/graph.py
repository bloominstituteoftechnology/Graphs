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
            print("error, no verticies found")
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex): # acylical (visit all neighbors one by one then move onto the next node and its neighbors  )
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # how can we keep track of what nodes are up next?  
        # create empty queue & starting_vertex 
        queue = []
        queue.append(starting_vertex)
        # this will keep track of all the next_to_visit_vertices
        visited = set() 
        # set() helps keep us organized when searching for visited vertices 
        #      vertice(s): edge(s) pairs 
        # while the queue is not empty:
        while len(queue) > 0:
        #   pop or dequeue the vertex of the queue:
            cur_vertex = queue.pop(0) #pop the "first" item 
        #   if vertex not in visited_vertices:
            if cur_vertex not in visited:
            #   print it 
                print(cur_vertex)
            #   add the vertex to the visited set()
                visited.add(cur_vertex)
            #   add all neighbors to the queue
                for neighbor in self.get_neighbors(cur_vertex):
                    queue.append(neighbor)

        
        
        

    def dft(self, starting_vertex): # cyclical (unordered using a stack (FirstInLastOut) )
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack & starting_vertex 
        stack = []
        stack.append(starting_vertex)
        # this will keep track of all the next_to_visit_vertices
        visited = set() 
        # set() helps keep us organized when searching for visited vertices 
        #      vertice(s): edge(s) pairs 
        # while the stack is not empty:
        while len(stack) > 0:
        #   pop or destack the vertex of the stack:
            cur_vertex = stack.pop() #pop the "last" item 
            if cur_vertex not in visited:
            #   print it 
                print(cur_vertex)
            #   add the vertex to the visited set()
                visited.add(cur_vertex)
            #   add all neighbors to the stack
                for neighbor in self.get_neighbors(cur_vertex):
                    stack.append(neighbor)
            

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # normal bft operations until we find the goal vertex
        # and return an array of vertex IDs that are part of the PATH
        # create an empty queue AND add a "PATH" to starting_vertex
        # add arr[1] to the queue 

        # create visited set ....its empty for now 
        # while queue is not empty:
            # pop off the current path from the queue 
            
            # get the cur_vertex to anaylize from the PATH 
            # use the vertex at the end of the path array 
            
            # if vertex not visited:
                #   then add vertex to visited list 
                # check if cur_vertex is the target vertex
                    # we found the vertex and its paired PATH 
                    # return to PATH 
            
            # for each neigbhor of the cur_vertex:
                # add the PATH to that neighbor to the -> queue 
                    # copy the current PATH 
                    # add neighbor to new PATH
                    # add the whole PATH to the --> queue 
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            cur_path = queue.dequeue()
            last_vertex = cur_path[-1]
        if last_vertex not in visited:
            visited.add(last_vertex)
        for neighbor in self.get_neighbors(last_vertex):
            next_path = cur_path
            next_path.append(neighbor)
        if neighbor == destination_vertex:
            return next_path
        else:
            queue.enqueue(next_path)
            

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
            cur_path = stack.pop()
            last_vertex = cur_path[-1]
        if last_vertex not in visited:
            visited.add(last_vertex)
        for neighbor in self.get_neighbors(last_vertex):
            next_path = cur_path
            next_path.append(neighbor)
        if neighbor == destination_vertex:
            return next_path
        else:
            stack.push(next_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

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
    print('bft1')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft1')

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
