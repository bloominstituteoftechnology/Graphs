import random
from itertools import combinations
from util import Stack, Queue  # These may come in handy
# Implemented by Ben Hakes

def rSubset(arr, r): 
  
    # return list of all subsets of length r 
    # to deal with duplicate subsets use  
    # set(list(combinations(arr, r))) 
    return list(combinations(arr, r))

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for index in range(0, numUsers):
            self.addUser(f'User-{index}')
        
        # Create friendships
        list_to_shuffle = rSubset([n for n in range(1,numUsers + 1)],2)
        # shuffle the list
        random.shuffle(list_to_shuffle)
        # shorten the list
        shuffled_list = list_to_shuffle[:int(numUsers * avgFriendships/2)]

        count = 0
        for pair in shuffled_list:
            count += 1
            self.addFriendship(pair[0], pair[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        for user in self.users:
            if userID == user:
                continue
            result = self.bfs(userID, user)
            if result == None:
                continue
            visited[user] = result 

        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print(f'Trying to get from {starting_vertex} to {destination_vertex}.')
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first PATH
            path = queue.dequeue()
            # Grab the last vertex from the PATH
            user = path[-1]
            # If that node/vertex has not been visited...
            if user not in visited:
                # CHECK IF IT'S THE TARGET
                if user == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...    
                visited.add(user)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_node in self.friendships[user]:
                    # COPY THE PATH
                    # new_path = list(path)
                    new_path = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path.append(next_node)
                    queue.enqueue(new_path)

        return None

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
