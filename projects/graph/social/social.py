from itertools import combinations
from random import shuffle
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
            self.addUser(f"User {i}")

        # Create friendships
        possible_friendships = list(combinations(range(1, numUsers+1), 2))
        shuffle(possible_friendships)
        num_friendships = avgFriendships * numUsers
        friendship_list = possible_friendships[:num_friendships//2]
        for friendship in friendship_list:
            self.addFriendship(friendship[0], friendship[1])
        
        

    def getAllSocialPaths(self, userID, q=None, visited=None, path=None):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        if not visited:
            q = deque()
            path = [userID]
            visited = {userID: path}
        for related in self.friendships[userID]:
            new_path = path[:]
            new_path.append(related)
            if related not in visited:
                q.append((related, new_path))
                visited[related] = new_path
        if len(q) == 0:
            return visited
        if len(q) > 0:
            user, path = q.popleft()
            return self.getAllSocialPaths(user, q, visited, path)


"""
To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why?
    - 500 becuase friendships are bi-directional and 1000 friendships would average out to 10 per user.

If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
    - About 100%
    - Avg is 3 intermediate people
    - They say there's about ~6 degrees of separation between any person on the planet and another
"""


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

