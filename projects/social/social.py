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
        self.reset()

    def reset(self):
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

        # # Reset graph
        self.reset()

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        possible_friendships = []
        # avoid dups by ensuring first num < second num
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # shuffle friendships
        random.shuffle(possible_friendships)
        # create friendships for the 1st n number of pairs
        N = num_users * avg_friendships // 2
        # n determined by the formula  n -> num_users * avg_friendships // 2  //--> reurns a whole number
        for i in range(N):
            friendship = possible_friendships[i]
            user_id, friend_id = friendship
            self.add_friendship(user_id, friend_id)

    # def populate_graph2(self, num_users, avg_friendships):
    #     #reset graph
    #     self.reset()
    #     #Add users
    #     for i in range(num_users):
    #         self.add_user(f"User {i+1}")
    #     #Create friendships
    #     target_friendships = num_users * avg_friendships
    #     total_friendships = 0

    #     while total_friendships < target_friendships:
    #         user_id = random.randint(1, self.last_id)
    #         friend_id = random.randint(1, self.last_id)

    #         if self.add_friendship(user_id, friend_id):
    #             total_friendships += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # BFS--> find shortest path

        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # use BFS to find the shortest path
        q = Queue()
        q.enqueue([user_id])
        while q.size():
            path = q.dequeue()
            u = path[-1]  # grabs last item in path

            if u not in visited:
                visited[u] = path

                for neighbor in self.friendships[u]:
                    path_copy = list(path)
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
"""
>>> sg = SocialGraph()
>>> sg.populate_graph(10, 2)
>>> print(sg.friendships)
{1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
>>> connections = sg.get_all_social_paths(1)
>>> print(connections)
{1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
```
Note that in this sample, Users 3, 4 and 9 are not in User 1's extended social network.
"""
