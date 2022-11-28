import random
import math

class Queue():
    def __init__(self):
        self.queue = []

    def __repr__(self):
        return str(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


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

        posible_friendships = []
        
        # Add users

        for i in range(0, num_users):
            self.add_user(f'User {i}')

        for user_id in self.users:     
        # Create friendships
            for friend_id in range(user_id + 1, self.last_id + 1):
                posible_friendships.append((user_id, friend_id))
        
        random.shuffle(posible_friendships)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = posible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        # crawl using a queue 
        queue = Queue()
        # start with the staring id in the queue 
        queue.enqueue([user_id])
        # keep track of what friends and friends of friends we visited
        visited = dict()
        while queue.size() > 0:
            current_path = queue.dequeue()
            # print(f'Current path: {current_path}')
            # pop off the last element in queue and declare that the path
            current_user_id = current_path[-1]
            if current_user_id not in visited:
                # mark current user visited key is current user and value is path
                # we use a dictionary to store the key of the user_id we are searching and the value is the path of how we get to that friend
                visited[current_user_id] = current_path
                for friend in self.friendships[current_user_id]:
                    newPath = list(current_path)
                    newPath.append(friend)
                    queue.enqueue(newPath) 
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
