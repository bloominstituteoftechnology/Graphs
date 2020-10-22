from collections import deque
import random
import math 


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {} # {1: User("1"), 2: User("2"), ...}
        self.friendships = {} # {1: {2, 3, 4}, 2: {1}, 2:{1}, 4:{1}}

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
        self.users[self.last_id] = User(name) # {1: User("mari")}
        self.friendships[self.last_id] = set() # {1: {}}

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
            self.add_user(f"User{i}")

        # Create friendships
        #Generate all poss. friendships and put into array
        # 3 users (0 1 2)
        #[(0,1), (0,2), (1,2)]
        possible_friendships = []
        for user_id in self.users:
            #prevent duplicate friendhips, create from user_id + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))


        # Shuffle friends array
        #[(1,2), (0,1), (0,2)]
        random.shuffle(possible_friendships)

        #Take first num_users * avg_friendhips / 2 and that will be friendships for the graph
        for i in range(math.floor(num_users * avg_friendships / 2)):
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
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
