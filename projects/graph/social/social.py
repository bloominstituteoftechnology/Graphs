import random

# user class creates user with parameter name


class User:
    def __init__(self, name):
        self.name = name
# evalues string representation of name from the user object

    def __repr__(self):
        return self.name

# social graph class creates a social graph with users as the verticies


class SocialGraph:
    def __init__(self):
        # initialize last id to 0
        self.lastID = 0
        # initialize users to empty dict
        self.users = {}
        # initialize friendships to an empty dict
        self.friendships = {}

    # add friendship method adds friendships to a user, accepts two arguments, userID and friendID, creates a bidirectional edge
    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        # cannot be friends with self
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        # if friendship already, dont do anything
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        # to add friendship connection or bidirectional edge, add friendID to key of userID in friendship dict
        # also add userID to key of friendID in friendship dict
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
    # add user method adds a user to the users dict and auto increments the lastID to assign a new user number

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        # assigns the user object to the users dict's key
        self.users[self.lastID] = User(name)
        # creates an empty set for friendships dict with the key of lastid or username
        self.friendships[self.lastID] = set()

    # populate graph generates a social graph with two arguments, the number of users and average friendships
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
        # for loop that adds users to the graph range numUsers argument
        for i in range(numUsers):
            # add user to graph, which increments lastID and sets users key to username, so key will be user i+1
            self.addUser(f'User {i+1}')
        # Create friendships, possible friendships is initially set to an empty list
        possibleFriendships = []
        # for all keys in self.users
        for userID in self.users:
            # nested for loop for friendID in range userID + 1 to resolve index starting at 0, until self.lastID + 1 to resolve no-inclusive end range
            for friendID in range(userID + 1, self.lastID + 1):
                # append to the possible friendships list the tupple userID and friendID
                possibleFriendships.append((userID, friendID))
        # print(possibleFriendships)
        # use the fisher-yates shuffle, to randomize possibleFriendships,
        random.shuffle(possibleFriendships)
        # print(possibleFriendships)
        print(possibleFriendships[:20])
        # print(len(possibleFriendships))

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


# test where a social graph is created
# then the social graph is populated with 10 users and an average of two friends
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # print(sg.users)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    # print(connections)

# avg = total/count
# 2 = total/10
# 20 = total
# total = avg * num_users

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 10 choose 2
# n! / 2 * (n-2)!
# n! = n * (n-1) * (n-2)!
# n * (n-1) / 2
# O(n^2)
# 10 * (9) / 2

# build friend-based social network.
# users are able to view friends, friend's friend, friends friend's friend, etc
# people connected through any number of connections are considered part of extended social network

# functionality users and friendships completed
# implement function that shows all the friends in a user's extended social netowrk and chain of friendships that link them
# the number of connections between one user and another are called the degrees of separation

# client also interested in how the performace will scale as more users join
# implement feature that creates large numbers of users to the network and assigns random distribution of friends
