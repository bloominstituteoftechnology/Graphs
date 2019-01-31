from itertools import combinations
import random 
import time
from queue import Queue

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
        for i in range(numUsers):
            self.addUser(f'User_{i}')
        
        # Create friendships
        possible_friendships = list(combinations(range(1, int(len(self.users) + 1)),2))
        #print(possible_friendships,"\nlength of possible combinations  : ", len(possible_friendships))
        random.shuffle(possible_friendships)
        index = (numUsers * avgFriendships) //2
        #print("index  : ", type(index))
        actual_friendships = possible_friendships[ : index]
        #print("\n\nactual friendships  : ", actual_friendships)
        
        for friendship in actual_friendships:
            self.addFriendship(friendship[0], friendship[1])
        

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        if userID in self.users:
            print("VALID USER.....")
            if self.friendships[userID]:
                print("Have Friends.........")
                print(self.friendships[userID])
                
                for i in range(1, len(self.users) + 1):
                    visited[i] = self.BFS_path(userID, i)
            return visited
        else:
            return 'Invalid User...'

    def BFS_path(self, start, destination):
        if start in self.users and destination in self.users:
            if start == destination:
                return [start]
       
            visited = set()
            queue = Queue()
            queue.enqueue([start])

            while queue.size() > 0:
                path = queue.dequeue()
                vertex = path[-1]

                for edge_vertex in self.friendships[vertex]:
                    if edge_vertex not in visited:
                        visited.add(edge_vertex)
                        new_path = path + [edge_vertex]

                        if edge_vertex is destination:
                            return new_path

                        else:
                            queue.enqueue(new_path)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    start_time = time.time()
    connections = sg.getAllSocialPaths(1)
    end_time = time.time()
    print(connections)
    print(end_time - start_time)