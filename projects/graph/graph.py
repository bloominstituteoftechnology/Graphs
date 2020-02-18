"""
Simple graph implementation
"""
# A small change to make a pull request
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
            raise IndexError("That vertex does not exist!")

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
        # Create an empty queue
        q = Queue()
        # Add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        print("bft:")
        while (q.size() > 0):
            # Dequeue, the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it has not been visited...
            if (v not in visited):
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        print("dft:")
        while (s.size() > 0):
            # pop, the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if (v not in visited):
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # Check if the node is visited
        # If not
        if (starting_vertex not in visited):
            # Mark it as visited
            visited.add(starting_vertex)
            # print
            print(starting_vertex)
            # call dft_recursive on each child
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
 

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH to the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while(q.size() > 0):
            # Dequeue, the first PATH
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            end = path[-1]
            # CHECK IF IT'S THE TARGET
            if (end == destination_vertex):
                # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            # If it has not been visited...
            if (end not in visited):
                # Mark it as visited
                visited.add(end)
                # Then add A PATH TO all neighbors to the back of the queue
                for neighbor in self.get_neighbors(end):
                    new_path = path + [neighbor]
                    q.enqueue(new_path)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        s = Stack()
        # Add A PATH to the starting vertex_id to the stack
        s.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while(s.size() > 0):
            # pop, the first PATH
            path = s.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            end = path[-1]
            # CHECK IF IT'S THE TARGET
            if (end == destination_vertex):
                # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            # If it has not been visited...
            if (end not in visited):
                # Mark it as visited
                visited.add(end)
                # Then add A PATH TO all neighbors to the front of the stack
                for neighbor in self.get_neighbors(end):
                    new_path = path + [neighbor]
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()

        if (starting_vertex == destination_vertex):
            return [destination_vertex]
        
        # Check if the node is visited
        # If not
        if (starting_vertex not in visited):
            # Mark it as visited
            visited.add(starting_vertex)
            # call dft_recursive on each child
            for neighbor in self.get_neighbors(starting_vertex):
                path = self.dfs_recursive(neighbor, destination_vertex, visited)
                if path:
                    return [starting_vertex] + path
            
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
    print("RECURSION")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("BFS")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("DFS")
    print(graph.dfs(1, 6))
    print("RECURSION")
    print(graph.dfs_recursive(1, 6))
