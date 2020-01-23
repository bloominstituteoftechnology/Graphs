from random import shuffle
from util import Stack


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

        # Add users
        for num in range(num_users):
            self.add_user(f'user{num}')

        # Create friendships
        for index in self.users:
            users = [u for u in self.users.keys() if u != index]
            shuffle(users)
            friendship = users[:avg_friendships]
            for friend in friendship:
                if friend not in self.friendships[index]:
                    self.add_friendship(index, friend)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        s = Stack()
        for friend in self.friendships[user_id]:
            s.push(friend)
        prev_user = None
        while s.size():
            curr_friend = s.pop()
            if curr_friend not in visited.keys():
                visited[curr_friend] = []
                if curr_friend not in self.friendships[user_id]:
                    for user in visited[prev_user]:
                        visited[curr_friend].append(user)
                visited[curr_friend].append(curr_friend)
                for fof in self.friendships[curr_friend]:
                    s.push(fof)
            else:
                curr = []
                for user in visited[prev_user]:
                    curr.append(user)
                curr.append(curr_friend)
                if len(curr) < len(visited[curr_friend]):
                    visited[curr_friend] = curr
            prev_user = curr_friend

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
