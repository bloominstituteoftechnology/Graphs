import random
from util import Queue


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
            self.add_user(f"user {i+1}")

        # Create friendships
        # Create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        
        # Shuffle the list
        random.shuffle(possible_friendships)
        # print("----")
        # print(possible_friendships)
        # print("----")
        # Grab the first total friendship pairs from the list and create those friendships
        for i in range(num_users*avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        # N = avg_friendships * num_users // 2 


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """    
        q = Queue()
        q.enqueue([user_id])
        visited={}

        while q.size() > 0:
            path = q.dequeue()
            last = path[-1]
            if last not in visited:
                visited[last] = path
                for friends in self.friendships[last]:
                    new_path = path + [friends]
                    q.enqueue(new_path)
        return visited

    '''
    A noble first attempt
    '''
    def get_all_social_paths_long(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """        
        social = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for user in self.users:
            # Create empty array for paths
            extended_sn = []
            # Create empty queue
            q = Queue()
            # add first user to queue
            q.enqueue([user])
            # create empty visited
            visited = set()
            # While queue is not empty
            while q.size() > 0:
                # dequeue an item
                network = q.dequeue()
                # get the user of the network
                last = network[-1]
                # if the last user matches the target user
                if (last == user_id):
                    # Add to extended_sn list
                    extended_sn.append(network)
                else:
                    # If last user has not be visited
                    if (last not in visited):
                        # add them to visited
                        visited.add(last)
                        # for the friends of the last user
                        for friends in self.friendships[last]:
                            # Add them to the network
                            new_network = network + [friends]
                            # add new network to queue
                            q.enqueue(new_network)
            # Add shortest path to social if it's not empty
            if (len(extended_sn) > 0):
                shortest = extended_sn[0]
                for sn in extended_sn:
                    if (len(sn) < len(shortest)):
                        shortest = sn
                shortest.reverse()
                social[user] = shortest
        return social


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    # print(sg.users)
    # print("FRIENDSHIPS!", sg.friendships)
    connections = sg.get_all_social_paths(1)
    # long_conn = sg.get_all_social_paths_long(1)
    print("CONNECTIONS", connections)
    # print("LONG CONN", long_conn)
    print("Answer to question 2:")
    print("Don't forget to change populate graph.")
    users = 0
    degrees_of_separation = 0
    for i in range(1, 1001):
        if i in connections:
            users += 1
            degrees_of_separation += len(connections[i])
    avg_dos = degrees_of_separation / 100
    percent_users = (users / 1000) * 100
    print("Average degrees of separation", avg_dos)
    print(f'{percent_users} %')
