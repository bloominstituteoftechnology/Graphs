from util import Queue
import random

class User:
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     return self.__init__()

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
            self.add_user(f'User {i+1}')
        # Create friendships
        target_friendships = avg_friendships * num_users
        total_friendship = 0
        collisions = 0

        while total_friendship < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            if self.add_friendship((user_id, friend_id)):
                total_friendship += 2
            else:
                collisions += 1
        print(f'collisions: {collisions}')

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                self.friendships.append((user_id, friend_id))

        random.shuffle(self.friendships)

        print(self.friendships)



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # create the queue
        q = Queue()
        # enqueue a path to the starting user
        q.enqueue([user_id])
        # create a dict to store the visited user
        visited = {}  # Note that this is a dictionary, not a set
        while q.size() > 0:
            path = q.dequeue()
            u = path[-1]
            if u not in visited:
                visited[u] = path
                for friend in self.friendships[u]:
                    path_copy = path.copy()
                    q.enqueue(path_copy.append(friend))
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
