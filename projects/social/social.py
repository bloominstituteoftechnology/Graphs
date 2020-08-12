import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"User({repr(self.name)})"

class SocialGraph:
    def __init__(self):
        self.reset()

    def add_friendship(self, user_id, friend_id): # add an edge
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

    def add_user(self, name): # add a node
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def reset(self):
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}") 

        # Create friendships
        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        for i in range(num_users * avg_friendships // 2):
            friendships = possible_friendships[i]
            self.add_friendship(friendships[0], friendships[1])        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # locate all friends of a user (includes friends of friends, get whole network) starting from the user:
            # find all immediate friends of the user
            # for each friend, find all friends of the friend
            # repeat until all friends traversed
            # if friend of friend already in visited, ignore
        # log the shortest path from the user to a friend

        print(f"User {user_id}: {self.friendships[user_id]}")
        print("\n")

        # initialize queue with user_id using a BFS
        q = Queue()
        q.enqueue([user_id])
        visited = {}

        while q.size() > 0:
            link = q.dequeue()

            # get the last user from the friendship
            u = link[-1]

            if u not in visited.keys():
                # create a dictionary entry for each friend of user_id
                # store the path to that friend as the value
                visited[u] = link

                # for all friends of the current user:
                for friend in self.friendships[u]:
                    # create a path to that user
                    link2 = link.copy()
                    # add the friend of the current user to the friendship path
                    link2.append(friend)
                    # add to the queue
                    q.enqueue(link2)

        # finding the degrees of separation
        degrees = 0 # counter
        for i in visited.values():
            degrees += len(i)
        # calculate the average degrees of separation
        total_degrees = round(degrees / len(visited.keys()), 2)
        print("Average Degrees of Separation:", total_degrees)
        print("\n")

        # calculate the number of connections in the extended social network
        print("Number of Connections:", len(visited.keys()))
        print("\n")

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("Friendships:", sg.friendships)
    print("\n")
    connections = sg.get_all_social_paths(1)
    print("Connections:", connections)
