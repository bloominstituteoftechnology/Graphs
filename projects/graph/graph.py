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
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

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
        # Create empty queue and enque starting vertex
        queue = Queue()
        # 
        queue.enqueue(starting_vertex)
        # Create an empty set to track visited vertices
        visited = set()
        # while the queue is not empty
        while queue.size() > 0:
            # get the current vertex(deque)
            node = queue.dequeue()
            # 1
            # check if current vertex has not been visited
            if node not in visited:
                # print current vertex
                # Mark current vertex as visited
                print(node)
                # Add the current vertex to a visited set
                visited.add(node)
                # {1}
            # queue up all the current vertex's neighbors
            # I CANT DO THIS BECAUSE IT RETURN THE NUMBERS, BUT IN A SET AND I CAN'T STORE A SET WITHIN A SET
            # queue.enqueue(self.get_neighbors(node))
                for neighbor in self.get_neighbors(node):
                    queue.enqueue(neighbor)
            # print(queue)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in self.get_neighbors(node):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create empty queue and enque path to starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # [1]
        # Create an empty set to track visited vertices
        visited = set()
        # while the queue is not empty
        while queue.size() > 0:
            print(queue)
            #  queue = [ [1, 2,3, 5], [1, 2, 4,6] [1,2,4,7]]]
            currrent_path = queue.dequeue()
            # [1, 2, 4]
            print(f'\nthe currrent_path is {currrent_path}')
            current_node = currrent_path[- 1]
            print(f'\nthe current_node is {current_node}')
            # [4]
            if current_node == destination_vertex:
                return currrent_path
            if current_node not in visited:
                    visited.add(current_node)
                    # {1, 2, 3,4}
                    print(f'visted: {visited}')
                    for neighbor in self.get_neighbors(current_node):
                        newPath = list(currrent_path)
                        # [1, 2, 4,6]
                        newPath.append(neighbor)
                        # [6]
                        print(f'the new path is: {newPath}')
                        queue.enqueue(newPath)
                        # [[1, 2, 4,6] [1,2,4,7]]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create empty queue and enque path to starting vertex
        queue = Stack()
        queue.push([starting_vertex])
        # [1]
        # Create an empty set to track visited vertices
        visited = set()
        # while the queue is not empty
        while queue.size() > 0:
            # get the current vertex path (deque)
            currrent_path = queue.pop()
            # [1, 2]
            print(f'\nthe currrent_path is {currrent_path}')
            # set the current vertex to the last element of the path
            current_node = currrent_path[- 1]
            print(f'\nthe current_node is {current_node}')
            # [2]
            # check if current vertex is destination
            if current_node == destination_vertex:
                return currrent_path
            # check if current vertex has not been visited
            if current_node not in visited:
                # Mark current vertex as visited
                    # Add the current vertex to a visited set
                    visited.add(current_node)
                    # {1, 2}
                    print(f'visted: {visited}')
                    # queue up new paths with each neighbor
                    for neighbor in self.get_neighbors(current_node):
                        newPath = list(currrent_path)
                        # [1,2, 4]
                        newPath.append(neighbor)
                        # [4]
                        print(f'the new path is: {newPath}')
                        # take current path 
                        queue.push(newPath)
                        # [1, 2, 3, 4]

                        # append neighbor to it's path
                        # queue up new path

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
    # print(graph.vertices)

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
    graph.dft_recursive(1)

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
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
