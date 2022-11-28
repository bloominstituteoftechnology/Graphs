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
        self.friendships = {} # {1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {1}}

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

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # Generate all the possible friendships and put them into an array
        # 3 users (0, 1, 2)
        # [(0, 1), (0, 2), (1, 2)]
        possible_friendships = []
        for user_id in self.users:
            # To prevent duplicate friendship, create from user_id + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the friendship array
        # [(1, 2), (0, 1), (0, 2)]
        random.shuffle(possible_friendships)

        # Take the first num_users * avg_friendships / 2 and that will be the friendships for that graph
        for i in range(math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def populate_graph_linear(self, num_users, avg_friendships):
        # Keep randomly making friendships until we've made the right amount
        # Randomly select two vertices to become friends
        # if it's a success, then increment number of friendships made
        # else try again
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(0, num_users):
            self.add_user(f"User {i}")
        
        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship_linear(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        print(f"collisions: {collisions}")

    def add_friendship_linear(self, user_id, friend_id):
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = deque()
        queue.append([user_id])
        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1]
            visited[currNode] = currPath
            for friend in self.friendships[currNode]:
                if friend not in visited:
                    new_path = list(currPath)
                    new_path.append(friend)
                    queue.append(new_path)
        return visited

    def count_direct_friends(self, friend_id):
        if friend_id not in self.friendships:
            print(f"WARNING: No user exists with friend_id: {friend_id}")
            return -1
        return len(self.friendships[friend_id])
    
    def count_extended_network(self, friend_id):
        if friend_id not in self.friendships:
            print(f"WARNING: No user exists with friend_id: {friend_id}")
            return -1
        return len(self.get_all_social_paths(friend_id))

    def percent_of_total_users_in_extended_network(self, friend_id):
        if friend_id not in self.friendships:
            print(f"WARNING: No user exists with friend_id: {friend_id}")
            return -1
        return (self.count_extended_network(friend_id) / len(self.users)) * 100
    
    def avg_degree_of_separation_in_extended_network(self, friend_id):
        if friend_id not in self.friendships:
            print(f"WARNING: No user exists with friend_id: {friend_id}")
            return -1
        degrees_of_separation = []
        extended_network = self.get_all_social_paths
        degrees_of_separation = [len(p) for p in self.get_all_social_paths(friend_id).values()]
        return sum(degrees_of_separation) / len(degrees_of_separation)

    def print_stats(self):
        direct_friends_count_list = []
        extended_network_count_list = []
        avg_degree_of_separation_in_extended_network_list = []

        for friend_id in self.users.keys():
            direct_friends_count_list.append(self.count_direct_friends(friend_id))
            extended_network_count_list.append(self.count_extended_network(friend_id))
            avg_degree_of_separation_in_extended_network_list.append(self.avg_degree_of_separation_in_extended_network(friend_id))

        total_avg_direct_friends = self.average(direct_friends_count_list)
        total_avg_extended_network = self.average(extended_network_count_list)
        total_avg_percent_of_total_users_in_extended_network = (total_avg_extended_network / len(self.users)) * 100
        total_avg_degree_of_separation_in_extended_network = self.average(avg_degree_of_separation_in_extended_network_list)
        
        print(f"""
        Total number of users in social network: {len(self.users)}
        Average number of friends per user: {total_avg_direct_friends}
        Average size of a user's extended network: {total_avg_extended_network}
        Percentage of total users in a user's extended network: {total_avg_percent_of_total_users_in_extended_network}%
        Average degrees of separation in a user's extended network: {total_avg_degree_of_separation_in_extended_network}
        """)
    
    def average(self, list_of_values):
        return sum(list_of_values) / len(list_of_values)

if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(1000, 5)
    sg.populate_graph_linear(1000, 5)
    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)
    sg.print_stats()
