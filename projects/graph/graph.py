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
            raise IndexError('That vertex does not exist.')

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
        # create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # create an empty Set to store visited vertices
        visited = set()
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been visited...
            if v not in visited:
                # mark it as visited
                print(v)
                visited.add(v)
                # then add all of its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # create a Set to store visited vertices
        visited = set()
        # while the stack is not empty...
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited...
            if v not in visited:
                # mark it as visited...
                print(v)
                visited.add(v)
                # then add all of its neighbors to the top if the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check if visited had been initialized
        if visited is None:
            visited = set()
        # mark the node as visited
        print(starting_vertex)
        visited.add(starting_vertex)
        # call dft recursive on each neighbor that has not been visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the queue id not empty...
        while q.size() > 0:
            # dequeue the first PATH
            v_path = q.dequeue()
            # grab the last vertex from the PATH
            v = v_path[-1]
            # if that last vertex has not been visited...
            if v not in visited:
                # check if it's the target
                if v is destination_vertex:
                    # if so return path
                    return v_path
                # mark it as visited...
                visited.add(v)
                # then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    # copy the PATH
                    path_copy = v_path.copy()
                    # append the neighbor to the back
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty...
        while s.size() > 0:
            # dequeue the first PATH
            v_path = s.pop()
            # grab the last vertex from the PATH
            v = v_path[-1]
            # if that last vertex has not been visited...
            if v not in visited:
                # check if it's the target
                if v is destination_vertex:
                    # if so return path
                    return v_path
                # mark it as visited...
                visited.add(v)
                # then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    # copy the PATH
                    path_copy = v_path.copy()
                    # append the neighbor to the back
                    path_copy.append(neighbor)
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initiate visited
        if visited is None:
            visited = set()
        # init path
        visited.add(starting_vertex)
        if path is None:
            path = []
        # add vertex to the path
        path += [starting_vertex]
        # if we are at the target value, return the path
        if starting_vertex is target_vertex:
            return path
        # otherwise, call DFS_recursive on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, target_vertex, visited, path)
                if new_path is not None:
                    return new_path
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
    print('~~~~~~~~~~~~~~~~ BFT ~~~~~~~~~~~~~~')
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('~~~~~~~~~~~~~~~~ DFT ~~~~~~~~~~~~~~')
    # graph.dft(1)
    print('~~~~~~~~~~~~~~~~ DFT recursive ~~~~~~~~~~~~~~')
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('~~~~~~~~~~~~~~~~ BFS ~~~~~~~~~~~~~~')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('~~~~~~~~~~~~~~~~ DFS ~~~~~~~~~~~~~~')
    print(graph.dfs(1, 6))
    print('~~~~~~~~~~~~~~~~ DFS recursive ~~~~~~~~~~~~~~')
    print(graph.dfs_recursive(1, 6))
