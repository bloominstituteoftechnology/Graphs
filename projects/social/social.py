import random
import math

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size():
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

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
        friendship_combinations = []
        # avg Friendships = totalFriendships / numUsers
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                if userID != friendID:
                    friendship_combinations.append((userID, friendID))
        # shuffle friendship combinations
        random.shuffle(friendship_combinations)
        totalFriendships = avgFriendships * numUsers
        # take the N Number of friendships
        friends_to_make = friendship_combinations[:math.floor( totalFriendships / 2) ]

        # make all possible friendship combinations
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
        
        #implement bfs
        # make a queue
        queue = Queue()
        # enqueue userID
        queue.enqueue([userID])
        # while queue isn't empty
        while queue.size():
            # dequeue the path
            path = queue.dequeue()
            # last thing on path is the new current item
            newUserID = path[-1]
            # if newUserID isn't visited
            if newUserID not in visited:
                visited[newUserID] = path
                # for each of friendID's neighbor's
                for friendID in self.friendships[newUserID]:
                    if friendID not in visited:
                        # copy path
                        new_path = path.copy()
                        # append friendID to path
                        new_path.append(friendID)
                        # enqueue new_path
                        queue.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
