from itertools import combinations
import random
# --------------- NOTES from instructions / instructors ------------

'''The functionality behind creating users and friendships has been 
completed already via functions below : addFriendship + addUser'''

""" POPULATION GRAPH FUNCTION 
_ Takes a number of users and an average number of friendships as arguments

_ Creates that number of users and a randomly distributed friendships between those users.

_ The number of users must be greater than the average number of friendships. """

""" GET ALL SOCIAL PATHS FUNCTION
_Takes a user's userID as an argument

_Returns a dictionary containing every user in that user's extended network 
with the shortest friendship path between them.

_The key is the friend's ID and the value is the path."""

# - Lambda -  <----- denotes which comments are provided by Lambda staff

# ------------------------------- END of NOTES ---------------------------

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
        Creates a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()



    def populateGraph(self, numUsers, avgFriendships):
        # a feature that creates large numbers of users to the network and assigns them a random distribution of friends.
        # - Lambda - Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # - Lambda - !!!! IMPLEMENT ME

        # - Lambda - Add users
        # use addUsers function here
        for i in range(10):
            self.addUser(f"user {i}")

        # - Lambda - Create friendships
        # use addFriendships function here
        possible_friendships = list(combinations(range(1, numUsers + 1), 2))
        random.shuffle(possible_friendships)
        actual_friendships = possible_friendships[:15]

        for friendship in actual_friendships:
            self.addFriendship(friendships[0], friendships[1])
        
        # HINT for STRETCH #2 --- (random.randint(1,10), random.randint(1,10))

    def getAllSocialPaths(self, userID):
        # BFS for shortest path
        # - Lambda - shows all the friends in a user's extended social network and chain of friendships that link them
       
        visited = {}  # - Lambda - Note that this is a dictionary, not a set
        # - Lambda -  !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
