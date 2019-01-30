import random
import time


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
        elif friendID in self.friendships[userID] \
                or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # auto increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of
        friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add numUsers users
        for i in range(numUsers):
            self.addUser(f"User {i}")

        possible_friendships = []
        for i in range(1, numUsers + 1):
            for j in range(1, numUsers + 1):
                if i != j and (i, j) not in possible_friendships \
                        and (j, i) not in possible_friendships:
                    possible_friendships.append((i, j))

        # Create friendships
        random.shuffle(possible_friendships)
        total = int((numUsers * avgFriendships) / 2)
        print(total)
        made_friendship = possible_friendships[:total]

        for friends in made_friendship:
            self.addFriendship(friends[0], friends[1])

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


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(5, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)


"""
sg = SocialGraph()
for i in range(numUsers):
    self.addUser(f"User {i}")

possible_combos = list(combonations(range(1, len(sg.users) + 1), 2))
shuffle(possible_combos)
actual_friendships = possible_combos[:15]

for friendship in actual_friendships:
    self.addFriendship(friendship[0], friendship[1])
"""
