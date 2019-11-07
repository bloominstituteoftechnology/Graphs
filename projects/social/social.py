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

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"User {i + 1}")
        # Generate all possible friendship combinations
        possibleFriendships = []
        # Avoid duplicates by ensuring the first number is always smaller than the second number
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        # Shuffle the possible frienships (use Fisher-Yates)
        random.shuffle(possibleFriendships)
        # Create friendships for the first X pairs of the list
        # X = Friendships_needed
        # Friendships_needed = numusers * (avgFriendships // 2)
        # Need to divide by 2 since each addFriendship() creates 2 friendships
        for i in range(numUsers * (avgFriendships // 2)):
            friendships = possibleFriendships[i]
            self.addFriendship(friendships[0], friendships[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME OR SHOOT ME. FINE WITH BOTH
        queue = Queue()
        queue.enqueue([userID])

        while queue.size() > 0:
            path = queue.dequeue()
            friendID = path[-1]

            if friendID not in visited:
                visited[friendID] = path

                for next_friendID in self.friendships[friendID]:
                    new_path = path + [next_friendID]
                    queue.enqueue(new_path)

        return visited

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
