import random


class Queue:
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
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

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
        # # Add users
        for i in range(num_users):
            self.add_user(f'User {i + 1}')
        # # Create friendships
        # possible_friendships = []
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))
        #
        # random.shuffle(possible_friendships)
        #
        # print(possible_friendships)
        #
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])
        target_friendships = (num_users * avg_friendships)
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            # Create a random friendship
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print(f'COLLISIONS: {collisions}')

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # DO BFT and store the paths along the way

        # Create an empty queue
        queue = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        # Add a path to the starting node to the queue
        queue.enqueue([user_id])
        # While the queue is not empty:
        while queue.size() > 0:
            # Dequeue the first path from the queue
            path = queue.dequeue()
            curr_friend = path[-1]
            # Check if it's been visited
            if curr_friend not in visited:
                # if not, mark it as visited
                visited[curr_friend] = path
                # When an unvisited node is found, add the path the to visited dictionary
            # Add a path th each neighbor to the end of the queue
                for friend_id in self.friendships[curr_friend]:
                    path_copy = path.copy()
                    path_copy.append(friend_id)
                    queue.enqueue(path_copy)
        # Return visited dictionary
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(500, 2)
    print('-----Users-----')
    print(sg.users)
    print('-----Friendships-----')
    print(sg.friendships)
    print('----Social Paths------')
    connections = sg.get_all_social_paths(1)
    print(connections)

    connection_lens = [len(v) for v in connections.values()]

    print('Lengths of all Social Paths')
    print(connection_lens)
    print('Average Lengths of Social Paths')
    print(sum(connection_lens) // len(connection_lens))
