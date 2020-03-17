"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Error: Vertex aint here homie.")

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else: 
            raise ValueError("Vertex does not exist")

    def bft(self, starting_vertex):
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size() > 0:
            v = queue.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        visited.add(starting_vertex)
        print(starting_vertex)

        edges = self.get_neighbors(starting_vertex)
        # base case
        if len(edges) == 0:
            return 
        else:
            for edge in edges:
                if edge not in visited:
                    self.dft_recursive(edge, visited)
                    # print(visited)
                else:
                    return
        

    def bfs(self, starting_vertex, destination_vertex):
        # Create a queue
        queue = Queue()
        # Enqueue A PATH TO the starting vertex
        visited = set()
        # Create a set to store visited vertices
        queue.enqueue([starting_vertex])
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first PATH
            current_path = queue.dequeue()
            current_node = current_path[-1]
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # Check if it's been visited
            if current_node == destination_vertex:
                return current_path
            # If it hasn't been visited...
                # Mark it as visited
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN THE PATH
            else:
                if current_node not in visited:
                    visited.add(current_node)
                    edges = self.get_neighbors(current_node)
                # Enqueue A PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
                for edge in edges:
                    path_copy = list(current_path)
                    path_copy.append(edge)
                    queue.enqueue(path_copy)
        



    def dfs(self, starting_vertex, destination_vertex):
        # Create a queue
        stack = Stack()
        # Enqueue A PATH TO the starting vertex
        visited = set()
        # Create a set to store visited vertices
        stack.push([starting_vertex])
        # While the queue is not empty...
        while stack.size() > 0:
            # Dequeue the first PATH
            current_path = stack.pop()
            current_node = current_path[-1]
            # GRAB THE VERTEX FROM THE END OF THE PATH
            # Check if it's been visited
            if current_node == destination_vertex:
                return current_path
            # If it hasn't been visited...
                # Mark it as visited
                # CHECK IF IT'S THE TARGET
                    # IF SO, RETURN THE PATH
            else:
                if current_node not in visited:
                    visited.add(current_node)
                    edges = self.get_neighbors(current_node)
                # Enqueue A PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
                for edge in edges:
                    path_copy = list(current_path)
                    path_copy.append(edge)
                    stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, target_value, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == target_value:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, target_value, visited, path)
                if new_path:
                    return new_path
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
    # print(graph.dfs_recursive(1, 6))
