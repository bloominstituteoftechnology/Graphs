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
        # !!!! IMPLEMENT ME

        if numUsers < avgFriendships:
            print("WARNING: Number of users must be less than the average number of friendships.")
        else:
            # Add users
            for i in range(0, numUsers):
                self.addUser(i)

            # Create friendships
            possibles = []

            # Loop through users
            for user in self.users:
                # to avoid repeats (1,2) and (2,1), start with user +1 each time through (cant friend yourself)
                for friend in range(user + 1, self.lastID + 1):
                    possibles.append((user, friend))

            # Shuffle the list of possible connections
            random.shuffle(possibles)
            
            for i in range(0, (numUsers * avgFriendships // 2)):
                addFriend = possibles[i]
                self.addFriendship(addFriend[0], addFriend[1])



    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Use BFS
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
                    
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
