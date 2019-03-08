from random import randint
from queue import *


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        self.times_addFriendship_called = 0

    def addFriendship(self, userID, friendID):
        self.times_addFriendship_called += 1
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

        # Make sure avg friendships is less then number of users
        if not numUsers > avgFriendships:
            avgFriendships = numUsers - 1

        # Add users
        for num in range(1, numUsers + 1):
            self.addUser(num)

        # Create friendships
        total_friendships = (numUsers * avgFriendships) // 2
        friendships = []

        while len(friendships) < total_friendships:
            # generat possiblity
            possibility = sorted([randint(1, numUsers), randint(1, numUsers)])
            # discard if user is friends with self
            if possibility[0] == possibility[1]:
                continue
            # discard if friendship already exists
            if possibility in friendships:
                continue
            # otherwise add to friendships
            friendships.append(possibility)

        # add friendships to network
        for friendship in friendships:
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
        queue = Queue()
        queue.put([userID])

        while not queue.empty():
            current_path = queue.get()
            current = current_path[-1]
            if current not in visited:
                visited[current] = current_path
                # queue up new paths
                for item in self.friendships[current]:
                    if item not in visited:
                        queue.put(list(current_path) + [item])

        return visited

    def return_avg_num_of_friends(self):
        num_friendships = 0
        for person in self.friendships.keys():
            num_friendships += len(self.friendships[person])
        return num_friendships / len(self.friendships)

    def return_avg_separation(self):
        total_connections = 0
        total_paths = 0
        total_path_length = 0

        for person in self.friendships.keys():
            social_paths = self.getAllSocialPaths(person)
            print(social_paths)
            num_friends = len(social_paths)
            total_connections += num_friends

            for path in social_paths:
                total_paths += 1
                total_path_length += len(social_paths[path]) - 1
                print(social_paths[path])

        print(
            f'Average extended network size: {total_connections/len(self.friendships.keys())}')
        print(
            f'Average degrees of separation: {total_path_length/total_paths}')


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    # print(sg.times_addFriendship_called)
    # print(sg.return_avg_num_of_friends())
    connections = sg.getAllSocialPaths(1)
    # print(connections)
    sg.return_avg_separation()
