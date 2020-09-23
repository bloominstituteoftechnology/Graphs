import random
from collections import deque

ORCNAME = ['Sugbu', 'Yambul', 'Zalthu', 'Snaglak', 'Noogugh', 'Varbu',\
'Podagog', 'Cukgilug', 'Xarpug', 'Jughragh', 'Murbol', 'Bashuk', 'Ugor', 'Mog',\
'Ghak', 'Murob', 'Ulumpha', 'Ushug', 'Sharn', 'Dura', 'Raghat', 'Brokil', \
'Pargu', 'Hibub', 'Jughog', 'Nurghed', 'Ditgurat', 'Durz', 'Kurdan', 'Bugdul']

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
        combos = []

        # Add users
        for _ in range(num_users):
            self.add_user(ORCNAME[random.randint(0, len(ORCNAME) - 1)])
        
        # Create all friendships
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id +1):
                combos.append((user_id, friend_id))

        # shuffle all possible friendships
        random.shuffle(combos)

        for i in range(int(num_users * avg_friendships // 2)):
            friendship = combos[i]
            self.add_friendship(friendship[0], friendship[1])



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = deque()
        queue.append((user_id, [user_id])) # List is a path to that user_id
        while len(queue) > 0:
            curr_vertex, curr_path = queue.popleft()
            if curr_vertex not in visited:
                visited[curr_vertex] = curr_path
                for friend_id in self.friendships[curr_vertex]:
                    new_path = curr_path.copy()
                    new_path.append(friend_id)
                    queue.append((friend_id, new_path))

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
