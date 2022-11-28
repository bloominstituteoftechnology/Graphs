import random
from collections import deque
class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'User({repr(self.name)})'
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
        for i in range(num_users):
            self.add_user(f'{i}')
        # Create friendships
        possible_friendships = []
        for user in self.users:
            for friend in range(user + 1, self.last_id + 1):
                possible_friendships.append((user, friend))

        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
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
        visited[user_id] = [user_id]
        for friend_id in self.friendships[user_id]:
            queue.append((friend_id, [friend_id]))

        while len(queue) > 0:
            current_node = queue.popleft()
            current_friend_id = current_node[0]
            current_path = current_node[1]
            if current_friend_id not in visited:
                visited[current_friend_id] = current_path
                for new_friend_id in self.friendships[current_friend_id]:
                    if new_friend_id not in visited:
                        new_path = list(current_path) + [new_friend_id]
                        queue.append((new_friend_id, new_path))
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    print(sg.users)
    connections = sg.get_all_social_paths(1)
    print(connections)
