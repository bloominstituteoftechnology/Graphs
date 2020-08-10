"""
Simple graph implementation
"""
from util import Stack, Queue  
import collections

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
        # make a Queue
        que = Queue()
        # enqueue our starting node
        que.enqueue(starting_vertex)
        # make a set to track if we've been here before 
        visited = set()
        # while our queue isn't empty
        while que.size() > 0:
        # dequeue whatever's at the front of our line this is our current_node
            current_node = que.dequeue()
            print(current_node)
        # if we haven't visited this node yet
            if current_node not in visited:
        # mark as Visited
                visited.add(current_node)
        # get it's neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of the neighbors add to the queue
                for neighbor in neighbors:
                    if neighbor not in visited:
                        que.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a Stack
        stack = Stack()
        # push on our starting node
        stack.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our stack isn't empty
        while stack.size() > 0:
        # pop off whatever's on top this is our current_node
            current_node = stack.pop()
            if current_node not in visited:
                print(current_node)
        # if we haven't visited this vertex yet then mark as Visited
            if current_node not in visited:
                    visited.add(current_node)
        # get it's neighbors
                    neighbors = self.get_neighbors(current_node)    
        # for each of the neighbors add to the stack
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Keep track of visited outside of recursive call
        # mark this vertex as visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
        # if its not visited
            if neighbor not in visited:
         # recurse on the neighbor
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # make a queue
        que = Queue()
        # make a set to track nodes we've visited
        visited = set()

        path = [starting_vertex]
        que.enqueue(path)

        # while queue is not empty
        while que.size() > 0:
        # dequeue the node at the front of the line
            current_path = que.dequeue()
            current_node = current_path[-1]
        # if this node is our target node
            if current_node == destination_vertex:
        # return true, it is in our network
                return current_path
        # if not vitied
            if current_node not in visited:
        # mark as visited
                visited.add(current_node)
        # get neighbors
                neighbors = self.get_neighbors(current_node)
        # for each neighbor
                for neighbor in neighbors:
        # copy path so we don't mutate the original path
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
        # add to  queue
                    que.enqueue(current_path + [neighbor])


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size() > 0:
            current = stack.pop()
            visited.add(current)

            for edge in self.get_neighbors(current):
                if edge not in visited:
                    stack.push(edge)
                if edge is destination_vertex:
                    visited.add(edge)
                    return list(visited)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
            path = collections.deque([])
            path.append([starting_vertex])

        visited.add(starting_vertex)
        current = path.pop()
        last = current[-1]
        
        for last in self.get_neighbors(last):
            if last not in visited:
                route = list(current)
                route.append(last)
                path.append(route)
                if last is destination_vertex:
                    return route

        return self.dfs_recursive(last, destination_vertex, visited, path)

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
