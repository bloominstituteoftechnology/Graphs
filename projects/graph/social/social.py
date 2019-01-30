from random import shuffle, randint
from itertools import combinations
from queue import Queue


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
            return 0
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return 0
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return 1

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
        if numUsers <= avgFriendships:
            print("WARNING: Number of users must be greater than average friendships")
            return

        # Add users
        for user in range(numUsers):
            self.addUser(user)
        # Create friendships
        # possible_friendships = list(combinations(range(1, numUsers+1), 2))
        # shuffle(possible_friendships)
        # for num in range((numUsers*avgFriendships)//2):
        #     friendship = possible_friendships[num]
        #     self.addFriendship(friendship[0], friendship[1])

        # Refactor for adding friendships stretch
        numFriends = 0
        while numFriends < numUsers*avgFriendships//2:
            friends_added = self.addFriendship(
                randint(1, numUsers), randint(1, 10))
            numFriends += friends_added

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()
        queue.put([userID])
        while not queue.empty():
            path = queue.get()
            node = path[-1]
            if node not in visited:
                visited[node] = path
                for next_friend in self.friendships[node]:
                    queue.put(path + [next_friend])
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    # testing question 2 of part 3 below
    # test = SocialGraph()
    # test.populateGraph(1000, 5)
    # test_connections = test.getAllSocialPaths(1)
    # print(len(test_connections))
    # degree_of_sep = []
    # for key in test_connections:
    #     degree_of_sep.append(len(test_connections[key]))
    # print(sum(degree_of_sep)/len(degree_of_sep))
