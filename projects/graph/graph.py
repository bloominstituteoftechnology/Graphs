"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


from collections import deque
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # vertex ID --> set of neighbors
        self.vertices = {}

    # def __repr__(self):
    #     return str(self.vertices)

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        
    # adds directed edge from "from_vertex" to "to_vertex"
    def add_edge(self, from_vertex_id, to_vertex_id):
        """
        Add a directed edge to the graph.
        """
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print ("Attempting to add edge to non existing node")
            return
        self.vertices[from_vertex_id].add(to_vertex_id) #.add is method for set

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    #remove vertex from graph and any incoming edges to it
    def remove_vertex(self,vertex_id):
        if vertex_id not in self.vertices:
            print("Attempting to remove non existant vertices")
            return

        self.vertices.pop(vertex_id)
        for remaining_vertex in self.vertices:
            self.vertices[remaining_vertex].discard(vertex_id)

    def remove_edge(self,from_vertex_id,to_vertex_id):
        if from_vertex_id not in self.vertices or to_vertex_id not in self.vertices:
            print("Attempting to remove edges non existant vertex")
            return
        self.vertices[from_vertex_id].discard(to_vertex_id)
        
        

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = deque()
        visited = set()
        queue.append(starting_vertex)
        while len(queue)>0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print (currNode)
                for neigbor in self.vertices[currNode]:
                    queue.append(neigbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = deque()
        visited = set()
        stack.append(starting_vertex)
        while len(stack)>0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print (currNode)
                for neigbor in self.vertices[currNode]:
                    stack.append(neigbor)


    def dft_recursive(self, starting_vertex,visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.vertices[starting_vertex]:
                self.dft_recursive(neighbor,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = deque()
        visited = set()
        queue.append([starting_vertex])
        while len(queue)>0:
            currPath = queue.popleft()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    queue.append(newPath)
       
        
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        visited = set()
        #push the current path you are onto stack, instwead of single vertex
        stack.append([starting_vertex])
        while len(stack)>0:
            currPath = stack.pop()
            currNode = currPath[-1] # current node you are on is the last node in the path
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neigbor in self.vertices[currNode]:
                    newPath = list(currPath) # make copy of curr path
                    newPath.append(neigbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited=set()
        return self.dfs_recursive_helper([starting_vertex],destination_vertex,visited)

    # return path to goal vertex if it exists , if not it will return empty array.
    def dfs_recursive_helper(self,curr_path,destination_vertex,visited):
        curr_vertex = curr_path[-1]
        #Base-Case
        if curr_vertex == destination_vertex:
            return curr_path

        visited.add(curr_vertex)   

        # find neighbors of current vertex and make a copy of current path. 
        # If neighbor is not in visited then append it to copy of curr path
        # recurse over copy of curr path , until goal vertex is reached. 
        for neighbor in self.vertices[curr_vertex]:
            if neighbor not in visited:
                new_path = list(curr_path)
                new_path.append(neighbor)
                res = self.dfs_recursive_helper(new_path,destination_vertex,visited)
                if len(res)>0:
                    return res

        return []



        


        

        
        

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

    # graph.remove_edge(8,1)

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
    #graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft(1)
   # graph.dft_recursive(1)

    '''
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
    print(graph.dfs_recursive(1, 6))

