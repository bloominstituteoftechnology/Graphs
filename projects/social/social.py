import random
import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue, Stack

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

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
        # call addUser() until our number of users is numUsers
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create random friendships
        # totalFriendships = avgFriendships * numUsers
        # Generate a list of all possible friendships
        possibleFriendships = []
        # Avoid dups by ensuring the first ID is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append( (userID, friendID) )

        # Shuffle the list
        random.shuffle(possibleFriendships)
        # print("random friendships:")
        # print(possibleFriendships)

        # Slice off totalFriendships from the front, create friendships
        totalFriendships = avgFriendships * numUsers // 2
        # print(f"Friendships to create: {totalFriendships}\n")
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.addFriendship( friendship[0], friendship[1] )




    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        q.enqueue([userID])
       
        # Create a Set to store visited vertices
        visited = {}
         # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Mark it as visited...
            v = path[-1]
            
            if v not in visited:
                visited[v] = path
                #for every value in the vertices from the last item in the list
                for friendID in self.friendships[v]:
                    # CHECK IF IT'S THE TARGET
                    path_copy = path.copy()
                    path_copy.append(friendID)
                    q.enqueue(path_copy)
        return visited
        
  

     


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print("USERS:")
    print(sg.users)
    print("FRIENDSHIPS:")
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)