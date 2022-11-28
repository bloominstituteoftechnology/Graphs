import random
from random import randint
import collections

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

#     def populate_graph(self, num_users, avg_friendships):
#         """
#         Takes a number of users and an average number of friendships
#         as arguments
# ​
#         Creates that number of users and a randomly distributed friendships
#         between those users.
# ​
#         The number of users must be greater than the average number of friendships.
#         """
#         # Reset graph
#         self.last_id = 0
#         self.users = {}
#         self.friendships = {}
        
#         # Add users
#         for i in range(num_users):
#             self.add_user(f"User {i}")
        
#         # Create friendships
#         possible_friendships = []
        
#         for user_id in self.users:
#             for friend_id in range(user_id + 1, self.last_id + 1):
#                 possible_friendships.append((user_id, friend_id))

#         # Shuffle the possible friendships
#         random.shuffle(possible_friendships)
        
#         # Add friendships
#         for i in range(num_users * avg_friendships // 2):
#             friendship = possible_friendships[i]
#             self.add_friendship(friendship[0], friendship[1])

    

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
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships

        # The total number of friendships has to be equal to num_users * avg_friendships
        total_friendships = num_users * avg_friendships

        # So for total_friendships times, I am going to add a friendship
        # However, when I add a friendship, it is bidirectional, so that counts as two

        # I could randomly generate a number to get a user id
        # I could then generate another number to pick a friend
        # If that friendship doesn't exist and they are different users, then I can add it
        
        added_friendships = 0

        while added_friendships < total_friendships:
            user_id_1 = randint(1, self.last_id)
            user_id_2 = randint(1, self.last_id)

            if user_id_1 != user_id_2 and user_id_2 not in self.friendships[user_id_1]:
                self.add_friendship(user_id_1, user_id_2)
                added_friendships += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        # Breadth first search since we want to store shortest paths

        path_queue = collections.deque()

        path_queue.append([user_id])

        while len(path_queue) > 0:
            path = path_queue.popleft()
            friend_id = path[-1]

            if friend_id in visited:
                continue
            
            visited[friend_id] = path

            #Enqueue friends
            for id in self.friendships[friend_id]:
                new_path = path.copy()
                new_path.append(id)
                path_queue.append(new_path)

        # Figure out the number of friends / number of total users -1 to get percentage of users connected
        friend_coverage = (len(visited) - 1) / (len(self.users) - 1)
        print(f"Percentage of users that are in extended network: {friend_coverage * 100: 0.1f}%")

        # Figure average of path lengths to get average degrees of separation (subtract one to not count user)
        total_length = 0
        for path in visited.values():
            total_length += len(path) - 1

        if len(visited) > 1:
            avg_separation = total_length / (len(visited) - 1)
            print(f"Average degree of separation: {avg_separation}")
        else:
            print("No friends")

        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10000, 100)
    print(sg.friendships)
    print("\n")
    connections = sg.get_all_social_paths(1)
    # print(connections)
