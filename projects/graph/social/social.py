from itertools import combinations
from collections import deque
import random
# --------------- NOTES from instructions / instructors ------------

'''The functionality behind creating users and friendships has been 
completed already via functions below : addFriendship + addUser'''

""" POPULATION GRAPH FUNCTION 
_ Takes a number of users and an average number of friendships as arguments

_ Creates that number of users and a randomly distributed friendships between those users.

_ The number of users must be greater than the average number of friendships. """

""" GET ALL SOCIAL PATHS FUNCTION
_Takes a user's userID as an argument

_Returns a dictionary containing every user in that user's extended network 
with the shortest friendship path between them.

_The key is the friend's ID and the value is the path."""

# - Lambda -  <----- denotes which comments are provided by Lambda staff

# ------------------------------- END of NOTES ---------------------------

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
        Creates a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()



    def populateGraph(self, numUsers, avgFriendships):
        # a feature that creates large numbers of users to the network and assigns them a random distribution of friends.
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # use addUsers function here
        for i in range(numUsers):
            self.addUser(f"user {i}")

        # use addFriendships function here
        possible_friendships = list(combinations(range(1, numUsers + 1), 2))
        random.shuffle(possible_friendships)
        num_friendships = (numUsers * avgFriendships) // 2
        actual_friendships = possible_friendships[:num_friendships]

        for friendship in actual_friendships:
            self.addFriendship(friendship[0], friendship[1])
        
        # HINT for STRETCH #2 --- (random.randint(1,10), random.randint(1,10))

    def getAllSocialPaths(self, userID):
        # Function calls bfs_search on each user to output the shortest path between the
        # the userID and all other connected users. Each 'friend' serves as the target for 
        # bfs function. 

        visited = {}  

        for friend in self.users:
            visited[friend] = self.bfs_search(userID,friend)
        
        return visited
        # solution based off of "Connected Components Algorithm" 
        
    def bfs_search(self, starting_v, target_v):
        #finds shortest path between a starting point and end point in a graph 
        #the syntax is: mydict[key] = "value"
        # _The key is the friend's ID and the value is the path."""
        q = deque()
        visited = {}
        q.append(starting_v)
     
        while len(q) > 0:
            path = q.popleft()
            current_v = path

            if current_v not in visited:
                visited["path"]=current_v
                if current_v == target_v:
                    #print(visited)
                    return path 
               #enqueue all of it's children that have not been visited 
                for friend in self.friendships[current_v]:
                    q.append(friend)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
