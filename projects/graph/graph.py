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
        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 not in self.vertices:
            raise IndexError(f'Vertex {v1} does not exist!')
        elif v2 not in self.vertices:
            raise IndexError(f'Vertex {v2} does not exist!')
        

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
        # enqueue our starting node (we can start anywhere in our tree)
        q.enqueue(starting_vertex)

        # keep track if we visited already that node
        # make a set to track this
        visited = set()

        # while our queue isn't empty
        while q.size() > 0:
            # dequeue whatever's at the fron of our line, this is our current_node
            current_node = q.dequeue()

            # if we haven't visited this node yet,
            if current_node not in visited:
                print(current_node)
                # marks as visited
                visited.add(current_node)
                # print the vertex (node)
                # get it's neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                for neighbor in neighbors:
                    # add to the queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on our starting vertex
        s.push(starting_vertex)

        # make a set to track if we've been here before
        visited = set()

        # while our stack is not empty
        while s.size() > 0:
            # pop off whatever is on top, this is current_node
            current_node = s.pop()

            # if we haven't visited this vertex vefore
            if current_node not in visited:
                # run function / print
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                for neighbor in neighbors:
                    # add to our stack
                    s.push(neighbor)
       
    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # if node hasn't been visited
        if starting_vertex not in visited:
            # mark as visited
            visited.add(starting_vertex)
            # print
            print(starting_vertex)

            # for each of node's neighbors
            for neighbor in self.vertices[starting_vertex]:
                # recurse
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Instantiate an empty queue
        q = Queue()
        # enqueue a path to the starting vertex
        q.enqueue([starting_vertex])
        # create a set to track visited nodes
        visited = set()

        # while queue not empty
        while q.size() > 0:
            # dequeue the path
            path = q.dequeue()
            # get the last vertex from the path
            node = path[-1]
            
            # if the node hasn't been visited
            if node not in visited:
                # return the path if the node is our target
                if node == destination_vertex:
                    return path
                # mark the node as visited
                visited.add(node)

                # add a path to its neighbors to the back of the queue
                for neighbor in self.vertices[node]:
                    # copy the path
                    new_path = path.copy()
                    # append the neighbor to the back
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # instantiate a stack
        s = Stack()
        # push a path to the starting vertex
        s.push([starting_vertex])
        # create a set to keep track of all visited nodes
        visited = set()

        # while stack is not empty
        while s.size() > 0:
            # pop the first path
            path = s.pop()
            # get the last vertex from the path
            node = path[-1]

            # if the node hasn't been visited
            if node not in visited:
                # is it our target?
                if node == destination_vertex:
                    # if yes, return path
                    return path
                
                # mark the node as visited
                visited.add(node)

                # add a path to its neighbors
                for neighbor in self.vertices[node]:
                    # copy the path
                    new_path = path.copy()
                    # append the neighbor
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # add the starting node in the visited set
        visited.add(starting_vertex)
        # add the node in path
        path = path + [starting_vertex]
        # base case
        # is the node our target?
        if starting_vertex == destination_vertex:
            # if yes, return
            return path
        # for each node's neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            # is the node visited?
            if neighbor not in visited:
                # if no, recurse and get the new path
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # is the new path None?
                if new_path is not None:
                    # if not none, return
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
    # print(graph.vertices)

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
    # graph.bft(1)

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
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))