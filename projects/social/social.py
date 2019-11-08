import random
import math
import time

class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)


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
        # loop over a range of 0 to numUsers
        for i in range(0, numUsers):
            # add user to the graph
            self.addUser(f"User {i}")

        # Create friendships
         # make a list of possible friendships
        possibleFriendships = []

        # avoid duplicates ensuring that the first number is smaller than the second

        # loop over userID in users
        for userID in self.users:
            # loop over friend id in a range from user id + 1 to the lastID +1
            for friendID in range(userID + 1, self.lastID + 1):
                # append the tuple of (user id , friend id) to the possible friendships list
                possibleFriendships.append((userID, friendID))

        # shuffle the possible friendships using the random.suffle method
        random.shuffle(possibleFriendships)
        for i in range(0, math.floor(numUsers * avgFriendships / 2)):
            # set the friendship to possible friends at i
            friendship = possibleFriendships[i]
            # add friendship of friendship[0] and friendship[1]
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
        # create a queue
        queue = Queue()
        # enqueue the user id as a list
        queue.enqueue([userID])

        # while queue is not empty
        while queue.size() > 0:
            # dequeue to path variable
            path = queue.dequeue()
            # set new user id to the last item in path
            new_user_id = path[-1]

            # check if the new user id is not in the visited structure
            if new_user_id not in visited:
                # set the new user ids path in visited
                visited[new_user_id] = path

                # loop over each friend id in the friendships at the index of new user id
                for friend_id in self.friendships[new_user_id]:
                    # check that the friend id is not in visited
                    if friend_id not in visited:
                        # create a copy of the path
                        new_path = list(path)
                        # append the friend id to the copy of the path
                        new_path.append(friend_id)
                        # enqueue the copy of the path
                        queue.enqueue(new_path)

        # return the visited data structure
        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
