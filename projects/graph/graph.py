"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
        # Sets are unique values, no duplicates

    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            self.add_vertex(v1)

        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.vertices[v1].add(v2)

        self.vertices[v2].add(v1)

    def bft(self, starting_vertex):
        queue = Queue()

        visited = set()

        while queue.size():
            node = queue.dequeue()

            if not node in visited:
                visited.add(node)

                for edge in self.vertices[node]:
                    queue.enqueue(edge)
        pass  # TODO

    def dft(self, starting_vertex):
        stack = Stack()

        visited = set()

        stack.push(starting_vertex)

        while stack.size():
            node = stack.pop()
            if node not in visited:
                visited.add(node)

                for edge in self.vertices[node]:
                    stack.push(edge)

    def dft_recursive(self, node, visited=(set)):
        # take node were given
        # if this node hasn't been visited:
        if node not in visited:
            # mark it as visited
            visited.add(node)
            # for each of this nodes neighbors:
            for neighbor in self.vertices[node]:
                # call dft_recursive
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # make a queue
        q = Queue()
        # make a visited set
        visited = set()
        # enqueue the path to that node
        q.enqueue([starting_vertex])
        # while the queue isn't empty:
        while q.size() > 0:
            # dequeue the PATH
            path = q.dequeue()
        # the las thing in the path is our current item
            node = path[-1]
        # if it's not visited:
            if node not in visited:
        # CHECK if its the target
                if node == destination_vertex:
                    return path
                    # for each of the nodes neighbors
                for neighbor in self.vertices[node]:
                    # copy the path
                    copy_path = path[:]
                    # add the neighbor to the path
                    copy_path.append(neighbor)
                    # enqueue the PATH COPY
                    q.enqueue(copy_path)
      

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
