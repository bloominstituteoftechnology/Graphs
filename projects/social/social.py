from itertools import permutations
from collections import deque
import random

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
        # Create friendships
        for x in range(0,num_users):
            self.add_user(name=x)

        random.seed(0)

        all_possible_combos = list(permutations(self.users, 2))
        random.shuffle(all_possible_combos)

        counter = 0
        friend_counter = 0

        while friend_counter < num_users*avg_friendships:
            pair = all_possible_combos[counter]
            if pair[1] > pair[0]:
                pass
            else:
                self.add_friendship(pair[0], pair[1])
                friend_counter += 2
            counter += 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        q = deque()

        q.append([user_id])
        # While the queue is not empty...
        while len(q) > 0:
            # Dequeue the first PATH
            path = q.pop()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # if the last vertex is not in visited
            # we need to check its neighbors
            if last_vertex not in visited:
                # If the last vertex is the destination, return the path
                visited[last_vertex] = path
                # else, we create new paths with each neighbor
                # of the last vertex and enqueue them to be searched
                for x in self.friendships[last_vertex]:
                    q.appendleft(path + [x])
            elif len(visited[last_vertex]) > len(path):
                visited[last_vertex] = path

        #visited = {key:set(value) for key,value in visited.items()}

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
