import random
from itertools import combinations
from collections import deque

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
        for i in range(numUsers):
            self.addUser(f'User: {i}')

        # Create friendships
        allFriends = list(combinations(range(1, numUsers + 1), 2))
        random.shuffle(allFriends)
        friendships = allFriends[:int(numUsers / 2)]
        for friendship in friendships:
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # trying this with a deque for a now, will work on a non-deque solution afterward

        x = deque()
        visited = {userID: []}
        x.append([self.users[userID]])

        while len(x) > 0:
            path = x.popleft()
            id = path[-1]
            if id not in visited:
                visited[id] = path
                for child in self.friendships[userID]:
                    newpath = path.copy()
                    newpath.append(child)
                    x.append(newpath)            
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

# testing for a larger case (question 2)
    sgXL = SocialGraph()
    sgXL.populateGraph(1000, 5)
    print(sgXL.friendships)
    connectionsXL = sgXL.getAllSocialPaths(1)
    print(connectionsXL)
"""
Questions:

1. To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why?

For this we would be looking at (100 * 10) = 1000 total friendships. We don't need to run call addFriendship 1000 times, however; since the relationships are bidirectional, 500 will suffice.

2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
"""