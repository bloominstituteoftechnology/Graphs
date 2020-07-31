import random
import time

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
        Will create an UNDIRECTED graph
        Makes TWO friendships
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
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(num_users):
            self.add_user(user)
            # starts at 1, up to and including num_users
       
        # Hint 1: to create N random friendships, can create a list with all possible friendship combinations of user ids
        
        friendship_combos = []
        # Time complexity is O(n^2)
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                friendship_combos.append((user, friend))
                
        #shuffle the list
        self.fisher_yates_shuffle(friendship_combos)
        
        #get the first N elements from the list
        total_friendships = num_users * avg_friendships
        friends_to_make = friendship_combos[:(total_friendships // 2)]
        
        # Create friendships
        for friendship in friends_to_make:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        qq = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        
        qq.enqueue([user_id])
        
        while qq.size() > 0:
            current_path = qq.dequeue()
            current_node = current_path[-1]
            
            if current_node not in visited:
                visited[current_node] = current_path
                
                friends = self.friendships[current_node]
                
                for friend in friends:
                    friend_path = current_path.copy()
                    friend_path.append(friend)
                    
                    qq.enqueue(friend_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

# #percentahe of users in this user's extended social networ
print(len(connections)/ 1000 * 100)

# #average degree of seperation
# total = 0
# for path in connections.values():
#     total = len(path)
    
# average = total/connections