import random, itertools
from util import Stack, Queue


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

        for i in range(numUsers):
            self.addUser(str(i+1))

        # Create friendships
        connections = int((numUsers * avgFriendships) / 2)
        possible_friendships = list(itertools.combinations(self.users, 2))
        random_connections = random.sample(possible_friendships, connections)

        for i in random_connections:
            self.addFriendship(i[0], i[1])
    
    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                if v == destination_vertex:
                    return path
                else:
                    visited.add(v)
                for next_vert in self.friendships[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
        return None

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        for i in self.users:
            if i != userID and self.bfs(userID, i) != None:
                visited[i] = self.bfs(userID, i)

        return visited

        # add all other users to visited as keys with blank path - CHECK
        # for each key, run BFS between user and key and set key value to path - CHECK
        # if no value for a given key, remove from dict - EDIT: only set key if bfs returned result, less steps & no popping


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # print(sg.friendships)
    # connections = sg.getAllSocialPaths(1)
    print(sg.getAllSocialPaths(1))