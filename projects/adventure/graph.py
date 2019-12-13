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
        # Check if visited
        #print("room now in: ", starting_vertex)
        #print("exits: ", roomNeighbors[1])
        if starting_vertex not in visited: 
            visited.add(starting_vertex)
            #print("Currently in room", starting_vertex)
            # Drill through the dictionary to necessary information
            for i in roomNeighbors.items():
                for j in i[1]:
                    currentRoom = i[0]
                    neighborDirection = j
                    neighborNumber = i[1][j]
                    numberOfExits = len(i[1])
                    # print("neighbor direction: ", neighborDirection)
                    # print("neighbor number: ", neighborNumber)
                    if numberOfExits == 1:
                        #print("dead end found", currentRoom)
                        #print("data looking at: ", i[1])
                        endPoints.add(currentRoom)
                    if numberOfExits > 1 and neighborNumber not in visited:
                        #print("Heading to: ", neighborNumber)
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

        # pathfinder - lists of visited nodes from one target to the next
        pathfinder.add(starting_vertex)
        visitedMasterList.add(starting_vertex)
        #print("Starting vertex is: ", starting_vertex)
        # Path - path to target, what's appended into traversal
        path = path + [starting_vertex]
        print("Current room: ", starting_vertex)
        #print("test: ", roomNeighbors[starting_vertex])
        print("length of visit: ", len(visited))
        # If destination found and all nodes visitedMasterList
        #if starting_vertex == destination_vertex and traversalPath has len(roomNeighbors) == len(visitedMasterList):
        if starting_vertex == destination_vertex and len(visited) == 0:    
            path = path + [starting_vertex]
            print("Destination reached, all nodes visitedMasterList")
            print("Length of room: ", len(roomNeighbors))
            print("lenght of visited: ", len(visited))
            #print(visitedMasterList)
            print("Path as of now is: ", path)
            print("Traversal as of now is: ", traversalPath)
            #traversalPath = traversalPath[:-1]
            #print("traversal after slicing: ", traversalPath)
            for i in path:
                traversalPath.append(i)
            print("Traversal after appendate of path: ", traversalPath)
            return traversalPath
        # If destination found but nodes unvisitedMasterList
        #if starting_vertex == destination_vertex and len(roomNeighbors) != len(traversalPath):
        if starting_vertex == destination_vertex and len(visited) > 0:
            print("length of visited: ", len(visited))
            # Endpoints not yet exhausted
            if endPoints != set():
            # Locate next endpoint
                print("Endpoints not yet depleted")
                nextDestination = endPoints.pop()
                print("head to: ", nextDestination)
                #print("remaining endpoints: ", endPoints)
            # Copy over current path into traversal
                print("traversal path start: ", traversalPath)
                print("path current: ", path)
                print("pathfinder: ", pathfinder)
                for i in path:
                    traversalPath.append(i)
                print("traversal path now: ", traversalPath)
                current = traversalPath[-1]
                #print("visited master list: ", visitedMasterList)
                pathfinder = set()
                path = []
                self.dfs_recursive(current, nextDestination, pathfinder, path, roomNeighbors, endPoints, traversalPath, visitedMasterList, visited)
            
            # Endpoints exhausted, time to find a random node
            if endPoints == set():
                print("endpoints exhausted")
                print("Room list to date: ", traversalPath)
                print("length of visited: ", len(visited))
                
                print("path up to exhaustion: ", path)
                for i in path:
                    traversalPath.append(i)
                print("Traversal up to exhaustion: ", traversalPath)
                # Update visited list
                for i in traversalPath:
                    print("to be deleted from masterlist ", i)
                    visited.discard(i)
                
                print("cleaned masterlist: ", visited)
                if visited == set():
                    return traversalPath
                #print("visited rooms to date: ", visitedMasterList)
                # Reset pathfinder
                pathfinder = set()
                path = []
                current = traversalPath[-1]
                backupDestination = visited.pop()
                #traversalPath.append(backupDestination)
                #print("traversal path, appended backup: ", traversalPath)
                # Need a starting location, current room
                print("current room: ", current)
                print("Next backup: ", backupDestination)
                self.dfs_recursive(current, backupDestination, pathfinder, path, roomNeighbors, endPoints, traversalPath, visitedMasterList, visited)
            # for i in path:
            #     # print("sending Path to traversal, resetting")
            #     traversalPath.append(i)
            
            # for i in traversalPath:
            #     print("currently trodden: ", i)
            #     visited.discard(i)
            # Reset pathfinder so it will retread if needed
                
        for i in roomNeighbors[starting_vertex]:
            neighbors = roomNeighbors[starting_vertex][i]
            #print("Neighbors from for-loop: ", neighbors)
            if neighbors not in pathfinder:
                # for j in i:
                #     print("TEst 2: ", j)
                newPath = self.dfs_recursive(neighbors, destination_vertex, pathfinder, path, roomNeighbors, endPoints, traversalPath, visitedMasterList, visited)
                #print("newPath is: ", newPath)
                if newPath is not None:
                    return newPath
        print("No path")
        return None
        # Catchall if there's no path, return none

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
        # s = Stack()
        # path = [starting_vertex]
        # s.push(path)
        # visited = set()
        # while s.size() > 0:
        #     nextPath = s.pop()
        #     lastNode = nextPath[-1]
        #     if lastNode not in visited:
        #         if lastNode == destination_vertex:
        #             #print("dfs path found")
        #             return nextPath
        #         visited.add(lastNode)
        #         for i in self.vertices[lastNode]:
        #             newPath = list(nextPath)
        #             newPath.append(i)
        #             s.push(newPath)
        
        s = Stack()
        s.push( [starting_vertex] )
        visited = set()
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in visited:
                if v == destination_vertex:
                    return path
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    path_copy = path.copy()
                    path_copy.append(neighbor)


    
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
