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

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # make sure we already know about both nodes already, if so then add
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1) #uncomment for bidirectional
        else:
            raise IndexError("That index does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # initialize visited set and queue
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)
        # continue looping while items still in queue
        while q.size() > 0:
            # pop out first item from queue
            current = q.dequeue()

            # add to visited set if not in there, then print
            if current not in visited:
                visited.add(current)
                print(current)
                # enqueue nodes that current is connected to in queue
                for connected_to in self.vertices[current]:
                    q.enqueue(connected_to)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # initialize visited dict as well as stack
        visited = set()
        stack = Stack()

        stack.push(starting_vertex)

        while stack.size() > 0:
            # remove last item
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                print(current)
                for connected_to in self.vertices[current]:
                    stack.push(connected_to)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # first call visited will be initialized, other calls will not
        if not visited:
            visited = set()

        # add vertex to visited, then print
        visited.add(starting_vertex)
        print(starting_vertex)

        # repeat for all connecting nodes in self.verices[starting_vertex]
        for child in self.vertices[starting_vertex]:
            if child not in visited:
                # if child has not been visited, call function recursively
                self.dft_recursive(child, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # initialize queue and visited, add starting_vertex as array to queue
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
            # dequeue item and set the current vertex to the last item in the list
            path = queue.dequeue()
            vertex = path[-1]

            # if vertex hasnt been visited, add to visited
            # if vertex is currently at the destination, return the path
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)

                # add the next connected nodes to a copy of the array as those will be next nodes to search
                for next_node in self.vertices[vertex]:
                    copy = list(path)
                    copy.append(next_node)
                    queue.enqueue(copy)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # initialize queue and visited, add starting_vertex as array to queue
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])

        while stack.size() > 0:
            # dequeue item and set the current vertex to the last item in the list
            path = stack.pop()
            vertex = path[-1]

            # if vertex hasnt been visited, add to visited
            # if vertex is currently at the destination, return the path
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)

                # add the next connected nodes to a copy of the array as those will be next nodes to search
                for next_node in self.vertices[vertex]:
                    copy = list(path)
                    copy.append(next_node)
                    stack.push(copy)
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


# graph = Graph()  # Instantiate your graph
# graph.add_vertex('0')
# graph.add_vertex('1')
# graph.add_vertex('2')
# graph.add_vertex('3')
# graph.add_edge('0', '1')
# graph.add_edge('0', '3')
# graph.add_edge('0', '3')
# graph.add_edge('32', '3')
# print('testing', graph.vertices)


# graph.bft('1')
