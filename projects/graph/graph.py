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
        # 1
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
        # Write a function within your Graph class that takes takes a starting node as an argument, then performs BFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        queue = Queue()
        # make a visited set
        visited = set()
        # put Starting Vertex in the queue
        queue.enqueue(starting_vertex)
        # While queue isn't empty
        while queue.size():
            # dequeue the item, it is our current item
            node = queue.dequeue()
            print(node)
            # mark Current as Visited
            visited.add(node)
            # for all dequeued item's edges
            for edge in self.vertices[node]:
            # if not visited
                if edge not in visited:
            # put them in queue
                    queue.enqueue(edge)

    def dft(self, starting_vertex):
        # Write a function within your Graph class that takes takes a starting node as an argument, then performs DFT. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        stack = Stack()
        # make a visited set
        visited = set()
        # put starting vertex in the stack
        stack.push(starting_vertex)
        # while the stack isn't empty
        while stack.size():
            # Pop off the top of the stack, it is current item
            node = stack.pop()
            # if node isn't visited
            if node not in visited:
                print(node)
                # mark as visited
                visited.add(node)
                # for each of our current item's edges
                for edge in self.vertices[node]:
                    stack.push(edge)


    def dft_recursive(self, starting_vertex, visited = None):
        # Write a function within your Graph class that takes takes a starting node as an argument, then performs DFT using recursion. Your function should print the resulting nodes in the order they were visited. Note that there are multiple valid paths that may be printed.

        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for child_vertex in self.vertices[starting_vertex]:
            if child_vertex not in visited:
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # Write a function within your Graph class that takes takes a starting node and a destination node as an argument, then performs BFS. Your function should return the shortest path from the start node to the destination node. Note that there are multiple valid paths.
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        queue = Queue()
        # make a visited set
        visited = set()
        # put Starting Vertex in the queue
        queue.enqueue([starting_vertex])
        # While queue isn't empty
        while queue.size():
            # dequeue the item, it is our current item
            path = queue.dequeue()
            node = path[-1]
            if node not in visited:
                if node == destination_vertex:
                    return path
                visited.add(node)
                for next_vertex in self.vertices[node]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    queue.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        # Write a function within your Graph class that takes takes a starting node and a destination node as an argument, then performs DFS. Your function should return a valid path (not necessarily the shortest) from the start node to the destination node. Note that there are multiple valid paths.
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        stack = Stack()
        # make a visited set
        visited = set()
        # put starting vertex in the stack
        stack.push(starting_vertex)
        # while the stack isn't empty
        while stack.size():
            # Pop off the top of the stack, it is current item
            node = stack.pop()

            if node == destination_vertex:
                visited.add(node)
                print(visited)
            # if node isn't visited
            elif node not in visited:
                # mark as visited
                visited.add(node)
                # for each of our current item's edges
                for edge in self.vertices[node]:
                    stack.push(edge)


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

    print("\nprint(graph.vertices)")

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
    print("\ngraph.dft(1)")
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
    print("\ngraph.bft(1)")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("\ndft_recursive(1)")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("\ngraph.bfs(1,6)")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("\ngraph.dfs(1,6)")
    print(graph.dfs(1, 6))
