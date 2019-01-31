from random import randint
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

        #Creating every possible friendship
        possible_friendships = list(combinations(range(1, numUsers+1), 2))
        #Shuffle the possible friendships
        shuffle(possible_friendships)
        total_friendships = numUsers * avgFriendships // 2

        friends = possible_friendships[:total_friendships]

        for friend in friends:
            self.addFriendship(friend[0], friend[1])



        """
        O(N) for adding friends
        """
        # target_friendships = numUsers *avgFriendships // 2
        # num_created = 0
        # while num_created < target_friendships:
        #     friendship = (randint(1, numUsers), randint(1, numUsers))
        #     if self.addFriendship(friendship[0], friendship[1]):
        #         num_created += 1

    def getAllSocialPaths(self, userID, queue = None, visited = None, path = None):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        if not visited:
            queue = deque()
            path = [userID]
            visited = {userID: path}

        for friend in self.friendships[userID]:
            _path = path[:]
            _path.append(friend)

            if friend not in visited:
                queue.append((friend, _path))
                visited[friend] = _path
        if len(queue) == 0:
            return visited
        elif len(queue) > 0:
            user, path = queue.popleft()
            return self.getAllSocialPaths(user, queue, visited, path)
                

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)




"""
To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why?
-500 since its bidirectional


If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
-About all of them ~2%
"""