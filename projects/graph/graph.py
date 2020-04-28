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
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)

        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:

            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()

            # if its not been visited
            if current_vertex not in visited_vertices:

                # print the vertex
                print(current_vertex)

                # mark it as visited, (add it to visited_vertices)   
                visited_vertices.add(current_vertex)

                # add all unvisited neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)

        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:

            # pop the first vertex from the stack
            current_vertex = plan_to_visit.pop()

            # if its not been visited
            if current_vertex not in visited_vertices:

                # print the vertex
                print(current_vertex)

                # mark it as visited, (add it to visited_vertices)   
                visited_vertices.add(current_vertex)

                # add all unvisited neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Initial Case
        if visited is None:
            visited = set()

        # Track visited vertices
        visited.add(starting_vertex)

        # Print vertex
        print(starting_vertex)

        # Call the function on neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a empty queue, and enqueue a PATH to the starting vertex (list)
        plan_to_visit = Queue()
        plan_to_visit.enqueue([starting_vertex])

        # create a set for visited vertices
        visited_vertices = set()
        paths = []

        # while the queue is not empty
        while plan_to_visit.size() > 0:

            # dequeue the first PATH
            path = plan_to_visit.dequeue()

            # grab the last vertex in the path
            current_vertex = path[-1]
            
            # if it hasn't been visited
            if current_vertex not in visited_vertices:

                # check if its the target
                if current_vertex == destination_vertex:
                    # Return the path
                    return path

                # mark it as visited
                visited_vertices.add(current_vertex)

                # make new versions of the current path, with each neighbor added to them
                for neighbor in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(path)
                    # add the neighbor
                    new_path.append(neighbor)
                    # add the new path to the queue
                    plan_to_visit.enqueue(new_path)
                    
        return None # return None is implied

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a plan_to_visit stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push([starting_vertex])

        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:

            # pop the first vertex from the stack
            path = plan_to_visit.pop()

            # Get current_vertex
            current_vertex = path[-1]

            # if its not been visited
            if current_vertex not in visited_vertices:

                # check if its the target
                if current_vertex == destination_vertex:
                    # Return the path
                    return path
                
                # mark it as visited, (add it to visited_vertices)   
                visited_vertices.add(current_vertex)

                # add all unvisited neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(path)
                    # add the neighbor
                    new_path.append(neighbor)
                    # add the new path to the queue
                    plan_to_visit.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # Initial Case
        if visited is None:
            visited = set()
        if path is None:
            path = []

        # Track visited vertices
        visited.add(starting_vertex)

        # Add to path
        path = path + [starting_vertex]

        # If at destination_vertex return the path
        if starting_vertex == destination_vertex:
            return path

        # Call the function on neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                # Look for a path
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # Return only if there is a path
                if neighbor_path:
                    return neighbor_path

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
    print("- Vertices -")
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
    print("- BFT Paths -")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("- DFT Paths -")
    graph.dft(1)
    print("- DFT Paths Recursive -")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("- BFS shortest path -")
    print("Expecting: [1, 2, 4, 6]")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("- DFS path -")
    print("Expecting: [1, 2, 4, 6] or [1, 2, 4, 7, 6]")
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))