import sys
sys.path.append("../graph")
from graph import Graph
import random 


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
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
        # !!!! IMPLEMENT ME
        # add users
        #generate all friend combinations
        # avoid duplicates by making sure num1 < num2
        
        # create friendships 

        for i in range(0, num_users):
            self.add_user(f'Fred {i+1}')
        possible_friends=[]
        for user_id in self.users:
            for friend_id in range(user_id +1 , self.last_id +1):
                 possible_friends.append((user_id, friend_id))
        # shuffle the list and get N from the list 

        random.shuffle(possible_friends)
        # create for X pairs (tatal // 2)
        for i in range(num_users*avg_friendships //2):
            friendship =possible_friends[i]
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
        for friend_id in self.users:
            connection = self.bfs(user_id, friend_id)
            if connection:
                visited[friend_id] = connection
        return visited
# Note: This Queue class is sub-optimal. Why?


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create a queue
        q = Queue()
        # enqueue the path to starting vertex
        q.enqueue([starting_vertex])
        # set for visited
        visited = set()
        # as long as not empty dequeue the first path
        while q.size() > 0:
            path = q.dequeue()
            if path[-1] not in visited:
                visited.add(path[-1])
                if path[-1] == destination_vertex:
                    return path
                for n in self.friendships[path[-1]]:
                    new_path = list(path)
                    new_path.append(n)
                    q.enqueue(new_path)
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
