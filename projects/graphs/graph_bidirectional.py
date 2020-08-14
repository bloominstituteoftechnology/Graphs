"""
Simple graph implementation (as class Graph).
"""
# Import libraries, packages, modules, classes/functions:
from data_structures import Stack, Queue


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges (an adjacency list)."""
    def __init__(self):
        # Initiate as empty adjacency list:
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        """
        Add vertex_id as a vertex in the graph.
        """
        # Check to make sure the provided vertex isn't already in the graph:
        if vertex_id not in self.vertices:
            # Add it:
            self.vertices[vertex_id] = set()
        else:
            raise IndexError(f"Vertex {vertex_id} is already in the graph!")

    def add_edge(self, v1, v2):
        """
        Add a bidirectional edge to the graph, from vertex v1 to v2.
        """
        # Make sure both vertices are in the graph before adding the edge that connects them:
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)  # Bidirectional
        else:
            raise IndexError("Vertex does not exist in graph!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighboring vertices (with connecting edges) of the given vertex in the graph.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        """
        Traverse and print each vertex in breadth-first order (a BFT) beginning from starting_vertex.
        """
        # Initialize empty queue and set of visited nodes:
        queue = Queue()
        visited = set()

        # Check if provided starting vertex is in our graph:
        if starting_vertex_id in self.vertices.keys():
            # If so, add starting vertex to queue:
            queue.enqueue(starting_vertex_id)
        else:
            return IndexError(f"Provided starting vertex {starting_vertex_id} does not exist in graph!")

        # Process all vertices via BFT:
        while queue.size() > 0:
            # Get next vertex to process as first item in queue:
            current_vertex = queue.dequeue()
            # If the current vertex has not already been visited+processed, process it:
            if current_vertex not in visited:
                # Process current vertex:
                print(current_vertex)
                # Add adjacent vertices to queue for future processing:
                for adjacent_vertex in self.get_neighbors(current_vertex):
                    queue.enqueue(adjacent_vertex)
                # Mark current vertex as "visited" by adding to our set of visited vertices:
                visited.add(current_vertex)

    def dft(self, starting_vertex_id):
        """
        Traverse and print each vertex in depth-first order (DFT) beginning from starting_vertex.
        """
        # Initialize empty stack and set of visited nodes:
        stack = Stack()
        visited = set()

        # Check if provided starting vertex is in our graph:
        if starting_vertex_id in self.vertices.keys():
            # If so, add starting vertex to stack:
            stack.push(starting_vertex_id)
        else:
            return IndexError(f"Provided starting vertex {starting_vertex_id} does not exist in graph!")

        # Process all vertices via BFT:
        while stack.size() > 0:
            # Get next vertex to process as first item in stack:
            current_vertex = stack.pop()
            # If the current vertex has not already been visited+processed, process it:
            if current_vertex not in visited:
                # Process current vertex:
                print(current_vertex)
                # Add adjacent vertices to stack for future processing:
                for adjacent_vertex in self.get_neighbors(current_vertex):
                    stack.push(adjacent_vertex)
                # Mark current vertex as "visited" by adding to our set of visited vertices:
                visited.add(current_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Traverse and print each vertex in depth-first order (DFT) beginning from starting_vertex. Recursive implementation.
        """
        # Placeholder until implemented recursively:
        return self.dft(starting_vertex)

    def bfs(self, starting_vertex, target_vertex):
        """
        Return a list containing the shortest path from starting_vertex to destination_vertex, 
        after searching for and finding it with a breadth-first search (BFS) algorithm.
        """
        # Initialize empty queue and set of visited nodes:
        queue = Queue()
        visited = set()

        # Initialize path (we will add the rest of the path from starting vertex to target vertex below):
        path = [starting_vertex]

        # Check if provided starting vertex is in our graph:
        if starting_vertex in self.vertices.keys():
            # If so, add starting vertex to queue:
            queue.enqueue(path)
        else:
            return IndexError(f"Provided starting vertex {starting_vertex} does not exist in graph!")

        # Process all vertices via BFT:
        while queue.size() > 0:
            # Get next vertex to process as first item in queue:
            current_path = queue.dequeue()
            current_vertex = current_path[-1]
            # If the current vertex has not already been visited+processed, check and process it:
            if current_vertex not in visited:
                # Check if it is the target --> if so, return its full path:
                if current_vertex == target_vertex:
                    return current_path
                # If not, then get its neighbor vertices and add their paths to the queue for future processing:
                for adjacent_vertex in self.get_neighbors(current_vertex):
                    adjacent_vertex_path = current_path + [adjacent_vertex]
                    queue.enqueue(adjacent_vertex_path)
                # Mark current vertex as "visited" by adding to our set of visited vertices:
                visited.add(current_vertex)
        
        # If no path found in entire graph, return None:
        return None

    def dfs(self, starting_vertex, target_vertex):
        """
        Return a list containing the shortest path from starting_vertex to destination_vertex, 
        after searching for and finding it with a depth-first search (DFS) algorithm.
        """
        # Initialize empty stack and set of visited nodes:
        stack = Stack()
        visited = set()

        # Initialize path (we will add the rest of the path from starting vertex to target vertex below):
        path = [starting_vertex]

        # Check if provided starting vertex is in our graph:
        if starting_vertex in self.vertices.keys():
            # If so, add starting vertex to stack:
            stack.push(path)
        else:
            return IndexError(f"Provided starting vertex {starting_vertex} does not exist in graph!")

        # Process all vertices via BFT:
        while stack.size() > 0:
            # Get next vertex to process as first item in stack:
            current_path = stack.pop()
            current_vertex = current_path[-1]
            # If the current vertex has not already been visited+processed, check and process it:
            if current_vertex not in visited:
                # Check if it is the target --> if so, return its full path:
                if current_vertex == target_vertex:
                    return current_path
                # If not, then get its neighbor vertices and add their paths to the stack for future processing:
                for adjacent_vertex in self.get_neighbors(current_vertex):
                    adjacent_vertex_path = current_path + [adjacent_vertex]
                    stack.push(adjacent_vertex_path)
                # Mark current vertex as "visited" by adding to our set of visited vertices:
                visited.add(current_vertex)
        
        # If no path found in entire graph, return None:
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from starting_vertex to destination_vertex, 
        after searching for and finding it with a depth-first search (DFS) algorithm. 
        Recursive implementation.
        """
        # Placeholder until implemented recursively:
        return self.dfs(starting_vertex, destination_vertex)

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

    # graph = Graph()  # Instantiate your graph
    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # graph.add_edge('0', '1')
    # graph.add_edge('1', '0')
    # graph.add_edge('0', '3')
    # graph.add_edge('3', '0')
    # print(graph.vertices)
    # # graph.add_edge('0', '4')  # Should throw IndexError.
