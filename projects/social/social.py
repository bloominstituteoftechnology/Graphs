import random
from utils import Queue


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


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
        # create a list  all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        # shuffle the list
        random.shuffle(possible_friendships)
        # print("----")
        # print(possible_friendships)
        # print("----")
        # Grab the fist N frinship pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # avg_friendships = total_friendships /num_user
        # total_frindships = avg_frindships * num_users
        # N = avg_frienships * num_users // 2

    def get_connections(self, user_id):
        '''
        Takes the user_id and returns the list of their friends 
        '''
        return self.friendships[user_id]

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME
        # use BFS to search the shortest connection between friendships

        # create an empty queue
        q = Queue()
        # add a path to the starting user_id to the queue
        q.enqueue([user_id])
        # create an empty visited dict to store visited node
        visited = {}  # Note that this is a dictionary, not a set
        # While the queue is not empty ....
        while q.size() > 0:
            # dequeue, the fist path
            v = q.dequeue()
            # grab the last connection from the path
            last = v[-1]
            # check if its been visited
            # if it has not been visited ...
            if last not in visited:
                # mark it as visited
                visited[last] = v
                # then add a path to all neigbors to the back of the queue
                # (make a copy before adding )
                for i in self.get_connections(last):
                    copy = v + [i]
                    q.enqueue(copy)

        return f'visited {visited}'


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
