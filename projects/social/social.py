import random, math
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

    def add_friendship_linear(self, user_id, friend_id):
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

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

        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id +1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_linear(self, num_users, avg_friendships):
        # keep randomly making friendships untill we have made the right amount
        # randomly select 2 vertices to become friends
        # if successful, increment friendships made
        # else try again

        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(0, num_users):
            self.add_user(f"User {i}")

        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship_linear(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print(f"collisions: {collisions}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        queue = deque()
        queue.append([user_id])

        while len(queue) > 0:
            curr_path = queue.popleft()
            curr_node = curr_path[-1]
            visited[curr_node] = curr_path

            for friend in self.friendships[curr_node]:
                if friend not in visited:
                    new_path = curr_path.copy()
                    new_path.append(friend)
                    queue.append(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph_linear(10, 2)
    print("friendships: ", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("connections: ", connections)
