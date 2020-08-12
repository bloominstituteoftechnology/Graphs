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
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, num_users):
            self.add_user(f'User {i}')

        # Create friendships
        # generate all possible friendship combinations
        possible_friendships = []

        # avoid duplicates by ensuring first number less than 2nd
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # shuffle friendships (using random)
        random.shuffle(possible_friendships)

        # create friendships for the first N pairs of the list
        # N -> num_users * avg_friendships // 2
        N = num_users * avg_friendships // 2
        for i in range(N):
            friendship = possible_friendships[i]
            # user_id, friend_id = friendship
            user_id = friendship[0]
            friend_id = friendship[1]
            self.add_friendship(user_id, friend_id)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}    EXAMPLE OUTPUT
        visited = dict()
        q = Queue()
        
        #self.friendships

        my_list = []
        for user in self.users:
            path = self.bfs(user_id, user)
            # my_tuple = (user_id, user, path)
            # my_list.append(my_tuple)
            visited[user] = path

        return visited

    
    # Helper functions   
    def get_neighbors(self, vertex_id):
        return self.friendships[vertex_id]
        
    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        visited = set()

        path = [starting_vertex]
        q.enqueue(path)

        while q.size() > 0:
            current_path = q.dequeue()
            current_node = current_path[-1]

            if current_node == destination_vertex:
                return current_path

            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)

                for neighbor in neighbors:
                    path_copy = current_path[:]
                    path_copy.append(neighbor)

                    q.enqueue(current_path + [neighbor])

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


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('----------------------------------------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------------------------------------')
    print(connections)

"""
QUESTIONS:
1. To create 100 users with an average of 10 friends each, how many times would you need to call `add_friendship()`? Why?
-------------------------------------------------------------------------------------------------------------------------
Take users (100) multiplied by the average number of friends (10). Because friendship is a two way pointing edge...divide this number
by 2 to get a total of 500 add_friendship calls.



2. If you create 1000 users with an average of 5 random friends each,
what percentage of other users will be in a particular user's extended social network?
What is the average degree of separation between a user and those in his/her extended network?
----------------------------------------------------------------------------------------------
test results (average degrees of seperation, no valid path) 
(5.707, 8)
(5.021, 5)
(5.559, 3)
(5.41, 8)

~993/1000 of other users will be in a user's social network (99.3%).
The average degrees of seperation was ~5.5 (This assumes self as 1 degree of seperation, so on average 4.5 people to connect)

"""