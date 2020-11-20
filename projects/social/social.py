import random
import math
from collections import deque

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []

        # Create friendships
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the entire array of possible friendships
        random.shuffle(possible_friendships)

        # Select the first num_users * avg_friendships / 2
        # We / 2 because a friendship is a bidirectional edge (we're essentially adding two edges)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = deque()
        queue.append([user_id])

        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1]
            visited[currNode] = currPath
            for friend in self.friendships[currNode]:
                if friend not in visited:
                    newPath = currPath.copy()
                    newPath.append(friend)
                    queue.append(newPath)

        return visited

    # Returns True if user_id and friend_id have successfully been added ad friends
    def add_friendship_linear(self, user_id, friend_id):
        if user_id == friend_id:
            return False
        # Check if friend_id and user_id are not already friends with each other
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def populate_graph_linear(self, num_users, avg_friendships):
        # Return graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users into the graph
        for i in range(num_users):
            self.add_users(f"User {i}")

        # Create random friendships until we've hit target number of friendships
        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            # keep adding friendships
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship_linear(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
            print(f"Collisions: {collisions}")


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(8, 4)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

"""
Questions:
    1. 
"""
