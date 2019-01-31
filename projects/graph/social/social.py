from itertools import combinations
import random
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
            self.addUser(f"User {i}")

        # Create friendships
        possible_friendships = list(combinations(range(1, len(self.users)+1), 2))
        random.shuffle(possible_friendships)
        number_connections = numUsers * avgFriendships // 2
        actual_friendships = possible_friendships[:number_connections]
#        print(actual_friendships)

        for friendship in actual_friendships:
            sg.addFriendship(friendship[0], friendship[1])
            
#        print(sg.friendships)

    
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        
        if userID not in self.friendships:
            return None
        
        visited = {}  # Note that this is a dictionary, not a set
        
        queue = Queue()
        
        queue.enqueue([userID])
        
        while queue.len() > 0:    # .len() is a method in Queue class
            path = queue.dequeue()
            node = path[-1] # last node in path
            
            if node not in visited:
#                print(node)
                visited[node] = path
                
                for next_node in self.friendships[node]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    
                    queue.enqueue(new_path)
                    
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)





#all_friendships = [(1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)]

#sg = SocialGraph()
#for i in range(10):
#    sg.addUser(f"User {i}")
#
#possible_friendships = list(combinations(range(1, len(sg.users)+1), 2))
#random.shuffle(possible_friendships)
#actual_friendships = possible_friendships[:15]
#print(actual_friendships)
#
#for friendship in actual_friendships:
#    sg.addFriendship(friendship[0], friendship[1])
#    
#print(sg.friendships)



#print(list(combinations([1, 2, 3, 4, 5], 2)))



# Stretch
# using sampling
#(random.randint(1,10), random.randint(1,10))
# 10 users, want each user to have an average of 9 friendships