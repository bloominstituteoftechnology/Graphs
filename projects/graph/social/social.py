from random import shuffle
from itertools import combinations
from collections import OrderedDict

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

        Creates that number of users and a randomly  distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        user_combos = []
        avg = numUsers * avgFriendships // 2
        
        for i in range(0, numUsers):
            self.addUser(f"User {i}")

        c = combinations(self.users, 2)
        
        for i in c:
            user_combos.append(i)
        shuffle(user_combos)
        
        for i in user_combos:
            if avg == 0:
                break
            self.addFriendship(i[0], i[1])
            avg -= 1



     def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a  dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {userID: [userID]}
        d = []
        d.append([userID])

        while d:
            path = d.pop()
            user = path[-1]
            for friend in self.friendships[user]:
                if friend not in visited:
                    social_path = path + [friend]
                    visited[friend] = social_path
                    d.append(social_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
