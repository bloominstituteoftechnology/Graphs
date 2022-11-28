from random import shuffle
from math import ceil, floor
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
        if num_users < avg_friendships:
            return
        for i in range(1, num_users + 1):
            self.add_user(f'User_{i}')
        # Add users
        def rand_friends(arr, num_users, avg_friends, res, prev_i):
            if len(arr) == avg_friends:
                if arr[0] != arr[1]:
                    res.append(list(arr))
                return
            for i in range(prev_i+1 , num_users + 1):
                arr.append(i)
                rand_friends(arr, num_users, avg_friends, res, i)
                arr.pop()
            return res
        res = rand_friends([], num_users, avg_friendships, [], 0)
        shuffle(res)
        for user, friend in res[:num_users]:
            self.add_friendship(user, friend)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = deque()
        q.append([user_id])
        while q:
            curr_path = q.popleft()
            curr_node = curr_path[-1]
            if curr_node in visited:
                continue
            visited[curr_node] = list(curr_path)
            for friend in self.friendships[curr_node]:
                new_path = list(curr_path)
                new_path.append(friend)
                q.append(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
