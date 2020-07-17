"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import collections

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


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
            self.vertices[v1].add(v2)  # there's an edge from v1 to v2
        else:
            raise IndexError("nonexistent vert")

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
        # Create an empty queue
        q = Queue()

        # Create a set to store the visited nodes
        visited = set()

        # Init: enqueue the starting node
        q.enqueue(starting_vertex)

        # While the queue isn't empty
        while q.size() > 0:
            # Dequeue the first item
            v = q.dequeue()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)
                # Do something with the node
                print(f"Visited {v}")

                # Add all neighbors to the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()

        # Create a set to store the visited nodes
        visited = set()

        # Init: push the starting node
        s.push(starting_vertex)

        # While the stack isn't empty
        while s.size() > 0:
            # pop the first item
            v = s.pop()
            # If it's not been visited:
            if v not in visited:
                # Mark as visited (i.e. add to the visited set)
                visited.add(v)

                # Do something with the node
                print(f"Visited {v}")

                # Add all neighbors to the stack
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        # q.enqueue(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()
        q.enqueue([starting_vertex])

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            v = q.dequeue()

            # Grab the last vertex from the PATH
            n = v[-1]

            # If that vertex has not been visited...
            if n not in visited:
                # CHECK IF IT'S THE TARGET
                if n == destination_vertex:
                    # IF SO, RETURN PATH
                    return v

                # Mark it as visited...
                visited.add(n)

                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.vertices[n]:
                    # COPY THE PATH
                    new = v.copy()
                    # APPEND THE NEIGHOR TO THE BACK
                    new.append(neighbor)
                    q.enqueue(new)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        v = Stack()
        visited = set()
        v.push([starting_vertex])
        while v.size() > 0:
            n = v.pop()
            last_vertex = n[-1]
            if last_vertex not in visited:
                visited.add(last_vertex)
            else:
                continue

            for neighbor in self.get_neighbors(last_vertex):
                new = n.copy()
                new.append(neighbor)
                v.push(new)
                if neighbor == destination_vertex:
                    return new


    def dfs_recursive(self, starting_vertex, destination_vertex, visited= None, s=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            s = collections.deque([])
            s.append([starting_vertex])
        visited.add(starting_vertex)
        current = s.pop()
        last = current[-1]
        for last in self.get_neighbors(last):
            if last not in visited:
                route = list(current)
                route.append(last)
                s.append(route)
                if last is destination_vertex:
                    return route

        return self.dfs_recursive(last, destination_vertex, visited, s)




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
