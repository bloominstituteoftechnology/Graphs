import random


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

        # Add users
        for i in range(num_users):
            # generates "test_user1", "test_user2", "test_user3"
            self.add_user(f"test_user{i}")

            # Create friendships
        potential_friendships = []
        for user_id in self.users:
            # start with friend after user_id, end with last_id
            for friend_id in range(user_id + 1, self.last_id + 1):
                potential_friendships.append((user_id, friend_id))

        random.shuffle(potential_friendships)  # shuffle up friendships!

        for i in range(0, (num_users * avg_friendships) // 2):
            friendship = potential_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        stack = Stack()

        def get_neighbors(node_id):
            return self.friendships[node_id]

        stack.push(user_id)  # put user_id at top of stack

        while stack.size() > 0:
            user = stack.pop()  # take top user off of stack
            if user not in visited:  # if we have not visited node
                visited[user] = set()  # initialize node in dictionary
                # assign new key a value of empty set

                # for each neighbor next to user
                for neighbor in get_neighbors(user):
                    # add neighbor to the stack
                    stack.push(neighbor)
                    # and add said neighbor to the visited dict
                    visited[user].add(neighbor)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
