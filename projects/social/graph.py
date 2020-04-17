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
        v1_edges_set = self.vertices[v1]

        v1_edges_set.add(v2)

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
        # create an empty queue
        q = Queue()
        # enqueue the starting_vertex
        q.enqueue(starting_vertex)
        # create a set to track vertices we have visited
        visited = set()
        # while the queue isn't empty:
        while q.size() > 0:
        ## dequeue, this is our current_node
            current_node = q.dequeue()
        ## if we haven't visited it yet
            if current_node not in visited:
                print(current_node)
                ## mark as visited
                visited.add(current_node)
                ## get its neighbors
                neighbors = self.get_neighbors(current_node)
                ## and add each to the back of queue
                for neighbor in neighbors:
                    q.enqueue(neighbor)
                    # return visited
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack
        stack = Stack()
        # push the starting_vertex onto the stack
        stack.push(starting_vertex)
        # create a visited set
        visited = set()
        # while our stack isn't empty:
        while stack.size() > 0:
        ## pop off what's on top, this is our current_node
            current_node = stack.pop()
        ## if it hasn't been visited:
            if current_node not in visited:
                print(current_node)
                ### mark it as visited
                visited.add(current_node)
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### and add each neighbor to the top of the stack
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        visited = set()
        def dft_inner_recursion(vertex):
            if vertex in visited:
                return
            visited.add(vertex)
            print(vertex)
            for point in self.vertices[vertex]:
                dft_inner_recursion(point)

        dft_inner_recursion(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue
        q = Queue()
        # enqueue path to the starting vertex
        q.enqueue([starting_vertex])
        # create a set to track vertices we have visited
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            current_path = q.dequeue()
            # get last vertex from the path
            last_vertex = current_path[-1]
            # if vertex has not been visited:
            if last_vertex not in visited:
                # check the destination
                if last_vertex == destination_vertex:
                    return current_path
                # mark is as visited
                visited.add(last_vertex)
                # add a path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:
                    # clone path
                    new_path = [*current_path]
                # add neighbor to the back of the queue
                    new_path.append(v)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack
        stack = Stack()
        # push the starting_vertex id onto the stack
        stack.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty
        while stack.size() > 0:
            # dequeue the first path
            current_path = stack.pop()
            # get the last vertex from the path
            last_vertex = current_path[-1]
            # it has not been visited:
            if last_vertex not in visited:
                # check destination
                if last_vertex == destination_vertex:
                    return current_path
                # mark it as visited
                visited.add(last_vertex)
                # add path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:

                    # clone path
                    new_path = [*current_path]

                # add neighbor to the back of the queue
                    new_path.append(v)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        visited = set()
        path = []

        def dfs_inner_recursion(starting_vertex, destination_vertex, path):
            if starting_vertex in visited:
                return path
            elif starting_vertex == destination_vertex:
                path.append(starting_vertex)
                return path
            visited.add(starting_vertex)
            for v in self.vertices[starting_vertex]:
                if destination_vertex in dfs_inner_recursion(v, destination_vertex, path):
                    path.append(starting_vertex)
                    return path
            return path

        out_path = dfs_inner_recursion(starting_vertex, destination_vertex, path)
        # return reverse array
        return out_path[::-1]

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