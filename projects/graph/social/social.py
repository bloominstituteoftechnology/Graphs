from queue import *
import random


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
        try:
            if userID == friendID:
                None
            elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
                None
            else:
                self.friendships[userID].add(friendID)
                self.friendships[friendID].add(userID)
        except:
            return self.friendships

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
            self.addUser(f"User {i+1}")

        # Create friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)
        return possibleFriendships[:20]
        # print(len(possibleFriendships))

        # Create friendships
# total == avg

        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # Create an empty queue
        q = Queue()
        # Put UserID in our Queue
        q.put([userID])
        # while queue is not empty...
        while q.qsize() > 0:
            # Dequeue first path from queue
            path = q.get()
            # get the current node from the last element in the path
            v = path[-1]
            # if that node is not in the visited dict
            if v not in visited:
                # mark it as visited
                visited[v] = path
                # print("friendships:", self.friendships)
                # Then, put paths to all of it's children into the queue
                for friendship in self.friendships[v]:
                    if friendship not in visited:
                        q.put(list(path) + [friendship])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    sg.addUser(1)
    sg.addUser(2)
    sg.addUser(3)
    sg.addUser(4)
    sg.addUser(5)
    sg.addUser(6)
    sg.addUser(7)
    sg.addUser(8)
    sg.addUser(9)
    sg.addUser(10)
    sg.addFriendship(1, 8)
    sg.addFriendship(1, 10)
    sg.addFriendship(1, 5)
    sg.addFriendship(2, 10)
    sg.addFriendship(2, 5)
    sg.addFriendship(2, 7)
    sg.addFriendship(3, 4)
    sg.addFriendship(3, 6)
    sg.addFriendship(3, 7)
    sg.addFriendship(3, 1)
    sg.addFriendship(4, 9)
    sg.addFriendship(4, 3)
    sg.addFriendship(5, 8)
    sg.addFriendship(5, 2)
    sg.addFriendship(5, 1)
    sg.addFriendship(6, 10)
    sg.addFriendship(7, 2)
    sg.addFriendship(8, 5)
    sg.addFriendship(8, 1)
    sg.addFriendship(9, 4)
    sg.addFriendship(10, 1)
    sg.addFriendship(10, 2)
    sg.addFriendship(10, 6)
    connections = sg.getAllSocialPaths(10)
    print(f"connections is {connections}")

# qustion 1. it would be O(!n) factorial of n
# the other question is weird lol.
