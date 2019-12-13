"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from room import Room as room


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.recursiveVisited = set()
        self.recursiveVisited2 = set()
        self.path = list()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, node, neighbor):
        """
        Add a directed edge to the graph.
        """
        if node in self.vertices and neighbor in self.vertices:
            self.vertices[node].add(neighbor)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex, vertices, book):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create empty queue and enque the starting vertex ID
        # Create empty set to store visited Vertices
        # while queue is not empty, 
            # Dequeue first vertex
            # if that vertex has not been visited
                #Markt it as vissited, then add all of its 
                # # neighbors to the back of the queue
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                book[v] = 0
                visited.add(v)
                # changed from self.vertices to vertices
                for i in vertices[v]:
                    q.enqueue(i)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for i in self.vertices[v]:
                    #print("I is ", i)
                    s.push(i)
        

    def dft_recursive(self, starting_vertex, roomNeighbors, visited, endPoints):

        if starting_vertex not in visited: 
            visited.add(starting_vertex)
            for i in roomNeighbors.items():
                for j in i[1]:
                    currentRoom = i[0]
                    neighborDirection = j
                    neighborNumber = i[1][j]
                    numberOfExits = len(i[1])
                    if numberOfExits == 1:
                        endPoints.add(currentRoom)
                    if numberOfExits > 1 and neighborNumber not in visited:
                        self.dft_recursive(neighborNumber, roomNeighbors, visited, endPoints)

    # def dfs_test(self, starting_vertex, destination_vertex, pathfindingVisited, roomNeighbors, path, endPoints):
        
    #     print("path at top: ", path)
    #     pathfindingVisited.add(starting_vertex)
    #     path = path + [starting_vertex]
    #     if starting_vertex == destination_vertex:
    #         print("path found")
    #         print(path)
    #         return path
    #     for i in roomNeighbors.items():
    #         for j in i[1]:
    #             currentRoom = i[0]
    #             neighborDirection = j
    #             neighborNumber = i[1][j]
    #             numberOfExits = len(i[1])
    #     # print("neighbor direction: ", neighborDirection)
    #     # print("neighbor number: ", neighborNumber)
    #             if neighborNumber not in pathfindingVisited:
    #                 print("first if")
    #                 newPath = self.dfs_test(neighborNumber, destination_vertex, pathfindingVisited, roomNeighbors, path, endPoints)
    #                 if newPath not in endPoints:
    #                     print("second if")
    #                     return newPath
    #     # for i in self.get_neighbors(starting_vertex):
    #     #     if i not in visited:
    #     #         new_path = self.dfs_recursive(i, destination_vertex, visited, path)
    #     #         if new_path is not None:
    #     #             return new_path
    #     print("No path found")
    #     return None
    #     # Catchall if there's no path, return none
    
    def dfs_recursive(self, starting_vertex, destination_vertex, pathfinder, path, roomNeighbors, endPoints, traversalPath, visitedMasterList, visited):

        pathfinder.add(starting_vertex)
        visitedMasterList.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex and len(visited) == 0:    
            path = path + [starting_vertex]
            for i in path:
                traversalPath.append(i)
            return traversalPath
        if starting_vertex == destination_vertex and len(visited) > 0:
            if endPoints != set():
                nextDestination = endPoints.pop()
                for i in path:
                    traversalPath.append(i)
                current = traversalPath[-1]
                pathfinder = set()
                path = []
                self.dfs_recursive(current, nextDestination, pathfinder, path, roomNeighbors, endPoints, traversalPath, visitedMasterList, visited)
            if endPoints == set():
                for i in path:
                    traversalPath.append(i)
                for i in traversalPath:
                    visited.discard(i)
                if visited == set():
                    return traversalPath
                pathfinder = set()
                path = []
                current = traversalPath[-1]
                backupDestination = visited.pop()
                self.dfs_recursive(current, backupDestination, pathfinder, path, roomNeighbors, endPoints, traversalPath, visitedMasterList, visited)
        for i in roomNeighbors[starting_vertex]:
            neighbors = roomNeighbors[starting_vertex][i]
            if neighbors not in pathfinder:
                newPath = self.dfs_recursive(neighbors, destination_vertex, pathfinder, path, roomNeighbors, endPoints, traversalPath, visitedMasterList, visited)
                if newPath is not None:
                    return newPath
        return None

    def bfs(self, starting_vertex, destination_vertex, vertices, book):
        """ 
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        visited = set()
        while q.size() > 0:
            nextPath = q.dequeue()
            lastNode = nextPath[-1]
            if lastNode not in visited:
                if lastNode == destination_vertex:
                    #print("path found", nextPath)
                    book[destination_vertex] = nextPath
                    #print("Book is: ", book)
                    return nextPath
                visited.add(lastNode)
                for i in vertices[lastNode]:
                    newPath = list(nextPath)
                    newPath.append(i)
                    q.enqueue(newPath)

        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        path = [starting_vertex]
        s.push(path)
        visited = set()
        while s.size() > 0:
            nextPath = s.pop()
            lastNode = nextPath[-1]
            if lastNode not in visited:
                if lastNode == destination_vertex:
                    #print("dfs path found")
                    return nextPath
                visited.add(lastNode)
                for i in self.vertices[lastNode]:
                    newPath = list(nextPath)
                    newPath.append(i)
                    s.push(newPath)
    
    def dfs_recursive2(self, starting_vertex, visited = None, path = None):

        if visited is None:
            visited = set()
        if path is None:
            # array = ordered
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == None:
            print("None found")
            return path
        for i in self.get_neighbors(starting_vertex):
            if i not in visited:
                new_path = self.dfs_recursive2(i, visited, path)
                print(new_path)
                if new_path is not None:
                    print("Path found")
                    return new_path
        
        return None

    def dft_recursive2(self, starting_vertex, path = None):
        if path is None:
            # array = ordered
            path = []
        if starting_vertex not in self.recursiveVisited:
            print("Starting vertext: ", starting_vertex)
            print("Visited: ", self.recursiveVisited)
            # print("last one: ", self.recursiveVisited[-1])
            #solution = starting_vertex
            #print("solution is: ", solution)
            path.append(starting_vertex)
            print("path is: ", path)
            self.recursiveVisited.add(starting_vertex)
            for i in self.vertices[starting_vertex]:
                # if i is None:
                #     print("None found!")
                #solution = i
                print("i is: ", i)
                path.append(i)
                print("path is updated to: ", path)
                self.dft_recursive(i)
        return path, 200
        
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     # '''
#     # Should print:
#     #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     # '''
#     # print(graph.vertices)

#     # '''
#     # Valid BFT paths:
#     #     1, 2, 3, 4, 5, 6, 7
#     #     1, 2, 3, 4, 5, 7, 6
#     #     1, 2, 3, 4, 6, 7, 5
#     #     1, 2, 3, 4, 6, 5, 7
#     #     1, 2, 3, 4, 7, 6, 5
#     #     1, 2, 3, 4, 7, 5, 6
#     #     1, 2, 4, 3, 5, 6, 7
#     #     1, 2, 4, 3, 5, 7, 6
#     #     1, 2, 4, 3, 6, 7, 5
#     #     1, 2, 4, 3, 6, 5, 7
#     #     1, 2, 4, 3, 7, 6, 5
#     #     1, 2, 4, 3, 7, 5, 6
#     # '''
    # print("bft solution: ")
    # graph.bft(1)

#     # '''
#     # Valid DFT paths:
#     #     1, 2, 3, 5, 4, 6, 7
#     #     1, 2, 3, 5, 4, 7, 6
#     #     1, 2, 4, 7, 6, 3, 5
#     #     1, 2, 4, 6, 3, 5, 7
#     # '''
#     # print("dft solution: ")
#     # graph.dft(1)
#     # print("dft recursive solution: ")
#     # graph.dft_recursive(1)

#     # '''
#     # Valid BFS path:
#     #     [1, 2, 4, 6]
#     # '''
    # test = {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # print("bfs path is: ")
    # print(graph.bfs(1, 6, test))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     # print("Normal dfs solution: ")
#     # print(graph.dfs(1, 6))
#     print("dfs recursive solution: ")
#     print(graph.dfs_recursive(1, 6))
