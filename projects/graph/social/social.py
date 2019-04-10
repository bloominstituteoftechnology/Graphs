
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
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

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
            self.addUser(F"User {i}")
        

        # Create friendships
        # --- Following approach has O(n^2) runtime because of combinations, gets slow when n>1000 ----
        all_friendships = list(combinations(range(1, numUsers+1), 2))

        #----- Fisher yates shuffle
        for i in range(0, len(all_friendships)):
            j = random.randint(i, len(all_friendships)-1)
            all_friendships[i], all_friendships[j] = all_friendships[j], all_friendships[i]
    
        friendships = all_friendships[:int(numUsers*avgFriendships/2)]
        for friendship in friendships:
            self.addFriendship(friendship[0], friendship[1])
        
        # --- Following approach has O(n) runtime because of combinations, gets slow when friendship density is high ----
        # total = numUsers * avgFriendships // 2
        # count = 0
        # while count < total:
        #     random1 = random.randrange(1,len(self.users)-1)
        #     random2 = random.randrange(1,len(self.users)-1)
        #     print(random1,random2)
        #     friendship = self.addFriendship(random1, random2)
        #     if friendship:
        #         count += 1
        
        
        
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendshipact path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = deque()
        q.append([userID])
        while len(q) > 0:
            # print(visited)
            path = q.popleft()
            user = path[-1]
            if user not in visited:
                for friend in self.friendships[user]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    q.append(path_copy)
                    visited[user] = path
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print('friendships:')
    print(sg.friendships)
    print('connections:')
    connections = sg.getAllSocialPaths(1)
    print(connections)
