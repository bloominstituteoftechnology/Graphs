
import random
from util import Queue

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
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create Frienships
        # Generate all possible friendship combinations
        possible_friendships = []

        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the possible friendships
        random.shuffle(possible_friendships)

        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id, social_graph):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # do this in two sets. 
            # Find all of friends in the network, add them to dict
            # then find the shortest path to each one.   
         
        # Create an empty queue and enqueue the starting user ID
        q = Queue()
        q.enqueue(user_id)

        # Create a dict to store {visited vertices: [shortest_path]}
        visited = {}
        
        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            node = q.dequeue()

            # If that vertex has not been visited....
            if node not in visited:
                # Add to the visited dictionary, which will end up being our return
                visited[node] = None

                # Then add all of its neighbors to the back of the queue
                for next_vert in social_graph[node]:
                    q.enqueue(next_vert)
        
        # The first part, where we add all of the friends as the key values in the dict is complete
        # Now we need to add the shortest_path as the value on each dict entry

        # i is the destination node and user_id is the starting_node
        for destination_node in visited:

            q = Queue()
            # push the user_id into the queue as a list
            q.enqueue([user_id])

            while q.size() > 0:
                # get the first path from the queue
                path = q.dequeue()
                # get the last node from the path
                node = path[-1]
                # as soon as we find the first instance of the destination_node
                if node == destination_node:
                    visited[destination_node] = path
                    break
                # enumerate all adjacent nodes, construct a new path and push it into
                # the queue
                for adjacent in social_graph[node]:
                    new_path = list(path)
                    new_path.append(adjacent)
                    q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('Social Network:')
    print(sg.friendships)
    connections = sg.get_all_social_paths(1, sg.friendships)
    print('--------------------')
    print('Connections:')
    print(connections)