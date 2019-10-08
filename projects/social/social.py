from util import Stack, Queue
import random


class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

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

        # Time Complexity: O(numUsers ^ 2)
    # Space Complexity: O(numUsers ^ 2)
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

        # Add users
        # Time Complexity: O(numUsers)
        # Space Complexity: O(numUsers)
        for i in range(numUsers):
            self.addUser(f"User {i + 1}")

        # Create friendships
        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(numUsers ^ 2)
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        # Time Complexity: O(numUsers ^ 2)
        # Space Complexity: O(1)
        random.shuffle(possibleFriendships)
        # print(f"possibleFriendships:{possibleFriendships}")
        # print(f"possibleFriendships:{len(possibleFriendships)}")


        # print(f"avgFriendships:{avgFriendships}")
        # print(f"numUsers:{numUsers}")
        # Time Complexity: O(avgFriendships * numUsers // 2)
        # Space Complexity: O(avgFriendships * numUsers // 2)
        for friendship_index in range(avgFriendships * numUsers // 2):
            # print(f"friendship_index:{friendship_index}")
            friendship = possibleFriendships[friendship_index]
            # print(f"friendship:{friendship}")
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # !!!! IMPLEMENT ME

        # Create an empty Queue
        q = Queue()
        # Create an empty Visited dictionary
        visited = {}  # Note that this is a dictionary, not a set
        # Add A PATH TO the starting vertex to the queue
        q.enqueue( [userID] )
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex of the path
            v = path[-1]
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited (add it to the visited set)
                visited[v] = path
                # Then enqueue PATHS TO each of its neighbors in the queue
                for friend in self.friendships[v]:
                    # print(f"v:{v}")
                    # print(f"friend:{friend}")
                    # print(f"path:{path}")
                    path_copy = path.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    # print(connections)
    summation = 0
    for i in connections:
        summation += len(connections[i])
        print(i, connections[i])
    percentage = (len(connections)/1000)*100
    print(f'Percentage of Seperation for 1000: {percentage}')
    averageDegree = summation/len(connections)
    print(f'Average Degree of Seperation: {averageDegree}')
