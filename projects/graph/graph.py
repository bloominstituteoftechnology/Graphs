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
        # This will hold the edges
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            # There's an edge from v1 to v2
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vert")

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
        # Init: enqueue the starting node
        q.enqueue(starting_vertex)
        # Create a set to store visited nodes
        visited = set()
        # While the queue isn't empty
        while q.size() > 0:
            # Dequeue the first item
            currentNode = q.dequeue()
            # If it's not been visited:
            if currentNode not in visited:
                # Do something with the node
                print(currentNode)
                # Add all neighbors to the queue
                visited.add(currentNode)
                # Add all neighbors to the queue
                for nextNode in self.get_neighbors(currentNode):
                    if nextNode not in visited:
                        q.enqueue(nextNode)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Create a set to store visited nodes
        visited = set()
        # Init: Push the starting node
        s.push(starting_vertex)
        # While the stack isn't empty
        while s.size() > 0:
            # Pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Add all neighbors to the stack
                visited.add(v)
                # Do something with the node
                print(v)
                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Add current node to visited
        visited.add(starting_vertex)
        # Print current node
        print(starting_vertex)
        # Save all current node neighbors to a variable
        neighbors = self.get_neighbors(starting_vertex)
        # While the current node has neighbors
        while len(neighbors) > 0:
            # For each neighnbor
            for each in neighbors:
                # If it has not been visited already
                if each not in visited:
                    # Rerun the function, replacing the current node with the neighbor
                    self.dft_recursive(each, visited)
                # If it has been visited
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create empty queue
        q = Queue()
        # Enqueue the starting node
        q.enqueue([starting_vertex])
        # Create a set for visited vertices
        visited = set()
        # While queue is not empty
        while q.size() > 0:
            # Create current path variable set to first node in q
            currentPath = q.dequeue()
            # Set the last node in the currentPath to a variable
            lastNode = currentPath[-1]
            # If it hasnt been visited
            if lastNode not in visited:
                # Check if it is the destination
                if lastNode == destination_vertex:
                    # Return the path if it is
                    return currentPath
                # If it is not the target
                else:
                    # Add the lastNode to visited
                    visited.add(lastNode)
                    # Set the lastNode neighbors to variable
                    neighbors = self.get_neighbors(lastNode)
                    # For each of lastNodes neighbors
                    for neighbor in neighbors:
                        # Copy the path current path
                        copy = currentPath[:]
                        # Add the neighbor
                        copy.append(neighbor)
                        # Add the copy to the q
                        q.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create empty stack
        s = Stack()
        # Push the starting node
        s.push([starting_vertex])
        # Create a set for visited vertices
        visited = set()
        # While stack is not empty
        while s.size() > 0:
            # Create current path variable set to first node in s
            currentPath = s.pop()
            # Set the last node in the currentPath to a variable
            lastNode = currentPath[-1]
            # If it hasnt been visited
            if lastNode not in visited:
                # Check if it is the destination
                if lastNode == destination_vertex:
                    # Return the path if it is
                    return currentPath
                # If it is not the target
                else:
                    # Add the lastNode to visited
                    visited.add(lastNode)
                    # Set the lastNode neighbors to variable
                    neighbors = self.get_neighbors(lastNode)
                    # For each of lastNodes neighbors
                    for neighbor in neighbors:
                        # Copy the path current path
                        copy = currentPath[:]
                        # Add the neighbor
                        copy.append(neighbor)
                        # Add the copy to the s
                        s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=Stack(), visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Create a path, this will be None the first time this function runs
        currentPath = path.pop()
        # If currentPath is None
        if currentPath == None:
            # Make currentPath the starting vertex
            currentPath = [starting_vertex]
        # Check if the last node in the currentPath is not in visited
        if currentPath[-1] not in visited:
            # Add the last node to visited
            visited.add(currentPath[-1])
            # For each of the last nodes neighbors
            for neighbor in self.get_neighbors(currentPath[-1]):
                # If the neighbor is the destination
                if neighbor == destination_vertex:
                    # Append that neighbor to the currentPath
                    currentPath.append(neighbor)
                    # Return the currentPath
                    return currentPath
                # Create a copy of the currentPath
                copy = currentPath.copy()
                # Add the neighbor to the copy
                copy.append(neighbor)
                # Push the copy to the reoccuring path
                path.push(copy)
            # Rerun the function with updated values
            return self.dfs_recursive(starting_vertex, destination_vertex, path, visited)


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
