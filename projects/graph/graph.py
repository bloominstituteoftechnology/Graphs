"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

graph = Graph()
graph.add_vertex(1)
# {}
# {1: set()}
myset.add(1)
# set(1)
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
            self.add_vertex(v2)

        if v2 not in self.vertices:
            self.add_vertex(v1)

        # if you say add an edge from v1 to v2, if you only only do one of the below it will be a directed graph
        self.vertices[v1].add(v2)
        # self.vertices[v2].add(v1)
        pass  # TODO
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        queue = Queue()
        # make a visited set
        visited = set()
        # put starting vertex in the queue
        queue.enqueue(starting_vertex)
        # while q isnt empty
        while queue.size():
            node = queue.dequeue()
        # dequeue the item, it is our current item
        #  mark current as visited
            visited.add(node)
        # for each of the dequeued items edges
            for edge in self.vertices[node]:
                # if not visited
                if edge no in visited:
                    queue.enqueue(edge)
        # put them in a queue



        pass  # TODO
    def dft(self, starting_vertex):
        #  the same except we make a stack
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        stack = Stack()
        # make a visited set
        visited = set()
        # pust starting vertext in stack
        stack.push(starting_vertex)
        # while stack is not empty
        while stack.size():
        #  pop off top of stack
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
        #  mark it as visited
                for edge in self.vertices(node):
                    if edge not in visited:
                        stack.push(edge)
        #  for each of our current items edges
        #  if not visited 
        #    put them on the stack



        pass  # TODO
    def dft_recursive(self, starting_vertex, visited):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        # fdjksalf
        # make a queue
        # 
        # fdjksalf

        q = Queue()

        visited = set()

        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()
        
        node = path[-1]

        if node not in visited:
            if node == destination_vertex:
                return path
            for neighbor in self.vertices[node]:
                copy_path = path[:]k
                copy_path.append(neighbor)
                q.enqueue(copy_path)

        # take the node were given
        #  if this node has not been visited:
        #   mark is as visited
            if node not in visited:
        #   for each of this notes neighbors
                print(node)
                visited.add(node)
                for neighbor in self.vertices[node]:
                    self.dft_recursive(neighbor, visited)
        #    call dft_recursive()


        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        q = Quene()

        visited = set()

        q.enqueue(starting_vertex)

        while q.size():
            path = q.dequeue()

            node = [-1]

            if node not in visited:
                if node == destination_vertex:
                    return path
            # node is the lat thing in our path
            # mark as visited
            #  if it has not been visited
            #  make a copy of that path
            #  add the firend to that path
            #   put the path to hat node in the queue
        pass  # TODO
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
