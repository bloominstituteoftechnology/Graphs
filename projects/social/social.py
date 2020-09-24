import random
from collections import deque
import copy

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id        = 0
        self.users          = {}
        self.friendships    = {}
        self.visited        = {}      # visited nodes (via traversal)
        self.friend_iters   = 0
        self.friend_colls   = 0

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        # Tally how many times this method is called
        self.friend_iters = self.friend_iters + 1 

        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False   # Dan: added this line
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            # Tally how many times there was a friend collision (friendship that already existed)
            self.friend_colls = self.friend_colls + 1 
            return False   # Dan: added this line
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True    # Dan: added this line

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

        # working variables
        total_friendships = num_users * avg_friendships

        # generate users
        for usr in range(1, num_users+1):
            self.add_user(f'User: {usr}')

        # randomly generate friendships
        ctr = 1 
        while ctr < total_friendships:
            per1 = random.randint(1, num_users)
            per2 = random.randint(1, num_users)

            # exception: same person, try again
            if per1 == per2:
                continue

            # generate a friendship between per1 and per2
            if self.add_friendship(per1, per2):
                # success
                ctr = ctr + 1

    # bft traverses the graph in a breadth first manner
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Reset the visited object
        self.visited = {}

        # Validate the passed parameter: is the passed vertex valid?
        if starting_vertex not in self.users:
            # vertex not found, nothing to do
            print("vertex {vtx} not found, nothing to do".format(vtx=starting_vertex))
            return False

        # Define a vertex search queue - "vertexes to traverse"
        vert_queue = deque()
        # Define a vertex status map - "status of the vertex's traversal"
        vert_status = {}

        # Set the initial status for each vertex as "not_started"
        for vtx in self.users:
            vert_status[vtx] = "search_not_started"

        # Start the breadth search with the passed vertex
        vert_status[starting_vertex]  = "search_started"
        # Construct the path from starting_vertex -> starting_vertex
        #    which is: [starting_vertex]
        self.visited[starting_vertex] = list([starting_vertex])
        # Place the start vertex in our queue
        vert_queue.append(starting_vertex)

        # Process while there are vertices in the queue
        while len(vert_queue) != 0:
            # Dequeue the vertex at the top of the queue
            tmp_vtx = vert_queue.pop()
            vert_status[tmp_vtx] = "search_started"

            # Iterate through the current vertex's neighbors
            #    and initate the search process on those vertices
            for vrtx in self.friendships[tmp_vtx]:
                if vert_status[vrtx] == "search_not_started":
                    vert_status[vrtx] = "search_started"

                    # Construct the path from starting_vertex to vrtx which is:
                    #   1. path from starting_vertex to tmp_vtx 
                    #   2. + vrtx
                    self.visited[vrtx] = copy.deepcopy(self.visited[tmp_vtx]) # Step 1
                    self.visited[vrtx].append(vrtx)                           # Step 2

                    # Add the current vertex to the queue to be inspected
                    vert_queue.append(vrtx)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Traverse the graph starting with passed user id
        self.bft(user_id)
        # Return the generated visited graph
        return self.visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(100, 10)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    print(sg.friend_iters)
    print(sg.friend_colls)
