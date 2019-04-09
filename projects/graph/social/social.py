import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() > 0:
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)


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

        if numUsers < avgFriendships:
            print("WARNING: The number of users must be greater than the average number of friendships")
            return

        # Add users
        for _ in range(0, numUsers):
            self.addUser(self.lastID)

        # Create friendships
        numFriendShips = int((numUsers * avgFriendships) / 2)
        possibleFriendships = []

        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        random.shuffle(possibleFriendships)

        for i in range(numFriendShips):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def bfs(self, root, searching):
        # Queue is an array of paths
        q = Queue()
        visited = []
        q.enqueue([root])

        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]

            if node not in visited:
                neighbors = self.friendships[node]
                for neighbor in neighbors:
                    nextPath = list(path)
                    nextPath.append(neighbor)
                    q.enqueue(nextPath)
                    if neighbor == searching:
                        return nextPath
                visited.append(node)
        return None


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # {friendID: path, friendID: path}

        for friendShip in self.friendships[userID]:
            path = self.bfs(userID, friendShip)
            visited[friendShip] = path


        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(100, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(3)
    print(connections)



