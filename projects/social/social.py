from collections import deque
import random 
import math 


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
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        # Generate all possible friendships possible
        for user_id in self.users:
            # To avoid duplicating friendships, create friendships from user_id + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the entire array of possible friendships
        random.shuffle(possible_friendships)

        # Select the first num_users * avg_friendships / 2
        # We / 2 because a friendship is a bidirectional edge (we're essentially adding two edges)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # A dictionary mapping from nodeID -> [path from user_id]
        queue = deque()
        queue.append([user_id])

        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1]
            visited[currNode] = currPath
            for friend in self.friendships[currNode]:
                if friend not in visited:
                    newPath = currPath.copy()
                    newPath.append(friend)
                    queue.append(newPath)

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
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
