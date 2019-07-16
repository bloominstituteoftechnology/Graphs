"""
Simple graph implementation
"""

from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.vertices[v1].add(v2)
        self.vertices[v2].add(v2)
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # make a queue
        queue = Queue()
        visited = set()
        # make a visited set
        # put starting vertex in the queue
        queue.enqueue(starting_vertex)
        # while q isn't empty
        while queue.size():
                # dequeue
            node = queue.dequeue()
            # mark current as visted

            visited.add(node)
            # for each of the deqeued item's edges
            for edge in self.vertices[node]:
                # put them in the queue
                if edge not in visited:
                    queue.enqueue(edge)
            pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        stack = Stack()

        # make a visited set
        visited = set()
        # pyt starting vertext in our stack
        stack.push(starting_vertex)
        # while the stack isnt empty
        while stack.size():
            node = stack.pop()
        # pop off the top of the stack, it is our current item
        # mark it as visted
            visited.add(node)
        # for each of our current item's edges
            for edge in self.vertices[node]:
                # put them on the stack
                if edge not in visited:
                    stack.push(edge)
            print(visited)

        pass  # TODO

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        # make a visited set
        if visited == None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                self.dft_recursive(edge, visited)
        pass

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        queue = Queue()
        # make a visited set
        visited = set()
        # queue the starting vertex
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            path = queue.dequeue()
            # Grab the last vertex from the PATH
            node = path[-1]
            # If the node is not been visited
            if node not in visited:
                # Then check if this node is our destination
                if node == destination_vertex:
                    # If it is return the current path
                    return path

            # mark current as visited
            visited.add(node)
            # for each each friend of the current node
            for friend in self.vertices[node]:
                # put the path to that node in the queue
                update_path = path.copy()
                # Add new friends to the back of the queue
                update_path.append(friend)
                queue.enqueue(update_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        # put starting vertext in our stack
        stack.push([starting_vertex])
        # make a visited set
        visited = set()
        # While the stack isn't empty
        while stack.size() > 0:
            # Let pop off the first path
            path = stack.pop()
            # Get the last node or vertex from the path
            node = path[-1]
            # If that node has not been visited
            if node not in visited:
                # See if that node is our destination
                if node == destination_vertex:
                    # If it is return the path
                    return path

                # Mark the node as visited
                visited.add(node)
                for friend in self.vertices[node]:
                    short_path = path.copy()
                    short_path.append(friend)
                    stack.push(short_path)

        return None


pass  # TODO


if __name__ == '__main__':
    graph = Graph()
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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print(graph.dft(1))

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
    print(graph.dfs(1, 6))
