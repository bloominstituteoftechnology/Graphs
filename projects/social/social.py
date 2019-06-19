import random


class Queue():

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
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
        elif (friendID in self.friendships[userID]
              or userID in self.friendships[friendID]):
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        # automatically increment the ID to assign the new user
        self.lastID += 1
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of
        friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(1, numUsers+1):
            self.addUser(i)

        # Create friendships
        combination_list = []

        # Create combinations to ensure first user ID < second user ID
        for i in range(1, numUsers+1):
            for j in range(i+1, numUsers+1):
                combination_list.append((i, j))

        random.shuffle(combination_list)

        # Here the friendship relation is bi-directional, so divide by 2
        friendship_count = (numUsers*avgFriendships)//2

        for friends in random.sample(combination_list, k=friendship_count):
            self.addFriendship(friends[0], friends[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        # Create an empty queue and add the first node path
        queue = Queue()
        queue.enqueue([userID])

        while queue.size() > 0:

            # Get the path and node
            path = queue.dequeue()
            node = path[-1]

            if node not in visited:
                visited[node] = path

                for next_node in self.friendships[node]:
                    new_path = path.copy()
                    new_path.append(next_node)
                    queue.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(5, 1)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
