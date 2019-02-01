from queue import Queue

import random
from itertools import combinations


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
            # print("WARNING: You cannot be friends with yourself")
            return False
        elif (
            friendID in self.friendships[userID] or userID in self.friendships[friendID]
        ):
            # print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

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
            self.addUser(f"User {i}")

        # Create friendships
        # possible_friendships = list(combinations(range(1, numUsers + 1), 2))
        # # random.seed(1)
        # random.shuffle(possible_friendships)
        # numFriendships = (numUsers * avgFriendships) // 2
        # actual_friendships = possible_friendships[:numFriendships]

        # for friendships in actual_friendships:
        #     self.addFriendship(friendships[0], friendships[1])

        # Run in O(n) time
        target_friendships = (numUsers * avgFriendships) // 2
        num_created = 0
        while num_created < target_friendships:
            friendship = (random.randint(1, numUsers), random.randint(1, numUsers))
            if self.addFriendship(friendship[0], friendship[1]):
                num_created += 1

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for user in self.users:
            visited[user] = self.bf_search(userID, user)
        return visited

    def bf_search(self, starting_vertex, target_vertex):
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = []

        while queue.len() > 0:
            path = queue.dequeue()
            current_vertex = path[-1]

            if current_vertex not in visited:
                visited.append(current_vertex)
                if current_vertex == target_vertex:
                    return path

                for child_vertex in self.friendships[current_vertex]:
                    dup_path = list(path)
                    dup_path.append(child_vertex)
                    queue.enqueue(dup_path)

        return None


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    # print(connections)
    total = 0
    for user in connections:
        if connections[user]:
            length = len(connections[user]) - 1
        if length >= 0:
            total += length
    avg_deg = total / len(connections)
    print(avg_deg)

