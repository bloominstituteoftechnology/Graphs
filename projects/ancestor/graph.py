"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        # A: {},
        # B: {},
        # C: {},
        # D: {}

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
        # Create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # Create a Set for visited_vertices
        visited_vertices = set()

        # While the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if its not been visited
            if current_vertex not in visited_vertices:
            #     print the vertex 
                print(current_vertex)
            #     mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
            #     add all neightbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # Create a Set for visited_vertices
        visited_vertices = set()

        # While the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex from the stack
            current_vertex = plan_to_visit.pop()
            # if its not been visited
            if current_vertex not in visited_vertices:
            #     print the vertex 
                print(current_vertex)
            #     mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
            #     add all neightbors to the stack
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
        # Create an empty queue, and enqueue a PATH to the starting vertex
        daQueue = Queue()
        daQueue.enqueue([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the queue is not empty
        while daQueue.size() > 0:
            # dequeue the first PATH
            path = daQueue.dequeue()
            # grab the last vertex in the path

            # of it hasnt been visited
            if path[-1] not in visited_vertices:
                # check if its the target
                if path[-1] == destination_vertex:
                    # return the path if it is
                    return path
                # mark it as visited
                visited_vertices.add(path[-1])
                # make new versions fo the current path, with each neighbor added to them
                for next_vert in self.get_neighbors(path[-1]):
                    # duplicate the path
                    new_path = list(path)
                    # add the neighbor
                    new_path.append(next_vert)
                    # add the new path to the queue
                    daQueue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue, and enqueue a PATH to the starting vertex
        daQueue = Stack()
        daQueue.push([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the queue is not empty
        while daQueue.size() > 0:
            # dequeue the first PATH
            path = daQueue.pop()
            # grab the last vertex in the path

            # of it hasnt been visited
            if path[-1] not in visited_vertices:
                # check if its the target
                if path[-1] == destination_vertex:
                    # return the path if it is
                    return path
                # mark it as visited
                visited_vertices.add(path[-1])
                # make new versions fo the current path, with each neighbor added to them
                for next_vert in self.get_neighbors(path[-1]):
                    # duplicate the path
                    new_path = list(path)
                    # add the neighbor
                    new_path.append(next_vert)
                    # add the new path to the queue
                    daQueue.push(new_path)

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
