import random 
import sys
sys.path.append('../graph')

from util import Stack, Queue

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

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User{i+1}')

        # Create friendships
        #generate all the possible friendship
        possible_friendship = []
        #generate all possible  firend for every single user
        for user_id in self.users:
            for friend_id in range(user_id +1, self.last_id +1):
                possible_friendship.append((user_id, friend_id))
        #randomly select x friendship
        # x= num_users * avg_friendship //2
        #shuffle the array and pick x friendship from the front of it
        random.shuffle(possible_friendship)
        num_friendship =  num_users * avg_friendships //2
        for i in range(0, num_friendship):
            friendship = possible_friendship[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        #do the Bft for shortes path    
        #create a queue
        queue = Queue()
        #create dic for visited vertex and path
        visited = {}  # Note that this is a dictionary, not a set
        #enqueue the queue with the starting user_id as a path
        queue.enqueue([user_id])
        #while queue is not empty
        while queue.size()>0:
            #dequeue the current path
            current_path = queue.dequeue()
            #get the current vertex from end of the path
            current_vertex = current_path[-1]
            if current_vertex not in visited:
                visited[current_vertex] = current_path
                #queue up all the neighbours as path
                for neighbour in self.friendships[current_vertex]:
                    new_path = current_path.copy()
                    new_path.append(neighbour)
                    queue.enqueue(new_path)
            
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
