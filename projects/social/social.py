import random
from util import Queue, Stack
import copy

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
            j = i+1
            user_text = "User " + str(j)
            self.add_user(user_text)

        # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))


        # Shuffle the list
        random.shuffle(possible_friendships)
        # print("----")
        # print(possible_friendships)
        # print("----")
        # Grab the first N pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        # N = avg_friendships * num_users // 2


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        #traversal then search
        q = Queue()

        # Add the starting vertex_id to the queue
        q.enqueue(user_id)

        # While the queue is not empty:
        while q.size() > 0:

            # Dequeue the first vertex
            dq = q.dequeue()

            # Check it its been visited
            if dq not in visited:
                # If it has not mark it as a friend in a key of visited
                visited[dq] = [user_id]

                # Then add all neighbors to the queue
                for v in self.friendships[dq]:
                    q.enqueue(v)

        # we want the shortest path, so we'll do BFS

        # find path to each friend
        for key in visited:
            # Initialize a stack
            s = Stack()
            destination_vertex = key

            #Add path to starting vertex to the stack
            s.push( visited[key] )
            # create empty set 
            visited2 = set()

            # while stack not empty
            while s.size() > 0:
                # pop the first path
                path = s.pop()
                # get last vertex from path
                v = path[-1]
                # see if it's the destination
                if v==destination_vertex:
                    # if so, return the path
                    visited[key] = path
                    break
                # if it hasn't been visited
                if v not in visited2:
                    # mark it as visited
                    visited2.add(v)
                    # and push a path to all neighbors to the stack 
                    for neighbor in self.friendships[v]:
                        path_copy = path[:] # why was .copy() not working?
                        path_copy.append(neighbor)
                        s.push(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.users)
    print(sg.friendships)
    print("---" * 10)
    sg.get_all_social_paths(1)
    connections = sg.get_all_social_paths(1)
    print(connections)