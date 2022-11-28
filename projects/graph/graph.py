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
        # make a queue
        q = Queue()
        # enqueue our starting a node
        q.enqueue(starting_vertex)
        # make a set to track if we've been at that node before 
        visited = set()
 
        # while our q isn't empty
        while q.size() > 0:
        ## dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
        ## if we haven't visited this node yet.
            if current_node not in visited:
                print(current_node)
        ### mark as visited
                visited.add(current_node)
        ### print node or vertex
        
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors,
                for neighbor in neighbors:           
        ### ad to q
                    q.enqueue(neighbor)

        # note - breadth first search guaranteed to give you shortest path between 2 nodes in any unweighted graph.

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)

        # made a set to track if we've been here before
        visited = set()

        # while our stack isn't empty
        while s.size() > 0:
        ## pop off whaterver's on top, this is current_node
            current_node = s.pop()
        ## if we haven't visited this vertex (aka node) before
            if current_node not in visited:
                print(current_node)
                ### mark as visited
                visited.add(current_node)
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
            ### for each of the neighbors,
                for neighbor in neighbors:           
            #### add to the stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # recursion does stack funcionality for us.  No stack needed

        if visited is None:
            visited = set()

        # mark start vertex as visited
        visited.add(starting_vertex)

        # print it
        print(starting_vertex)

        # get neighbors
        neighbors = self.get_neighbors(starting_vertex)

        # Base case is implicit.  
        # When length of neighbors is 0, then we finish for loop below.
        # In python this means we return even if not explicitly called.
        
        # for each neighbor
        for neighbor in neighbors:
            ## if not visited
            if neighbor not in visited:
            ### recurse on the neighbor
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # enqueue our starting a node

        path = [starting_vertex]
        q.enqueue(path)
        # make a set to track if we've been at that node before 
        visited = set() 

        # while q is not empty
        while q.size() > 0:

        ## dequeue path at the front of our line
            current_path = q.dequeue()
            current_node = current_path[-1] # last item in list of nodes in our path.

        ### it this is our destination_vertex (or search node), return our current path
            if current_node == destination_vertex:
                return current_path

        ### if we haven't visited this node yet.
            if current_node not in visited:
        ### mark node as visited
                visited.add(current_node)
        ### get the node's neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors
                for neighbor in neighbors:           
        #### add it to queue
                    q.enqueue(current_path + [neighbor])
                    #### alt way to add to our list of node's in our current path
                    # path_copy = current_path[:]
                    # path_copy.append(neighbor)
                    # q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make list to track if we've been here before
        visited = []

        # while our stack isn't empty
        while s.size() > 0:
        ## pop off whaterver's on top, this is current_node
            current_node = s.pop()
        ## if we haven't visited this vertex (aka node) before
            if current_node not in visited:
                ### mark as visited
                visited.append(current_node)
                ### if we've found out search term, return path.
                if current_node == destination_vertex:
                    return visited
                ### if no return, get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### for each of the neighbors,
                for neighbor in neighbors:           
                    #### add to the stack
                    s.push(neighbor)

    def dfs_recursive(self, vertex, destination_vertex, path=None, visited=None):
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

        ## mark our node as visited
        visited.add(vertex)

        # append our initial or starting vertex to path
        # if len(path) == 0:
        #     path.append(vertex)

        path = path + [vertex] # makes a copy of the path that persists between calls

        ## check if it's our target node, if so return
        if vertex == destination_vertex:
            return path
 
        ## get neighbors
        neighbors = self.get_neighbors(vertex)

        ## iterate over neighbors
        for neighbor in neighbors:
        ### check if visited
            if neighbor not in visited:
        #### if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path, visited)
        #### if this recrusion returns a path
                if result is not None:
        ##### return that path
                    return result

        return None

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
