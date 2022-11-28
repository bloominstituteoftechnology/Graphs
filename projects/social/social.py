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

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            return False
            # print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            # print("WARNING: Friendship already exists")
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

    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def populate_graph_2(self, num_users, avg_friendships): # THIS METHOD WORKS WELL WITH LOW AVG FRIENSHIPS BUT HIGH USERS.
         # if you have high avg. users there are increased collisions and this algo doesn't work as well.
         # this algo is essentially O(n) with LOW avg. users.

        self.reset()

        # create users
        for user in range(num_users):
            self.add_user(user)
        
        # total frienships needed.
        friendships_needed = num_users * avg_friendships

        total_friendships = 0
        collisions = 0

        while total_friendships < friendships_needed:
            user = random.randint(1, self.last_id)
            friend = random.randint(1, self.last_id)
           
            if self.add_friendship(user, friend):
               total_friendships += 2
            else:
                collisions += 1

        print(collisions)
        

    def populate_graph(self, num_users, avg_friendships):  # O(n^2)
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()

        # create users
        for user in range(num_users):
            self.add_user(user)

    # Hint 1: To create N random friendships, you could create a list with all possible friendship combinations, shuffle the list, then grab the first N elements from the list. You will need to `import random` to get shuffle.
    # Hint 2: `add_friendship(1, 2)` is the same as `add_friendship(2, 1)`. You should avoid calling one after the other since it will do nothing but print a warning. You can avoid this by only creating friendships where user1 < user2.

        # create list for holding possible friendships.
        friendships = []
       
        # Create possible friendships
        # for each user
        for user in range(1, self.last_id + 1):
             # for each friend after the user id up to total users
            for friend in range(user + 1, num_users + 1):
                # create a friendship between user and friend 
                friendship = (user, friend)
                # save the friendship in friendships
                friendships.append(friendship)

        # Determine total number of friendships needed
        friendships_needed = num_users * avg_friendships

        # shuffle our total possible friendships list
        random.shuffle(friendships)

        # put subset of shuffled possible friendships in new shuffled friendships list
        shuffled_friendships = friendships[:friendships_needed//2]   # // integer divide by 2 as frienships are bi directional

        # build our graph from each friend pair in shuffled friendships
        for friendship in shuffled_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()

        # enqueue our starting a node
        path = [starting_vertex]
        q.enqueue(path)

        # make a set to track if we've been at that node before 
        visited = set() 

        # while q is not empty
        while q.size() > 0:

        ## dequeue path at the front of our line
            current_path = q.dequeue()
            current_node = current_path[-1] # last item in list of nodes in our path.

        ### it this is our destination_vertex (or search node), return our current path
            if current_node == destination_vertex:
                return current_path

        ### if we haven't visited this node yet.
            if current_node not in visited:
        ### mark node as visited
                visited.add(current_node)
        ### get the node's neighbors
                neighbors = self.friendships[current_node]
        ### for each of the neighbors
                for neighbor in neighbors:           
        #### add it to queue
                    q.enqueue(current_path + [neighbor])
        
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        SHORTEST PATH = BREADTH FIRST TRAVERSAL

        The key is the friend's ID and the value is the path.
        """
        visited = {}

        # loop through the users in the network.
        for user in self.users:
            # get the shortest path (bfs) between each of those users and the user we're evaluating
            path = self.bfs(user_id, user)
            # if there is a path, populate dictionary with user id as key and path as value
            if path is not None and user_id != user:
                visited[user] = path

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph_2(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

