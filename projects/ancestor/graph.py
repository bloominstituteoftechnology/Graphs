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
       
        # make a queue
        q = Queue()   
        #enqueue our starting node aka starting_vertex
        q.enqueue(starting_vertex)
        #make a set to track if we've been here before\
        visited = set()
        # while our queue isnt empty
        while q.size() > 0:
            #dequeue whatever's at the front of our line, this is our starting_node
            current_node = q.dequeue()
            #if we haven't visited the starting_node
            if current_node not in visited:
                print(current_node)
                # mark as visited
                visited.add(current_node)
                #get its neighbors
                for v in self.get_neighbors(current_node):
                    #for each neighbor
                    q.enqueue(v)
       

       

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
       
        #make a stack
        stack = Stack()
        # push our starting node
        stack.push(starting_vertex)
       

        # make a set to track if we've been here before
        visited = set()
        # while our stack isn't empty
        while stack.size() > 0:
            # pop off whatever's on top, this is current_node
            current_node = stack.pop()
            # if we haven't visited this vertex before
            if current_node not in visited: 
                print(current_node)
                #add current_node to visited
                visited.add(current_node)
                # get its neighbhors 
                #for each of the neighbors
                #add to our stack 
                for v in self.get_neighbors(current_node):
                    stack.push(v)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #base case is empty array

        if visited is None:
            visited = set()
            
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.vertices[starting_vertex]:
            if v not in visited:
                self.dft_recursive(v, visited)

     

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        
1. Starting Node + Target Node
2. Add [starting_node] to path, and push it to stack
3. pop last item from stack
4. check the last item in the path, for instance [1, 2, 4, 6, 7]... check 7 (path[-1])
5. add path[-1] to your visited
6. get neighbors of path[-1]
7. add to your path, so for each neighbor, create a path copy, add the neighbor to end of path
8. push your new path to your stack
9. for instance, if neighbors of 7 are 10, 12, 13, 6, but 6 has been visited
10. [1, 2, 4, 6, 7, 10], [1, 2, 4, 6, 7, 12], [1, 2, 4, 6, 7, 13] will be added to stack
11. when path[-1] is your target, stop and return the path
"""
    
        
        q = Queue()
        #enqueue path
        q.enqueue([starting_vertex])
        # keep track of visited
        visited = set()
        #while queue is not empty
        while q.size() > 0:
            # dequeue first path
            current_path = q.dequeue()
            # get last node form the path
            last_node = current_path[-1]
            #if not visited
            if last_node not in visited:
                #if last node is destinaiton_vertex
                if last_node == destination_vertex:
                    return current_path
                # add to visited
                visited.add(last_node)
                # add the path to its neighbors to back of queue
                for v in self.vertices[last_node]:
                    #clone the path
                    new_path = current_path.copy()

                # add neighbor to the back of the queue 
                    new_path.append(v)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order. just copy paste lol
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        
        while stack.size() > 0:
            current_path = stack.pop()
            last_node = current_path[-1]
            if last_node not in visited:
                if last_node == destination_vertex:
                    return current_path
                visited.add(last_node)
                for v in self.vertices[last_node]:
                    new_path = [*current_path]
                    new_path.append(v)
                    stack.push(new_path)



    def dfs_recursive(self, starting_vertex, destination_vertex,s= Stack(), visited = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        
        """
        """
===== DFS =====
1. Starting Node + Target Node
2. Add [starting_node] to path, and push it to stack
3. pop last item from stack
4. check the last item in the path, for instance [1, 2, 4, 6, 7]... check 7 (path[-1])
5. add path[-1] to your visited
6. get neighbors of path[-1]
7. add to your path, so for each neighbor, create a path copy, add the neighbor to end of path
8. push your new path to your stack
9. for instance, if neighbors of 7 are 10, 12, 13, 6, but 6 has been visited
10. [1, 2, 4, 6, 7, 10], [1, 2, 4, 6, 7, 12], [1, 2, 4, 6, 7, 13] will be added to stack
11. when path[-1] is your target, stop and return the path
"""

        
        
        visited = set()

        current_path = s.pop()

        if current_path is None:
            current_path = [starting_vertex]

        if current_path[-1] not in visited:
            visited.add(current_path[-1])

        for v in self.get_neighbors(current_path[-1]):

            if v == destination_vertex:
                current_path.append(v)
                return current_path

            current_p_copy = [*current_path]
            current_p_copy.append(v)

            s.push(current_p_copy)

        return self.dfs_recursive(starting_vertex, destination_vertex, s, visited)

        

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
