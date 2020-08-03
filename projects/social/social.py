import random
import time

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
        for user in range(num_users):
            self.add_user(user)
            # starts at 1, up to and including num_users
        
        total_friendships = num_users * avg_friendships
        friendships_made = 0
    # until we've made the total friendships we want
        while friendships_made < total_friendships:
    # choose two user ids at random
            user = random.randint(1, self.last_id)
            friend = random.randint(1, self.last_id)
    # try to make them friends
            was_friendship_made = self.add_friendship(user, friend)
    # if that succeeds, increment a friendship counter
            if was_friendship_made:
                friendships_made += 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        q.enqueue([user_id])
​
        while q.size() > 0:
​
            current_path = q.dequeue()
            current_node = current_path[-1]
​
            if current_node not in visited:
                visited[current_node] = current_path
​
                friends = self.friendships[current_node]
​
                for friend in friends:
                    friend_path = current_path.copy()
                    friend_path.append(friend)
​
                    q.enqueue(friend_path)
​
​

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
