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
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty Queue FIFO LIST
        q = Queue()
        # Create an empty visited Set
        visited = set()
        # Add the starting vertex to the queue
        q.enqueue(starting_vertex)
         # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            pop = q.dequeue()
            # If it is has not been visited...
            if pop not in visited:
                # Mark it as visited (print it and add it to the visited set)
                print(pop)
                visited.add(pop)
                # Then enqueue each of its neighbors in the queue
                for neighbor in self.vertices[pop]:
                    q.enqueue(neighbor)          
                
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty Stack LIFO LIST
        s = Stack()
        # Create an empty visited Set
        visited = set()
        # Push the starting vertex to the stack
        s.push(starting_vertex)
         # While the stack is not empty...
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # If it is has not been visited...
            if v not in visited:
                # Mark it as visited (print it and add it to the visited set)
                print(v)
                visited.add(v)
                # Then push each of its neighbors onto the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)   
        
    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Mark the starting node as visited
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        # then call dft_recursive on each unvisited neighbors

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Store an entire path 
        # Keep track of every nodes Parent 
        visited = [] 
        q = Queue()
        q.enqueue([starting_vertex])
        if starting_vertex == destination_vertex:
            return starting_vertex
        while q.size()> 0:
            path = q.dequeue()
            node = path[-1]
            if node not in visited:
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                    if neighbor == destination_vertex:
                        return new_path
                visited.append(node)
        return "So sorry, but a connecting path doesn't exist :("
    def bfs_brady(self, sv, dv):
        q = Queue()
        visited = set()
        q.enqueue([sv])
        while q.size() >0:
            path = q.dequeue()
            v = path[-1]
            if v == dv:
                return path
            if v not in visited:
                visited.add(v)
                for neighbor in self.vertices[v]:
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = []
        s = Stack()
        s.push([starting_vertex])
        if starting_vertex == destination_vertex:
            return starting_vertex
        while s.size()>0:
            path = s.pop()
            node = path[-1]
            if node not in visited:
                neighbors = self.vertices[node]
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)
                    if neighbor == destination_vertex:
                        return new_path
                visited.append(node)

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
