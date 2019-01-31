import random
from collections import deque
from itertools import combinations

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
            self.addUser(f"User {i}")

        # Create friendships
        possible_friendships = list(combinations(range(1, len(self.users) + 1), 2))
        random.shuffle(possible_friendships)
        total = (numUsers * avgFriendships) // 2
        sliced_friendships = possible_friendships[:total]
        for friendship in sliced_friendships:
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
        if self.friendships[userID]:
            for i in range(1, self.lastID + 1):
                visited[i] = self.bfs(userID, i)
        return visited

    def bfs(self, starting_node, target_node):
        q = deque()
        visited = set()
        q.append([starting_node])
       
        while q:
            dequeued = q.popleft()
            end_path = dequeued[-1]
            if end_path not in visited:
                if end_path == target_node:
                    return dequeued
                visited.add(end_path)
                for child in self.friendships[end_path]:
                    copy = list(dequeued)
                    copy.append(child)
                    q.append(copy)
        return f'There is no path'

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    
    degree_of_sep = []
    for key in connections:
        degree_of_sep.append(len(connections[key]))
    print(sum(degree_of_sep) / len(degree_of_sep))

"""
1. To create 100 users with an average of 10 friends each, how many times would you need to call `addFriendship()`? Why?
    100 * 10 //2 => 500 Each instance of addFriendship() creates two friendships so it only needs to be called half as many times as the total number of friendships.
2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
    Nearly 99% and average degree of separation is about 5
"""