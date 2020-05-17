import random
from queue import SimpleQueue

class User:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name
    
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
        elif friend_id in self.friendships[user_id] or \
             user_id in self.friendships[friend_id]:
                 print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # automatically increment the ID to assign the new user
        self.last_id += 1
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments.

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of
        friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        with open('first-names.txt') as file:
            names = file.read().split()
        
        for i in range(num_users):
            self.add_user(random.choice(names))

        # Create friendships
        for i in range(num_users * avg_friendships // 2):
            successful = False
            while not successful:
                user1 = random.choice(list(self.users.keys()))
                user2 = random.choice(list(self.users.keys()))
                if user1 != user2:
                    if user2 not in self.friendships[user1] and \
                       user1 not in self.friendships[user2]:
                           self.add_friendship(user1, user2)
                           successful = True

    def get_total_users(self):
        return len(self.users)
                           
    def get_total_friendships(self):
        return sum([len(friend_list) for friend_list in \
                    self.friendships.values()])
                           
    def get_average_friendships(self):
        num_users = self.get_total_users()
        total_friendships = self.get_total_friendships()
        return total_friendships / num_users
    
    def get_min_friendships(self):
        return min([len(friend_list) for friend_list in \
                    self.friendships.values()])
            
    def get_max_friendships(self):
        return max([len(friend_list) for friend_list in \
                    self.friendships.values()])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument.

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        
        to_visit = SimpleQueue()
        to_visit.put((user_id, None))
        
        while to_visit.qsize() > 0:
            (vertex, prev) = to_visit.get()
            
            if vertex not in visited:
                if vertex == user_id:
                    visited[vertex] = [user_id]
                elif prev == user_id:
                    visited[vertex] = [user_id]
                else:
                    visited[vertex] = visited[prev] + [prev]
                        
            for edge in self.friendships[vertex]:
                if edge not in visited:
                    to_visit.put((edge, vertex))
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.users)
    print(sg.friendships)
    print(f'Total Users: {sg.get_total_users()}')
    print(f'Total friendships: {sg.get_total_friendships()}')
    print(f'Average friendships per user: {sg.get_average_friendships()}')
    print(f'Minimum friendships: {sg.get_min_friendships()}')
    print(f'Maximum friendships: {sg.get_max_friendships()}')
    connections = sg.get_all_social_paths(1)
    print(connections)
