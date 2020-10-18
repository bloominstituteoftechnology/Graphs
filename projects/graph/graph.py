"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """Add a directed edge to the graph."""
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print('Error: Vertices were not found')  

    def bft(self, starting_vertex):
        """Print each vertex in breadth-first order
        beginning from starting_vertex."""
        # Create an empty queue -- FIFO
        # Add starting_vertex to the queue and 
        # this will keep track of next_to_visit_vertices
        queue = Queue()      
        queue.enqueue(starting_vertex)
        # Create an empty set to track the visited vertices
        visited = set()
        # while queue is not empty
        while queue.size():
            # dequeue the vertex off the queue
            current_vertex = queue.dequeue() 
            # if current_vertex is not in visited set
            # add current vertex to the visited set
            if current_vertex not in visited:
                 # print the current_vertex
                print(current_vertex) 
                visited.add(current_vertex) 
                # for each neighbor of the current_list **Add to queue
                for neighbor in self.vertices[current_vertex]:
                    # Add all the neighbors of the current_list to the queue
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """Print each vertex in depth-first orderbeginning from starting_vertex."""
        # Create an empty stack
        stack = Stack()
        # Add the starting_vertex to the stack
        # so that we can track the next_to_visit_vertices
        stack.push(starting_vertex)
        # Create an empty stack to track visited vertices
        visited = set()
        # while stack is not empty:
        while stack.size():
            # Remove vertex off of the stack
            current_vertex = stack.pop()
            # If the current vertex is not in 
            if current_vertex not in visited:
                #print the current_vertex
                print(current_vertex)
                # Add current_vertex to the visited
                visited.add(current_vertex)
                # for every neighbor of the current vertex
                for neighbor in self.vertices[current_vertex]:
                    # Add neighbor to the stack
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):
        """Return a list containing the shortest path fromstarting_vertex to destination_vertex in
        breath-first order."""
        # Create an empty queue
        # Add a path to the empty queue i.e., add [starting_vertex] to the queue
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create an empty visited set to track of visited vertices
        visited = set()
        # while queue is not empty
        while queue.size():
            # Dequeue the queue to get the current_path
            current_path = queue.dequeue()
            # Get the current_vertex from the current_path(last vertex in path array)
            current_vertex = current_path[-1]
            # if current_vertex not in visited:
            if current_vertex not in visited:
                #Add current_vertex to the visited
                visited.add(current_vertex)
                #if current_vertex == destination_vertex
                # return current_path
                if current_vertex == destination_vertex:
                    return current_path
                # for each neighbor of the current_vertex
                for neighbor in self.vertices[current_vertex]:
                    # get the copy of the current path
                    current_path_copy = list(current_path)    
                    # add neighbor to the current path
                    current_path_copy.append(neighbor)
                    # now add this current path copy to the queue
                    queue.enqueue(current_path_copy)

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
    print("Executing Depth First Traverse>>>>>>>>>")
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
    print("Executing BFirst Traverse>>>>>>>>>")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Executing BFirst Search>>>>>>>>>")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
