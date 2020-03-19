import random 
from utils import Queue

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
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        possible_friendships = []

        # List with possible friendship combos
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        
        # Shuffle it up baby
        random.shuffle(possible_friendships)

        # Grab the first total friendship pairs from the list and create friendships

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
        visited = {} 
        # Queue 
        q = Queue()
        # Add path to starting vertex 
        q.enqueue([user_id])
        # While queue not empty
        while q.size() > 0:
            # Decrease that sucka 
            path = q.dequeue()
            # Grab last vertex from path
            new_user = path[-1]
            # Check if user visited
            if new_user not in visited:
                # Mark as visited 
                visited[new_user] = path 
                # Add path to it's neighbors
                for neighbor in self.friendships[new_user]:
                    # Copy path
                    new_path = list(path)
                    # Append neightbor to path
                    new_path.append(neighbor)
                    # Enqueue
                    q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
