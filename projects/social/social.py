
import random
from util import Queue
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

        # create a list with all possible friendship combinations
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append( (user_id, friend_id))

        # shuffle the lsit
        random.shuffle(possible_friendships)

        #then grab the first N elements form the list
        # number of times to call add_friendship = avg_friendships * num_users / 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_neighbors(self, vertex):
        return self.friendships[vertex]

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
            p = q.dequeue()
            v = p[-1]
            if v not in visited:
                visited[v] = p
            for i in self.friendships[v]:
                # to prevent infinite loop:
                if i not in visited:
                    new_path = list(p)
                    new_path.append(i)
                    q.enqueue(new_path)

        answer = {}
        for key in sorted(visited.keys()):
            answer[key] = visited[key]
        return answer



if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populate_graph(10, 2)
    sg.populate_graph(1000, 5)
    # print("sg: ", sg)
    # print("sg.friendships: ", sg.friendships)
    print("------")
    # print("sg.users: ", sg.users)
    connections = sg.get_all_social_paths(1)
    print("connections: ", connections)
