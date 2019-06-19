import random

class User:
    def __init__(self, name):
        self.name = name

def fisher_yates_shuffle(l):
    for i in range(0, len(l) - 2):
        random_index = random.randint(i, len(l) - 1)
        l[random_index], l[i] = l[i], l[random_index]

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
        # ---------
        # Generate 1 user per number between 1 and numUsers
        for i in range(numUsers):
            self.addUser(self.lastID + 1)
    
        # Create friendships
        # ------------------
        # Create while loop that goes while count < numUsers * avgFriendships
        count = 0
        print((numUsers * avgFriendships) // 2)
        while count < (numUsers * avgFriendships) // 2:
            # add a random friend to a random user, checking first to see if they are already friends or if the user is trying to befriend himself
            friend_key = random.randint(1, numUsers)
            user_key = random.randint(1, numUsers)
            while friend_key == user_key or friend_key in self.friendships[user_key] or  user_key in self.friendships[friend_key]:
                friend_key = random.randint(1, numUsers)

            count += 1
            self.addFriendship(user_key, friend_key)
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        
        
        
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 4)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
