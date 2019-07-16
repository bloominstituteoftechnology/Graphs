import random

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
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        
        self.vertices[v1].add(v2)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create queue, visited flag and add the starting vertex to the queue
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])

        #while not empty, dequeue and place in path
        #record the vertex as the last item in the path
        while q.size():
            path = q.dequeue()
            vertex = path[-1]
            #if the vertex is equal to the destination return the path
            if vertex == destination_vertex:
                return path
            #if the vertex has not been visited
            elif vertex not in visited:
                #for each item in the current path
                for next in self.vertices[vertex]:
                    #create a copy of the old path, append the next item to this new path, and add the new path to the queue
                    new_path = list(path)
                    new_path.append(next)
                    q.enqueue(new_path)
                #mark vertex as visited
                visited.add(vertex)
        #edge case if destination_vertex is not found
        if vertex != destination_vertex:
            return f"path from {starting_vertex} to {destination_vertex} not found"
        return path

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(numUsers):
            self.addUser(user)

        # create possible friendship combinations
        # for each userid in users and potienal friends present make a combination of friendships
        friend_combo = []
        for userID in self.users:
            for friendID in range(userID + 1, numUsers):
                if userID != friendID:
                    friend_combo.append((userID, friendID))

        #shuffle the friend combos and take N number of friendships
        random.shuffle(friend_combo)

        totalFrienships = avgFriendships * numUsers
        
        friends_to_make = friend_combo[:int(totalFrienships/2)]

        # Create friendships
        # for each friendship link the friends to the user
        for friendship in friends_to_make:
            friend1 = friendship[0]
            friend2 = friendship[1]
            self.addFriendship(friend1, friend2)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them. <-- bfs

        The key is the friend's ID and the value is the path.
        """

        #create graph
        graph = Graph()

        #loop through user friendships
        #add vertex and edges to graph
        for user in self.friendships:
            for friend in self.friendships[user]:
                graph.add_edge(user, friend)

        visited = {}  # Note that this is a dictionary, not a set
        q = []
        path = []
        current_user = []

        q.append(userID)

        #while the queue is not empty
        # current user is the removed from the queue
        #run bfs to find shortest distance from userID to current user
        #if there is a extended connection, add path to visited
        #add the current users friends to the queue if not visited
        while len(q):
            current_user = q.pop(0)
            path = graph.bfs(userID, current_user)
            if type(path) is not str:
                visited[current_user] = path
            else:
                visited[current_user] = None
            for friend in self.friendships[current_user]:
                if friend not in visited:
                    q.append(friend)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
