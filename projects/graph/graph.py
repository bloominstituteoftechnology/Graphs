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
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.vertices[v1].add(v2)


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Start with a FIFO queue
        que = Queue()
        visited = []

        que.enqueue(starting_vertex)

        # While que is not empty
        while que.size():
            node = que.dequeue()

            # Mark current as visited
            visited.append(node)

            for edge in self.vertices[node]:
                # if not visited
                if edge not in visited:
                    que.enqueue(edge)
        print(visited)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        stack = Stack()

        # make a visited list
        visited = []

        # Add starting_vertext to stack
        stack.push(starting_vertex)

        # While stack is not empty:
        while stack.size():
            node = stack.pop()

            if node not in visited:
                # Mark as visited
                visited.append(node)

                # Get edges
                for edge in self.vertices[node]:

                    if edge not in visited:
                        # Add it to the stack
                        stack.push(edge)

        print(visited)


    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        if len(visited) == len(self.vertices):
            # print(visited)
            print()
            return

        if starting_vertex not in visited:
            visited.append(starting_vertex)
            print(starting_vertex, end=", ")

            for edge in self.vertices[starting_vertex]:
                self.dft_recursive(edge, visited)




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # make a visited set
        visited = set()
        #enqueue the PATH to that node
        q.enqueue([starting_vertex])
        # while the queue isn't empty:
        while q.size() > 0:
            # dequeue the PATH
            path = q.dequeue()
            # last thing in the path is current item
            node = path[-1]
            # if it's not visited:
            if node not in visited:
                #check if it's the target
                if node == destination_vertex:
                    #return the path
                    return path
                # for each of the node's neighbors
                for neighbor in self.vertices[node]:
                    #copy the path
                    copy_path = path.copy()
                    # add neighbor to the path
                    copy_path.append(neighbor)
                    # enqueue the path_copy
                    q.enqueue(copy_path)
                    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()

        # add a path
        stack.push([starting_vertex])

        while stack.size() > 0:
            path = stack.pop()

            # we want the last thing in the path as the current item
            node = path[-1]

            if node not in visited:
                if node == destination_vertex:
                    return path

                for neighbor in self.vertices[node]:
                    copy_path = path[:]
                    copy_path.append(neighbor)
                    stack.push(copy_path)





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
