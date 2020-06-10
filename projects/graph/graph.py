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
        # creating a node for the given vertex_id
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # adding an edge between two given nodes
        if v1 in self.vertices and v2 in self.vertices:
            # at the starting node, add an edge connecting the second node
            self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # check vertex_id in dictionary
        # return value if edges exist

        if self.vertices[vertex_id]:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Queue  = First in First out - Breadth First

        # Stack = First in Last out - Depth First

        # initialize empty visited set
        visited = set()
        # initilize a queue and add the starting node
        queue = Queue()
        queue.enqueue(starting_vertex)

        while queue.size() > 0:
            node = queue.dequeue()
            if node not in visited:
                print(node)
                visited.add(node)
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    queue.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = Stack()
        #Add starting node to stack
        stack.push(starting_vertex)

        while stack.size() > 0:
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        # initialize storage before recursion starts if one doesn't exist
        if visited is None:
            visited = set()

        cur = starting_vertex
        neighbours = self.vertices[cur]

        if cur:
            visited.add(cur)
            print(cur)
        
        if neighbours:
            for neighbour in neighbours:
                if neighbour not in visited:
                    self.dft_recursive(neighbour, visited)
                
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = Queue()
        queue.enqueue([starting_vertex])

        while queue.size() > 0:
        
            cur_path = queue.dequeue()                  
            cur_node = cur_path[-1]
            # checks cur_node against destination_vertex
            if cur_node == destination_vertex:
                # returns path that got to destination node
                return cur_path
            else:
                # Marks nodes that are not the destination node as visited
                if cur_node not in visited:
                    visited.add(cur_node)
                    # set neighbors to variables
                    neighbors = self.get_neighbors(cur_node)
                    # print(neighbors)
                    for neighbor in neighbors:
                        # copy_path = [*cur_path, neighbor]
                        copy_path = list(cur_path)
                        # you add where you want to go to the copy
                        copy_path.append(neighbor)
                        # queue the copy
                        queue.enqueue(copy_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        visited = set()
        stack = Stack()
        stack.push([starting_vertex])

        while stack.size() > 0:

            cur_path = stack.pop()
            cur_node = cur_path[-1]

            if cur_node == destination_vertex:
                return cur_path
            else:
                if cur_node not in visited:
                    visited.add(cur_node)

                    neighbors = self.get_neighbors(cur_node)

                    for neighbor in neighbors:
                        copy_path = list(cur_path)
                        copy_path.append(neighbor)
                        stack.push(copy_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path = [], visisted=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visisted is None:
            visisted = set()
        
        cur = starting_vertex
        cur_path = path + [cur]
        neighbors = self.get_neighbors(cur)

        if cur:
            visisted.add(cur)
        
        if cur == destination_vertex:
            return cur_path
        else:
            # loop through neighbors
            for neighbor in neighbors:
                # check if neighbor has been visisted
                if neighbor not in visisted:
                    copy_path = self.dfs_recursive(neighbor, destination_vertex, cur_path, visisted)
                    if copy_path:
                        return copy_path




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
    print(f'THIS IS BFS: {graph.bfs(1, 6)}')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
