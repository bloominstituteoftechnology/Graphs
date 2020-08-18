"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
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
        # if self.vertices[v1]:
        #     self.vertices[v1].add(v2)
        # else:
        #     self.add_vertex(v1)
        #     self.vertices[v1].add(v2)

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
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our queue isn't empty 
        while q.size() > 0:
        # dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
            print(current_node)
            # print(f"{current_node}")
            # if we haven't visited this node yet mark as visited
            if current_node not in visited:
                visited.add(current_node)
                # get neighbors
                neighbors = self.get_neighbors(current_node)
                # for each neighbor, add to queue
                for neighbor in neighbors:
                    if neighbor not in visited:
                        q.enqueue(neighbor)
        

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we have visited before
        visited = set()
        # while our stack isn't empty
        while s.size() > 0:
            # pop off whatever is on top, this is current_node
            current_node = s.pop()
            if current_node not in visited:
                print(current_node)
                # print(f"{current_node}")
            # if we have not visited this vertex before mark as visited
            if current_node not in visited:
                visited.add(current_node)
                # get neighbors
                neighbors = self.get_neighbors(current_node)
                # for each neighbor, add to stack
                for neighbor in neighbors:
                    if neighbor not in visited:
                        s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for edge in self.vertices[starting_vertex]:
            if edge not in visited:
                self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = collections.deque([])
        q.append([starting_vertex])
        visited = set()
        
        while q.count is not 0:
            current = q.popleft()
            last = current[-1]
            if last not in visited:
                for neighbor in self.get_neighbors(last):
                    route = list(current)
                    route.append(neighbor)
                    q.append(route)
                    if neighbor is destination_vertex:
                        return route
                visited.add(last)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            current = s.pop()
            visited.add(current)
            for edge in self.get_neighbors(current):
                if edge not in visited:
                    s.push(edge)
                if edge is destination_vertex:
                    visited.add(edge)
                    return list(visited)
                

    # def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, s=None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     if visited is None:
    #         visited = set()
    #         s = collections.deque([])
    #         s.append([starting_vertex])
    #     visited.add(starting_vertex)
    #     current = s.pop()
    #     last = current[-1]
    #     for last in self.get_neighbors(last):
    #         if last not in visited:
    #             route = list(current)
    #             route.append(last)
    #             s.append(route)
    #             if last is destination_vertex:
    #                 return route
            
    #     return self.dfs_recursive(last, destination_vertex, visited, s)
        
    # Lecture Solution
    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​
        This should be done using recursion.
        """
        ## mark our node as visited
        visited.add(vertex)
        ## check if it's our target node, if so return
        if vertex == destination_vertex:
            return path
        if len(path) == 0:
            path.append(vertex)
        ## iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        ### check if visited
        for neighbor in neighbors:
            if neighbor not in visited: 
        #### if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
        ##### if this recursion returns a path,
                if result is not None:
            ###### return from here
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
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
