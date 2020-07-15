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
        #pass  # TODO

        self.vertices[vertex_id] = set()
        

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #pass  # TODO
        q = Queue()
        q.enqueue(starting_vertex)

        # record visited nodes 
        visited = set()

        # run until queue is empty
        while q.size() > 0:
            # Take the first node
            visit = q.dequeue()

            # Check if in visited
            if visit not in visited:
                print(visit)
                # Add to visited
                visited.add(visit)
                # Get some friends
                for next_vertex in self.get_neighbors(visit):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #pass  # TODO
        # create a stack
        # s = Stack()
        # # give stack the starting_vertex
        # s.push(starting_vertex)

        # # record visited nodes
        # visited = set()

        # # run until queue is empty
        # while s.size() > 0:
        #     # Take the first node
        #     visit = s.pop()

        #     # Check if it's been visited
        #     if visit not in visited:
        #         print(visit)

        #         # add to visited
        #         visited.add(visit)

        #         # get some friends
        #         for next_vertex in self.get_neighbors(visit):
        #             s.push(next_vertex)

        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size():
            current_node = s.pop()
            if current_node not in visited:
                print(current_node)
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #pass  # TODO
        visited.add(starting_vertex)
        print(starting_vertex)

        neighbors = self.get_neighbors(starting_vertex)


        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #pass  # TODO

        # Make a Queue
        q = Queue()

        visited = set()

        path = [starting_vertex]
        q.enqueue(path)

        # While Queue isn't empty
        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[-1]

            ## If this node is our target
            if current_node == destination_vertex:
                ## Return True
                return current_path

            ## If not visited
            if current_node not in visited:
                ## Mark as visited
                visited.add(current_node)

                ## Get its neighbor
                neighbors = self.get_neighbors(current_node)

                ## For each neighbor
                for neighbor in neighbors:

                    path_copy = current_path[:]
                    path_copy.append(neighbor)

                    q.enqueue(path_copy)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #pass  # TODO

        path = []
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            visit = s.pop()

            if visit not in visited:
                # print(visit)

                path.append(visit)
                
                if visit == destination_vertex:
                    return path

                for next_vert in self.get_neighbors(visit):
                    s.push(next_vert)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #pass  # TODO

        if starting_vertex == destination_vertex:
            print('target found!', starting_vertex)
            return visited + [starting_vertex]
        else:
            visited.append(starting_vertex)
            for edge in self.get_neighbors(starting_vertex):
                print(f'{edge} is a neighbor to {starting_vertex}:{self.get_neighbors(starting_vertex)}')
                if edge not in visited:
                    print(f'{edge} not in visited, recurse, append {starting_vertex} if not in list')
                    path = self.dfs_recursive(edge, destination_vertex, visited)
                    if path:
                        print('path is', path)
                        return path
            visited.remove(starting_vertex)
            print(f'Delete: {starting_vertex} its exit {edge} has been visited and no path to {destination_vertex} was found')


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
