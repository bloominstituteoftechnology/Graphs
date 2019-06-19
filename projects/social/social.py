import random
import sys
sys.path.append('../graph')
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

    def num_friends(self, userId):
        return len(self.friendships[userId])

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
            self.addUser(i + 2 * numUsers)

        total = numUsers
        # Create friendships
        for key in self.users.keys():
            if total == 0:
                break
            t = random.randint(1,min(total + 1,5))
            r = random.sample(range(0, numUsers),t)
            for i in r:
                if key < i and i not in self.friendships[key] and self.num_friends(key) < 4 and total > 0:
                    self.addFriendship(key, i)
                    total -= 1

        while total > 0:
            # print('total', total)
            dumper = random.randint(1, numUsers)
            loop = 0
            while self.num_friends(dumper) < 4 and total > 0 and loop < 10:
                r = random.randint(0, numUsers)
                if dumper < r and r not in self.friendships[dumper]:
                    self.addFriendship(dumper, r)
                    total -= 1
                loop += 1


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # loop = 0
        q = Queue()
        q.enqueue(userID)
        visited[userID] = [userID]
        while q.size() > 0:
            # print('q.size', q.size())
            v = q.dequeue()
            # print('v',v)
            for friend in self.friendships[v]:
                if friend != v and friend != userID and friend not in visited:
                    # print('friend', friend, 'visited[userID]', visited[userID])
                    visited[friend] = [*visited[v], friend]
                    q.enqueue(friend)
            # loop += 1
            # if loop >= 10:
            #     break
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
