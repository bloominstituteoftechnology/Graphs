from random import shuffle
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        self.non_mutual = []

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
        # write a for loop that calls create user the right amount of times
        for i in range(num_users):
            self.add_user(f"{i + 1}")
        # to create N random firendships
        # create a list woth all possible friendship combonations
        # shuffle the list, then grab the first N elements from the list
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id +1, self.last_id +1):
                possible_friendships.append((user_id,friend_id))
        
        shuffle(possible_friendships)

        # Create N friendships where N = avg_friendships * num_users // 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0],friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        direct_friends = self.friendships[user_id]
        print(f"\nImmediate Friends {direct_friends}")

        if len(direct_friends) == 0:
            print(f"User {user_id} has no friends :(")
            return {}

        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            # grab the first path
            path = q.dequeue()
            # get the last node in the path
            v = path[-1]
            if v not in visited:
                # add the path to at the id
                visited[v] = path
                
                for friend in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)




        for user in self.users:
            if user not in visited:
                self.non_mutual.append(user)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    
    connections = sg.get_all_social_paths(1)
    print(connections)
    print(f"These users have no mutual friend {sg.non_mutual}")
