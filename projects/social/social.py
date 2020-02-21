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
            return False

        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
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
            self.add_user(f"User {i + 1}")
        # Create friendships
        # Create list to hold all possible friendship combos
        possible_friendships = []
        for user_id in self.users:  # Gives you primary id of all users
            # user_id+1 ensures you only add friends w/ id bigger than user's
            # last_id+1 ensures you include every id
            for friend_id in range(user_id + 1, self.last_id + 1):  
                # Append tuple to possible_friendships list
                possible_friendships.append((user_id, friend_id))
        # print('unshuffled poss friendships', possible_friendships)
        # shuffle list
        random.shuffle(possible_friendships)
        # print('shuffled poss_friendships', possible_friendships)
        # Grab first N elements from list
        # num_times_to_call_add_friend = avg_friend * num_users/2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
    def populate_graph_linear(self, num_users, avg_friendships):

        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for user in range(num_users):
            self.add_user(user)

        target_friendships = num_users * avg_friendships
        friendships_successfully_added = 0
        failures = 0

        while friendships_successfully_added < target_friendships:
            user_id =  random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)

            add_friendship = self.add_friendship(user_id, friend_id)
        
            if add_friendship:
                friendships_successfully_added += 2
            else:
                failures += 1

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            friend = path[-1]
            # print(path, 'path)

            if friend not in visited:
                visited[friend] = path
                # print(visited, 'visited')
                # print(self.friendships[friend], 'friend')
                for neighbor in self.friendships[friend]:
                    # print(neighbor)
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # print(path_copy, 'copy')
                    # print(path_copy, 'path copy')
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
