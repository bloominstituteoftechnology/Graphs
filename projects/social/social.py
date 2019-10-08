import random
from util import Queue
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
        for user in range(numUsers):
            self.addUser(user)

        friendship_combinations = []
        for userID in range(numUsers - 1):
            for friendID in range(userID + 1,  self.lastID + 1):
                if userID != friendID:
                friendship_combinations.append((userID, friendID))


        # Add users
        random.shuffle(friendship_combinations)
        totalFriendships = avgFriendships * numUsers
        friends_to_make = friendship_combinations[:totalFriendships / 2]

        for friendship in friends_to_make:
            first_friend = friendship[0]
            second_friend = friendship[1]
            self.addFriendship(first_friend, second_friend)
        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        

        # bfs for searching


        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()

        path = [userID]
        q.enqueue(path)

        while q.size():
            path = q.dequeue()
            node = path[-1]
            if node not in visited:
                visited[node] = path
                for friend in self.friendships[node]:
                    path_copy = path[:]
                    path_copy.append(friend)
                    q.enqueue(path_copy)
                    # copy the path
                    # add the firned to the path
                    # put the path to the fridn in the queue

        # self.friendships[userID]

        return visited

    # def populateGraphLinear(self, numUsers, avgFriendships):
    #     self.lastID
    #     self.users
    #     self.friendships = {}

    #     for user in range(numUsers):
    #         self.addUser(user)


    #     totalFriendships = avgFriendships * numUsers
    #     friendships_created = 0
    #     while friendships_created < totalFriendships:
    #         first_friend = random.randint(0, numUsers)
    #         second_friend = random.randint(0, numUsers)
    #         maybe_friendship = self.addFriendship(first_friend, second_friend)
    #         if maybe_friendship = true:
                
    
    #     friendships_created += 1

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
