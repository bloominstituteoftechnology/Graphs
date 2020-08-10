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
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
        # make a queue
        q = Queue()
        # q.size = 0
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # q.size = 1
        # make a set to track if we've been here before
        visited = set()
        # while our queue isn't empty
        while q.size > 0:
        ## dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
            # q.size = 0
        ## if we haven't visited thos nide yet,
            if current_node not in visited:
        ### mark as visited
                visited.add(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors,
                for n in neighbors:
        #### add to queueu
                    q.enqueue(n)
                    # q.size = x
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # make a satck
        s = Stack()
        # s.size = 0
        # push our starting node
        s.push(starting_vertex)
        # s.size = 1
        # make a set to track if we've been here before
        visited = set()
        # while our stack isn't empty
        while s.size > 0:
        ## pop whatever's at the top of our stack, this is our current_node
            current_node = s.pop()
            # s.size = 0
        ## if we haven't visited thos nide yet,
           if current_node not in visited:
        ### mark as visited
                visited.add(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors,
                for n in neighbors:
        #### add to stack
                    s.push(n)
                    # s.size = x

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            
            for n in self.get_neighbors(starting_vertex):
                self.dfs_recursive(n)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        q = Queue()
        q.enqueue(starting_vertex)

        if starting_vertex == destination_vertex:
            return "That was easy! Start = goal"
       
        visited = set()
    
        while q.size > 0:

            path = q.dequeue()

            current_node = path[0]
            if current_node not in visited:
                visited.add(current_node)

                neighbors = self.get_neighbors(current_node)

                for n in neighbors:
                    new_path = list(path)
                    new_path.append(n)
                    q.enqueue(n)

                    if n == destination_vertex:
                        return new_path

        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size > 0:
            current_node = s.pop()
            if current_node not in visited: 
                visited.add(current_node)
                if current_node == end_node: 
                    return success
        
                for n in self.get_neigbhors(current_node):
                    s.push(n)

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
