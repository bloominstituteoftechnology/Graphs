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
        # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exits")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
        # Create an empty queue
        q = Queue()
        # add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # create an empty set to store visited nodes
        visited = set()
        # while the dequeue is not empty...
        while q.size() > 0:
            # Deque ,the first vertex
            v = q.dequeue()
            # check if it's not been visited
            # if it has been visited
            if v not in visited:
                # mask as visited
                visited.add(v)
                print(v)
            # then add all neighbors to the back of the queue
            for neighbor in self.get_neighbors(v):
                q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # create an empty stack
        s = Stack()
        # push the starting vertex_id to the stack
        s.push(starting_vertex)
        # create an empty set to store visited nodes
        visited = set()
        # while the stack is not empty ...
        while s.size() > 0:
            # Pop the vertex
            v = s.pop()
            # check if its been visited
            # if it has not been visited ...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                #  then push all neibors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # TODO
        # Check if the node is visited
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited
            visited.add(starting_vertex)
            # Print
            print(starting_vertex)
            for i in self.get_neighbors(starting_vertex):
                # Call DFT_Recursive on each child
                self.dft_recursive(i, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        target = destination_vertex
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            v = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            last = v[-1]
            # CHECK IF IT'S THE TARGET
            if last == target:
                # IF SO, RETURN THE PATH
                return v
            # Check if it's been visited
            # If it has not been visited...
            if last not in visited:
                # Mark it as visited
                print(last)
                visited.add(last)
                # Then add A PATH TO all neighbors to the back of the queue
                # (Make a copy of the path before adding)
                for i in self.get_neighbors(last):
                    copy = v + [i]
                    q.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO\
        target = destination_vertex
        # Create an empty Stack
        s = Stack()
        # Add A PATH TO the starting vertex_id to the Stack
        s.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the Stack is not empty...
        while s.size() > 0:
            # DeStack, the first PATH
            v = s.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            last = v[-1]
            # CHECK IF IT'S THE TARGET
            if last == target:
                # IF SO, RETURN THE PATH
                return v
            # Check if it's been visited
            # If it has not been visited...
            if last not in visited:
                # Mark it as visited
                print(last)
                visited.add(last)
                # Then add A PATH TO all neighbors to the front of the Stack
                # (Make a copy of the path before adding)
                for i in self.get_neighbors(last):
                    copy = v + [i]
                    s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        # check if the node is visited
        # if node == target return pat
        # if not ...
        # mark it as visited
        visited.add(starting_vertex)
        # print
        print(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        # call DFS_recursive on each child
        for i in self.get_neighbors(starting_vertex):
            if i not in visited:
                new_path = self.dfs_recursive(
                    i, destination_vertex, visited, path)
                if new_path:
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
    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)
    # '''
    # Valid DFT recursive paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft_recursive(1)
    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))
    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
