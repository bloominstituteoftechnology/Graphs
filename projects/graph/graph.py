"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import random 

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
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex_id)

        # Create a Set to store visited vertices
        visited = set()
        
        # While the queue is not empty....
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()

            # If taht vertex has not been visited....
            if v not in visited:
                # visit it (Doing whatever we have to do here. In this case, we are just printing it)
                print(v)

                # MArk it as visited...
                visited.add(v)

                # Then add all of its neighbors to the back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        EXAMPLE: 
           cur(C)

            A - B - C - D - E - F
                \   /       /  
                  G   -   H
        STACK: A B 
        neighbors: C
        VISITED: A B
        """
        stack = Stack()

        stack.push(starting_vertex)
        stack.push(starting_vertex)
        cur = stack.pop()

        visited = set()

        while stack.size() > 0:
            
            if cur not in visited:
                print(cur)
                visited.add(cur)
            
            counter = 0
            for next_vert in self.get_neighbors(cur):
                counter += 1
                if next_vert not in visited:
                    stack.push(next_vert)
                    cur = next_vert
                    break   

                elif counter == len(self.get_neighbors(cur)):
                    cur = stack.pop()
                    break


    def dft_recursive(self, cur, stack=None, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Explore(g, path_so_far):
            # processing the first node
            # explore(the rest of the graph)

        # Stopping condition
        if len(visited) == len(self.vertices):
            return

        if cur not in visited:
            print(cur)
            visited.add(cur)

        if stack is None:
            stack = Stack()
            stack.push(cur)
            stack.push(cur)
            cur = stack.pop()

        for next_vert in self.get_neighbors(cur):
            if next_vert not in visited:
                stack.push(next_vert)
                cur = next_vert
                self.dft_recursive(cur, stack, visited)
                break 
        
        cur = stack.pop()
        self.dft_recursive(cur, stack, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        # push the first path into the queue
        q.enqueue([starting_vertex])
        while q.size() > 0:
            # get the first path from the queue
            path = q.dequeue()
            # get the last node from the path
            node = path[-1]
            # path found
            if node == destination_vertex:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into
            # the queue
            for adjacent in self.get_neighbors(node):
                new_path = list(path)
                new_path.append(adjacent)
                q.enqueue(new_path)
                    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

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
    graph.dfs(1, 7)
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
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
