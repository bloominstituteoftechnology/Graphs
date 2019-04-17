import random 
from queue import Queue
from itertools import combinations

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
            self.addUser(i)
        # Create friendships
        possible_friendships = list(combinations(range(1, numUsers + 1), 2))
        random.shuffle(possible_friendships)
        friends_set = (numUsers * avgFriendships) // 2
        actual_friendships = possible_friendships[:friends_set]
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
        for user in self.users:
            visited[user] = self.bfs(user, userID)
        return visited

    def bfs(self, starting_node, target_node):
        queue = Queue()
        visited = []
        queue.enqueue([starting_node])
        while queue.len() > 0:
            path = queue.dequeue()
            node = path[-1]
            if node not in visited:
                visited.append(node)
                if node == target_node:
                    return path
                for next_node in self.friendships[node]:
                    duplicate = list(path)
                    duplicate.append(next_node)
                    queue.enqueue(duplicate)
        return None

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)


"""
    1. To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why? 
    
        A: 500 because it's bidirectional



    2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network? 
"""