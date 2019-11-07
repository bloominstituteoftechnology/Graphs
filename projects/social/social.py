import random
import math
import time
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
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

        """
        For a one directional Friendship
        elif friendID in self.friendships[userID]:
            print("WARNING: YOU ARE ALREADY FOLLOWING USER")
        else:
            self.friendships[userID].add(friendID)
        """

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraphLinear(self, numUsers, avgFriendships):
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # loop over a range of 0 to numUsers
        for i in range(numUsers):
            # add user to the graph
            self.addUser(f"User {i + 1}")

        # friendships

        # get the target friendships via (numUsers * avgFriendships)
        targetFriendships = (numUsers * avgFriendships)
        # set a counter for total friendships
        totalFriendships = 0
        # set a counter for collisions
        collisions = 0

        # while total friendships is less than the target friendships
        while totalFriendships < targetFriendships:
            # set userID to a random number between 1 and the lastID
            userID = random.randint(1, self.lastID)
            # set friendID to a random number between 1 and the lastID
            friendID = random.randint(1, self.lastID)
            # if the return of add friendship of userID and friendID is true
            if self.addFriendship(userID, friendID):
                # increment total friendships
                totalFriendships += 2
            # otherwise
            else:
                # increment collisions
                collisions += 1
        # print collision
        print(f"COLLISIONS: {collisions}")

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
        for i in range(0, numUsers):
            self.addUser(f"User {i}")

        # Add users
        
        # Create friendships
        possibleFriendships = []
        
        for userID in self.users:
            for friendID in range(userID +1,self.lastID + 1):
            #why not for friendID in range(0, self.lastID + 1):
            # if friendID == userID:
            #because starting from zero it means thats the zeroth user is already friends with the 1th user and automatically when you do addfriendship 1th will become friend with the zeroth
            #this is for two way connections but in the case of following like in twitter, i think your solution can work
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)
        #dividing by 2 because each friendship adds 2 frienships
        # if its for one directional we wont be dividing by 2
        for i in range(0,math.floor(numUsers * avgFriendships / 2)):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {} 
        # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()

        q.enqueue([userID])

        while q.size() > 0:
            path = q.dequeue()
            newUserID = path[-1]

            if newUserID not in visited:
                # set the new user ids path in visited
                visited[newUserID] = path
                # loop over each friend id in the friendships at the index of new user id
                for friendID in self.friendships[newUserID]:
                    # check that the friend id is not in visited
                    if friendID not in visited:
                        # create a copy of the path
                        new_path = list(path)
                        # append the friend id to the copy of the path
                        new_path.append(friendID)
                        # enqueue the copy of the path
                        q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraphLinear(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

# if __name__ == '__main__':
#     sg = SocialGraph()
#     start_time = time.time()
#     numUsers = 2000
#     avgFriendships = 190
#     # sg.populateGraph(numUsers, avgFriendships)
    
#     sg.populateGraphLinear(numUsers, avgFriendships)
#     end_time = time.time()
#     print(f"Linear runtime: {end_time - start_time} seconds")

#     start_time = time.time()
#     sg.populateGraph(numUsers, avgFriendships)
#     end_time = time.time()
#     print(f"Quadratic runtime: {end_time - start_time} seconds")
