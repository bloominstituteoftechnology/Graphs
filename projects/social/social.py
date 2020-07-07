import random
from util import Queue, Stack


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
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
        self.last_id += 1  # automatically increment the ID to assign the new user

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

        # Add users
        for num in range(num_users):
            self.add_user(num)

        # Create friendships
        count_to_create = num_users * avg_friendships // 2
        possible_friendships = []
        i = 0
        while i < num_users:
            j = i + 1
            while j < num_users:
                pair = (i, j)
                possible_friendships.append(pair)
                j += 1
            i += 1
        random.shuffle(possible_friendships)
        for (user_id, friend_id) in possible_friendships[:count_to_create]:
            self.add_friendship(user_id, friend_id)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        paths = {user_id: [user_id]}
        network = self.get_extended_network(user_id)

        for other in network:
            paths[other] = self.get_social_path(user_id, other)

        return paths

    def get_extended_network(self, user_id):
        unvisited = {i for i in range(len(self.users))}
        network = {user_id}

        queue = Queue()
        queue.enqueue(user_id)

        while queue.size() != 0:
            friend_id = queue.dequeue()
            friend_friends = self.friendships[friend_id]

            for fof_id in friend_friends:
                if fof_id in unvisited:
                    unvisited.remove(fof_id)
                    network.add(fof_id)
                    queue.enqueue(fof_id)
        return network

    def get_social_path(self, origin_id, dest_id):
        unvisited = {u for u in range(len(self.users))}
        stack = Stack()
        stack.push([origin_id])

        while stack.size() != 0:
            path = stack.pop()
            id = path[-1]
            if id == dest_id:
                return path

            friends = self.friendships[id]
            for friend in friends:
                if friend in unvisited:
                    unvisited.remove(friend)
                    new_path = path.copy()
                    new_path.append(friend)
                    stack.push(new_path)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
