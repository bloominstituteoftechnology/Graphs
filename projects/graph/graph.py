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
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
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
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()

        while queue.size() != 0:
            curr_node = queue.dequeue()
            # if not seen yet, print and add neighbors
            if curr_node not in visited:
                print(curr_node)
                visited.add(curr_node)
                neighbors = self.get_neighbors(curr_node)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() != 0:
            curr_node = stack.pop()
            # if not seen yet, print and add neighbors
            if curr_node not in visited:
                print(curr_node)
                visited.add(curr_node)
                neighbors = self.get_neighbors(curr_node)
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        """
        other implementation:
        path = [starting_vertex]
        q.enqueue(path)
        while q.size() > 0:
            curr_path = q.dequeue()
            curr_node = curr_path[-1]
            if curr_node == destination_vertex:
                return curr_path
            if curr_node not in visited:
                visited.add(curr_node)
                neighbors = self.get_neighbors(curr_node)
                for neighbor in neighbors:
                    new_path = curr_path + [neighbor]
                    q.enqueue(new_path)
        """
        # stores parents of vertices
        parent = {}
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() != 0:
            curr_node = q.dequeue()
            # check neighbors if not visited yet
            if curr_node not in visited:
                visited.add(curr_node)
                neighbors = self.get_neighbors(curr_node)
                # set tracker of wheter we find destination
                found_dest = False
                for neighbor in neighbors:
                    if neighbor == destination_vertex:
                        found_dest = True
                    # set parent of neighbor to curr_node
                    parent[neighbor] = curr_node
                    q.enqueue(neighbor)
                if found_dest:
                    break
        
        # initialize path to list with destination
        path = [destination_vertex]
        curr_node = destination_vertex

        # loop while we aren't at start
        while curr_node != starting_vertex:
            # add parent of curr_node
            path.insert(0, parent[curr_node])
            # set curr_node to curr_node's parent
            curr_node = parent[curr_node]

        return path


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        path = []

        while s.size() != 0:
            curr_node = s.pop()
            if curr_node not in visited:
                visited.add(curr_node)
                path.append(curr_node)
                if curr_node == destination_vertex:
                    return path 
                neighbors = self.get_neighbors(curr_node)
                for neighbor in neighbors:
                    s.push(neighbor)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if starting_vertex not in visited:
            visited.add(starting_vertex)

            if starting_vertex == destination_vertex:
                path.append(starting_vertex)
                return path
            else:
                neighbors = self.get_neighbors(starting_vertex)
                for neighbor in neighbors:
                    path = self.dfs_recursive(neighbor, destination_vertex, path, visited)
                    if path != []:
                        path.insert(0, starting_vertex)
                        return path
        return path

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