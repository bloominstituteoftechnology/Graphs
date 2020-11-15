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
        # Create new key with vertex id and set value to empty set
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()



    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Find v1 in our verticies, add V2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
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
        # Create an empty queue an enqueue the starting vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
        # Create an empty set to track visitied verticies
        visited_set = set()

        # while the queue is not empty
        while queue.size() > 0:
            # get the current vertex (deque from queue)
            current_vertex = queue.dequeue()
            # Check if the current vertex has been visited:
            if current_vertex not in visited_set:
                # print the current vertex
                print(current_vertex)
                # mark the current vertex as visited
                # add the current vertex to a visited_set
                visited_set.add(current_vertex)

                # queue up all the current vertex's neighbors (so we can visit them next)
                for neighbor in self.get_neighbors(current_vertex):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited_set = set()

        while stack.size() > 0:
            current_vertex = stack.pop()

            if current_vertex not in visited_set:
                print(current_vertex)
                visited_set.add(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex in visited:
            return None
        else: 
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                neighborSearch = self.dft_recursive(neighbor, visited)
                if neighborSearch is not None:
                    return [starting_vertex] + neighborSearch
                    
        return None




    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue an enqueue the starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create an empty set to track visitied verticies
        visited_set = set()

        # while the queue is not empty
        while queue.size() > 0:
            # get the current vertex (deque from queue)
            path = queue.dequeue()
            last = path[-1]

            # Check if the current vertex has been visited:
            if last not in visited_set:
                if last == destination_vertex:
                    return path
                # print the current vertex
                print(last)
                # mark the current vertex as visited
                # add the current vertex to a visited_set
                visited_set.add(last)

                # queue up all the current vertex's neighbors (so we can visit them next)
                for neighbor in self.get_neighbors(last):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

    # version with a dictionary
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue an enqueue the starting vertex
        queue = Queue()
        queue.enqueue(
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        )
        # Create an empty set to track visitied verticies
        visited_set = set()

        # while the queue is not empty
        while queue.size() > 0:
            # get the current vertex (deque from queue)
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            # Check if the current vertex has been visited:
            if current_vertex not in visited_set:
                if current_vertex == destination_vertex:
                    return current_path
                # print the current vertex
                print(current_vertex)
                # mark the current vertex as visited
                # add the current vertex to a visited_set
                visited_set.add(current_vertex)

                # queue up all the current vertex's neighbors (so we can visit them next)
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    queue.enqueue({
                        'current_vertex': neighbor,
                        'path': [starting_vertex]
                    })


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack add the starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # Create an empty set to track visitied verticies
        visited_set = set()

        # while the stack is not empty
        while stack.size() > 0:
            path = stack.pop()
            last = path[-1]
            if last not in visited_set:
                if last == destination_vertex:
                    return path
                print(last)

                visited_set.add(last)
            
            for neighbor in self.get_neighbors(last):
                new_path = list(path)
                new_path.append(neighbor)
                stack.push(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty queue an enqueue the starting vertex
        stack = Stack()
        stack.push(
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        )
        # Create an empty set to track visitied verticies
        visited_set = set()

        # while the queue is not empty
        while queue.size() > 0:
            # get the current vertex (deque from queue)
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            # Check if the current vertex has been visited:
            if current_vertex not in visited_set:
                if current_vertex == destination_vertex:
                    return current_path
                # print the current vertex
                print(current_vertex)
                # mark the current vertex as visited
                # add the current vertex to a visited_set
                visited_set.add(current_vertex)

                # queue up all the current vertex's neighbors (so we can visit them next)
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    stack.push({
                        'current_vertex': neighbor,
                        'path': [starting_vertex]
                    })

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex in visited:
            return None
        elif starting_vertex == destination_vertex:
            return [destination_vertex]
        else:
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                neighborSearch = self.dfs_recursive(neighbor, destination_vertex, visited)
                if neighborSearch is not None:
                    return [starting_vertex] + neighborSearch
                
        return None


        # if type(starting_vertex) is list:
        #     if starting_vertex[-1] == destination_vertex:
        #         return starting_vertex
        #     path = starting_vertex
        # else:
        #     path = [starting_vertex]

        # for neighbor in self.get_neighbors(path[-1]):
        #     if neighbor == destination_vertex:
        #         path.append(neighbor)
        #         return path
        #     else:
        #         path.append(neighbor)
                
        # return self.dfs_recursive(path, destination_vertex)

    

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
    print(graph.vertices)

    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    # print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    # '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
