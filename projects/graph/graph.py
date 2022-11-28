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
        # create a queue
        queue = Queue()

        # initialize queue with starting node
        queue.enqueue(starting_vertex)

        # create a set to keep track of visited node
        visited = set()

        while queue.size() > 0:

            # get next node in line
            current_node = queue.dequeue()

            # process current node if it hasn't been visited yet
            if current_node not in visited:
                print(current_node)

                # mark current node as visited
                visited.add(current_node)

                # add all neighbors to queue
                for neighbor in self.get_neighbors(current_node):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack
        stack = Stack()

        # initialize stack with starting node
        stack.push(starting_vertex)

        # create a set to keep track of visited node
        visited = set()

        while stack.size() > 0:

            # get next node in line
            current_node = stack.pop()

            # process current node if it hasn't been visited yet
            if current_node not in visited:
                print(current_node)

                # mark current node as visited
                visited.add(current_node)

                # add all neighbors to stack
                for neighbor in self.get_neighbors(current_node):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        def dft_helper(starting_vertex):

            if starting_vertex not in visited:
                print(starting_vertex)

                # mark current node as visited
                visited.add(starting_vertex)

                # process all neighboors recursively
                for neighboor in self.get_neighbors(starting_vertex):
                    dft_helper(neighboor)

        visited = set()

        dft_helper(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue to hold vertices to traverse
        queue = Queue()

        # initialize queue with starting vertex
        queue.enqueue(starting_vertex)

        # use a dictionary to keep track of visited vertices and their path from the starting node
        paths_to_vertices = dict()
        paths_to_vertices[starting_vertex] = []

        # use a set to keep track of visited vertices
        visited_nodes = set()

        while queue.size() > 0:

            # get next vertex in line
            current_vertex = queue.dequeue()

            # process current vertex if it hasn't been visited yet
            if current_vertex not in visited_nodes:

                # mark current vertex as visited and store its path at the same time
                visited_nodes.add(current_vertex)

                # inspect all the neighbors of the current vertex
                for neighbor in self.get_neighbors(current_vertex):

                    # if the target vertex is one of the neighbors, the search is done
                    # right now paths_to_vertices[current_vertex] only contains all the vertices up to and including the parent vertex
                    # to return the full path, add both the current vertex and the target vertex first.
                    if neighbor == destination_vertex:
                        final_path = paths_to_vertices[current_vertex][:]
                        final_path.append(current_vertex)
                        final_path.append(neighbor)
                        return final_path

                    # add all the other neighbors to the queue
                    queue.enqueue(neighbor)

                    # store a copy of the current path for each of the neighbors
                    # take the path leading to current_vertex and add current_vertex to it
                    # make a copy in order to not modify the original
                    copy_of_path_to_parent = paths_to_vertices[current_vertex][:]
                    copy_of_path_to_parent.append(current_vertex)

                    # store path in dictionary
                    paths_to_vertices[neighbor] = copy_of_path_to_parent

        # target not found
        print("Vertex", destination_vertex, "was not found.")
        return

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a queue to hold vertices to traverse
        stack = Stack()

        # initialize stack with starting vertex
        stack.push(starting_vertex)

        # use a dictionary to keep track of visited vertices and their path from the starting node
        paths_to_vertices = dict()
        paths_to_vertices[starting_vertex] = []

        # use a set to keep track of visited vertices
        visited_nodes = set()

        while stack.size() > 0:

            # get next vertex in line
            current_vertex = stack.pop()

            # process current vertex if it hasn't been visited yet
            if current_vertex not in visited_nodes:

                # mark current vertex as visited and store its path at the same time
                visited_nodes.add(current_vertex)

                # inspect all the neighbors of the current vertex
                for neighbor in self.get_neighbors(current_vertex):

                    # if the target vertex is one of the neighbors, the search is done
                    # right now paths_to_vertices[current_vertex] only contains all the vertices up to and including the parent vertex
                    # to return the full path, add both the current vertex and the target vertex first.
                    if neighbor == destination_vertex:
                        final_path = paths_to_vertices[current_vertex][:]
                        final_path.append(current_vertex)
                        final_path.append(neighbor)
                        return final_path

                    # add all the other neighbors to the stack
                    stack.push(neighbor)

                    # store a copy of the current path for each of the neighbors
                    # take the path leading to current_vertex and add current_vertex to it
                    # make a copy in order to not modify the original
                    copy_of_path_to_parent = paths_to_vertices[current_vertex][:]
                    copy_of_path_to_parent.append(current_vertex)

                    # store path in dictionary
                    paths_to_vertices[neighbor] = copy_of_path_to_parent

        # target not found
        print("Vertex", destination_vertex, "was not found.")
        return

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def dfs_helper(starting_vertex, destination_vertex, path_so_far):

            # process current vertex if it hasn't been visited yet
            if starting_vertex not in visited_nodes:

                visited_nodes.add(starting_vertex)

                # if the vertex has been found elsewhere, stop recursion
                if node_found:
                    return

                elif starting_vertex == destination_vertex:
                    final_path = path_so_far[:]
                    final_path.append(starting_vertex)

                    # add answer to dictionary to be returned
                    answer[destination_vertex] = final_path

                else:
                    for neighbor in self.get_neighbors(starting_vertex):
                        new_path = path_so_far[:]
                        new_path.append(starting_vertex)
                        dfs_helper(neighbor, destination_vertex, new_path)

        # create a set to keep track of visited vertices
        visited_nodes = set()

        # create a flag to deteremine whether to continue recursion
        node_found = False

        # create a variable to hold the answer
        answer = dict()

        dfs_helper(starting_vertex, destination_vertex, [])

        return answer[destination_vertex]


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
