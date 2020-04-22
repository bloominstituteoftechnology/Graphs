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
            raise IndexError('that vertex does not exist')

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
        # create a plan_to_visit queue and add starting_vertex
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create set for visiting verticies
        visited_vertices = set()
        # while plan_to_visit is not empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if it has not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark as visited, (add to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neghbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit stack and add starting_vertex
        print('DFT')
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create set for visiting verticies
        visited_vertices = set()
        # while plan_to_visit is not empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex on the stack
            current_vertex = plan_to_visit.pop()
            # if it has not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark as visited, (add to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neghbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

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
        # create and empty queue, and enqueue a path to the starting vertex
        print('************BFS***********')
        bft_path = Queue()
        # queue.enqueue([starting_vertex])
        bft_path.enqueue([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while queue is not empty
        while bft_path.size() > 0:
            # dequeue the first Path
            curr_path = bft_path.dequeue()
            # grab the last vertex in the path
            curr_path_last_vertex = curr_path[-1]
            # if it hasnt been visited
            if curr_path_last_vertex not in visited_vertices:
                # check if its the target
                if curr_path_last_vertex == destination_vertex:
                    # return the path if it is
                    return curr_path
                # mark it as visited if it is not
                else:
                    visited_vertices.add(curr_path_last_vertex)
                    neighbors = self.get_neighbors(curr_path_last_vertex)
                # make new versions of the the current path with each neighbor added to them
                    for neighbor in neighbors:
                        # duplicate the path
                        curr_path_copy = curr_path[:]
                        # add the neighbor
                        curr_path_copy.append(neighbor)
                        # add the new path
                        bft_path.enqueue(curr_path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        print('************DFS************')
        # create an empty stack
        dfs_path = Stack()
        # path to starting vertex
        dfs_path.push([starting_vertex])
        # set for visited vetices
        visited_vertices = set()
        # while path is not empty
        while dfs_path.size() > 0:
            # pop the first path
            curr_path = dfs_path.pop()
            # take last vertex in path
            curr_path_last_vertex = curr_path[-1]
            # if we havent been there yet
            if curr_path_last_vertex not in visited_vertices:
                # check if current is the destination
                if curr_path_last_vertex == destination_vertex:
                    # return the path if it is
                    return curr_path
                # mark as visited if it is not
                else:
                    # get the neighbors / make new versions on the path
                    visited_vertices.add(curr_path_last_vertex)
                    neighbors = self.get_neighbors(curr_path_last_vertex)
                    for neighbor in neighbors:
                        # duplicate the path
                        curr_path_copy = curr_path[:]
                        # add the neighbor
                        curr_path_copy.append(neighbor)
                        # add the new path
                        dfs_path.push(curr_path_copy)

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
