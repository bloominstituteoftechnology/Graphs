import random
from utils import Queue

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
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        possible_friendships = []
        # create list with possible friendship combinations
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        #Shuffle the list
        random.shuffle(possible_friendships)
        # Grab the first total_friendships pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        # N = avg_friendships * num_users //2
        # avg_friendships = total_friendships / num_users
        #total_friendships = avg_friendships * num_users
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set for each node ur adding a path
        # !!!! IMPLEMENT ME
        q = Queue()
        # Add a Path to the starting vertex_id to the queue
        q.enqueue([user_id])
        #while queue not empty
        while q.size() > 0:
            #Dequeue the first path
            path = q.dequeue()
            # Grab last vertex from path
            new_user = path[-1]
            #check if visited then if not
            if new_user not in visited:
                #mark as visited
                visited[new_user] = path
                # then add A Path to its neighbors to the back of queue
                for neighbor in self.friendships[new_user]:
                    # Copy the path
                    new_path = list(path)
                    # append the neighbor to new path
                    new_path.append(neighbor)
                    # Enqueue the new path to the back of the queue
                    q.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    print("\nSocial Paths:")
    connections = sg.get_all_social_paths(1)
    print(connections)