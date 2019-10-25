from util import Queue
from random import randint, choice
from typing import List, Dict, Set

class User:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"User({self.name})"

    def __str__(self) -> str:
        return self.name

class SocialGraph:
    def __init__(self):
        self.lastID: int = 0
        self.users = dict()
        self.friendships = dict()

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
        self.users = dict()
        self.friendships = dict()

        NAME_LENGTH = numUsers // avgFriendships

        # Add users
        for x in range(numUsers):
            self.addUser(self.random_string(NAME_LENGTH))


        # Create friendships
        for x in range(1, numUsers + 1):
            for j in range(avgFriendships):
                self.addFriendship(x, randint(1, numUsers))

        pass



    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
        q.enqueue([userID])
        while q.size > 0:
            path = q.dequeue()
            newUserID = path[-1]
            if newUserID not in visited:
                visited[newUserID] = path
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        new_path = list(path)
                        new_path.append(friendID)
                        q.enqueue(new_path)

        return visited
        
    @staticmethod
    def random_string(length: int) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        return ''.join(choice(alphabet) for _ in range(length))


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
