import random
##had to copy queue into this directory
from util import Queue


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
        # Create friendships
        friendship_combos = []

        for userID in self.users:
            for friendID in range(userID +1, self.lastID + 1):
                    friendship_combos.append((userID, friendID))
        random.shuffle(friendship_combos)
        sumOfFriends = (avgFriendships * numUsers)/2
        ##using int() to convert float to whole number
        friends_to_make = friendship_combos[ : int(sumOfFriends) ]

        for friendship in friends_to_make:
            first_friend = friendship[0]
            second_friend = friendship[1]
            self.addFriendship(first_friend, second_friend)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
        path = [userID]
        q.enqueue(path)
        while q.size():
            path = q.dequeue()
            node = path[-1]
            if node not in visited:
                visited[node] = path
                for friend in self.friendships[node]:
                    copiedPath = path[:]
                    copiedPath.append(friend)
                    q.enqueue(copiedPath)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
