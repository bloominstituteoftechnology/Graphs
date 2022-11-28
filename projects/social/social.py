import random
from itertools import combinations
from collections import deque


# Note: This Queue class is sub-optimal. Why?
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
        self.last_id = 0      # current number of users
        self.users = {}       # your users with their attributes
        self.friendships = {} # adjacency list

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

    def fisher_yates_shuffle(self, l):
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

        # Add users
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        # if 1 is a friend of 2, and 2 is a friend of 1, count this as 2 friendships
        total_friendships = avg_friendships * num_users
        
        # create a list with all possible friendship combinations, 
        # friendship_combos = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        friendship_combos = []

        for user_id in range(1, num_users + 1):
        # You can avoid this by only creating friendships where user1 < user2
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_combos.append((user_id, friend_id))

        # shuffle the list, 
        self.fisher_yates_shuffle(friendship_combos)
        # then grab the first N elements from the list
        friendships_to_make = friendship_combos[:(total_friendships // 2)]

        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])
        
    def populate_graph_linear(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # add users
        for user in range(num_users):
            self.add_user(user)
        # create friendships
        # if 1 is a friend of 2, and 2 is a friend of 1, 
        total_friendships = avg_friendships * num_users
        friendships_made = 0
        # do this until we have as many as we want
        while friendships_made < total_friendships:
        # choose two random user ids
            first_user = random.randint(1, num_users + 1)
            second_user = random.randint(1, num_users + 1)
        # try to make the friendship
            new_friendship = self.add_friendship(first_user, second_user)
            if new_friendship:
                friendships_made += 2

    def get_friends(self, current_friend):
        return self.friendships[current_friend]


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        Choose your fighter: BFT
        """
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # create a queue
        q.enqueue([user_id])
        while q.size() > 0:
            # get the next person in line
            current_path = q.dequeue()
            current_person = current_path[-1]
            # check if we've visited them yet
            if current_person not in visited:
            ## if not, mark as visited
                # key: user_id, value: path
                visited[current_person] = current_path
                ## get their friends (visited their edges)
                friends = self.get_friends(current_person)
            ## enqueue them
                for friend in friends:
                    friend_path = list(current_path)
                    # friend_path = [*current_path]
                    friend_path.append(friend)
                    q.enqueue(friend_path)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)


""" 
Questions Section:
Question 1: To create 100 users with an average of 10 friends each, 
how many times would you need to call add_friendship()? Why?

Answer 1: 500 times, because each time you call add_friendship() it 
creates a friendship for two keys, as it's bidirectional and thus creates 
two edges.

Question 2: If you create 1000 users with an average of 5 random friends 
each, what percentage of other users will be in a particular user's extended 
social network? What is the average degree of separation between a user 
and those in his/her extended network?

Answer 2: About 99.5%. There is more room for error in this percentage with
a smaller sample size like 10, where connections tend to vary between 8-10.
"""
