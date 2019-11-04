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
        # rejects if vertice does not exist
        if v1 not in self.vertices or v2 not in self.vertices:
            print(f'vertice {v1} does not exist')
            # raise KeyError("That vertex does not exist")
        else:
            self.vertices[v1].add(v2)          

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        queue = Queue()
        already_explored = {}
        queue.enqueue(starting_vertex)
        already_explored[starting_vertex] = True

        while queue.size():
            current_vertex = queue.dequeue()            
            print(f'{current_vertex} ', end='')

            for edge in self.vertices[current_vertex]:
                if edge not in already_explored:
                    queue.enqueue(edge)
                    already_explored[edge] = True

        print()                
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        already_explored = {}
        stack.push(starting_vertex)
        already_explored[starting_vertex] = True

        while stack.size():
            current_vertex = stack.pop()
            print(f'{current_vertex} ', end='') 

            for edge in self.vertices[current_vertex]:
                if edge not in already_explored:
                    stack.push(edge)
                    already_explored[edge] = True

        print()                       

    def dft_recursive(self, starting_vertex, already_explored = {}):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        already_explored[starting_vertex] = True
        print(starting_vertex)

        for edge in self.vertices[starting_vertex]:
            if edge not in already_explored:
                self.dft_recursive(edge, already_explored)

             

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
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
    graph.add_edge(8, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print()

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
    print('printing btf')    
    graph.bft(1)
    print()

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('printing dtf stack')
    graph.dft(1)
    print()

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('printing dtf recursive')
    graph.dft_recursive(1)
    print()

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('printing graph bfs')
    print(graph.bfs(1, 6))
    print()

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('printing graph dfs')
    print(graph.dfs(1, 6))
    print()
