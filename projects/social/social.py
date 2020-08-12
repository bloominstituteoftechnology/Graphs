import random

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.get_size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def get_size(self):
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

    def get_neighbors(self, friend_id):
        return self.friendships[friend_id]

    def populate_graph(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

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

        # Add users (vertices)
        for i in range(0, num_users):
            self.add_user(i)


        # Create friendships (edges)do this first
        # generate all possible friendship combinations
        possible_friendships = []

        #avoid duplicates by ensuring first num < second num
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # create a pair of user/friend (connected components)
                possible_friendships.append((user_id, friend_id))

        # shuffle friendships
        random.shuffle(possible_friendships)

        # create friendships from the first N pairs of the list
        # N -> num_users * avg_friendships // 2 (// or floor division prevents floats)
        N = num_users * avg_friendships // 2
        for i in range (N):
            friendship = possible_friendships[i]
            user_id, friend_id = friendship 
            self.add_friendship(user_id, friend_id) 
        
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
        q.enqueue([user_id])

        while len(q.queue) > 0:
            current = q.dequeue()
            vertex = current[-1]
            if vertex not in visited:
                visited[vertex] = current
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(current + [neighbor])




        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
