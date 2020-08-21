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
        # Create the new key with the vertex ID, and set the value to an empty set (meaning no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find vertex V1 in our vertices, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError(f'vertex {v1} and/or {v2} not in vertices')
        #pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #pass  # TODO
        if vertex_id not in self.vertices:
            raise IndexError(f'vertex {vertex_id} does not exist')
        else:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        ques = Queue()
        # enqueue our starting node
        ques.enqueue(starting_vertex)
        # make a set to track if we have been here before
        visited = set()
        # while our queue is not empty
        while ques.size() > 0:
            # dequeue whatever is in the front of our line, this is our current node
            curr = ques.dequeue()
        # if we have not visited this node yet,
            if curr not in visited:
                # mark as visited
                print(curr)
                visited.add(curr)
        # get its neighbors
                neighbors = self.get_neighbors(curr)
        # for each of its neighbors
                for neighbor in neighbors:
                    # add to queue
                    ques.enqueue(neighbor)
           

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #pass  # TODO
        # create the stack
        node_stack = Stack()
        # push the starting node
        node_stack.push(starting_vertex)
        # create set to track
        visited = set()
        # while the stack is not empty
        while node_stack.size() > 0:
            curr = node_stack.pop()
            if curr not in visited:

                print(curr)
                visited.add(curr)
                # get the neighbors involved
                neighbors = self.get_neighbors(curr)

                for neighbor in neighbors:
                    node_stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        #pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        ques = Queue()
        # enqueue a PATH to the starting vertex
        ques.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty:
        while ques.size() > 0:
            # Dequeue the first PATH and set it to current
            curr = ques.dequeue()
            # Grab the last vertex from the PATH
            vertex = curr[-1]
            # If that vertex has not been visited:
            if vertex not in visited:
                # Check if it's the target
                if vertex == destination_vertex:
                    # Return PATH
                    return curr
                # Mark as visited
                visited.add(vertex)
                # Add a PATH to its neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    # Copy path because different paths are added
                    path = curr.copy()
                    # Append neighbor - append returns None
                    path.append(neighbor)
                    ques.enqueue(path)


        #pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

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
