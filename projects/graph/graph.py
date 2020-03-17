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
            print("ERROR: Vertex does not exist")

    # def add_undirected_edge(self, v1, v2):
    #     """
    #     Add an undirected edge to the graph.
    #     Goes both ways
    #     """
    #     if v1 in self.vertices and v2 in self.vertices:
    #         self.vertices[v1].add(v2)
    #         self.vertices[v2].add(v1)
    #     else:
    #         print("ERROR: Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            # print("ERROR: Vertex does not exist")
            raise ValueError("Vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue
        q = Queue()
        # enqueue the starting vertex
        q.enqueue(starting_vertex)
        # create a set to store vistited vertices
        visited = set()
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first vertex
            temp = q.dequeue()
            # do the thing:
            # check if it's been visited and print if not
            if temp not in visited:
                # Mark it as visited and print
                print(temp)
                visited.add(temp)
                # enqueue all it's neighbors
                for neighbor in self.get_neighbors(temp):
                    q.enqueue(neighbor)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a STACK, otherwise same as above
        s = Stack()
        # push the starting vertex
        s.push(starting_vertex)
        # create a set to store vistited vertices
        visited = set()
        # while the stack is not empty...
        while s.size() > 0:
            # pop the first vertex
            temp = s.pop()
            # do the thing:
            # check if it's been visited and print if not
            if temp not in visited:
                # Mark it as visited and print
                print(temp)
                visited.add(temp)
                # push all it's neighbors
                for neighbor in self.get_neighbors(temp):
                    s.push(neighbor)
        return visited

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        else:
            return
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue
        # enqueue A PATH TO the starting vertex
        # create a set to store vistited vertices
        # while the queue is not empty...
            # dequeue the first PATH
            # do the thing:
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # check if it's been visited
            # If it hasn't been visited...
                # Mark it as visited
                # CHECK IF IT IS THE TARGET
                    # IF SO, RETURN THE PATH
                # Enqueue A PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
        q = Queue()
        starting_path = []
        starting_path.append(starting_vertex)
        q.enqueue(starting_path)
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            # print(path)
            end = path[-1]
            if end not in visited:
                visited.add(end)
                if end == destination_vertex:
                    return path
                for neighbor in self.get_neighbors(end):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    # print(new_path)
                    q.enqueue(new_path)
        else:
            print("Destination vertex not found in graph")


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        # push A PATH TO the starting vertex
        # create a set to store vistited vertices
        # while the stack is not empty...
            # pop the first PATH
            # do the thing:
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # check if it's been visited
            # If it hasn't been visited...
                # Mark it as visited
                # CHECK IF IT IS THE TARGET
                    # IF SO, RETURN THE PATH
                # push A PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    # push THE COPY
        s = Stack()
        starting_path = []
        starting_path.append(starting_vertex)
        s.push(starting_path)
        visited = set()
        while s.size() > 0:
            path = s.pop()
            # print(path)
            end = path[-1]
            if end not in visited:
                visited.add(end)
                if end == destination_vertex:
                    return path
                for neighbor in self.get_neighbors(end):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    # print(new_path)
                    s.push(new_path)
        else:
            print("Destination vertex not found in graph")

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = []
        # if starting_vertex is destination_vertex:
        #     path.append(starting_vertex)
        #     return path
        # elif starting_vertex not in visited:
        #     new_path = path.copy()
        #     new_path.append(starting_vertex)
        #     visited.add(starting_vertex)
        #     for neighbor in self.get_neighbors(starting_vertex):
        #         self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
        # else:
        #     return


        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
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
    # print(graph.vertices)

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
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
