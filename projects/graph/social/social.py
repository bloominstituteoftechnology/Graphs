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
        return (len(self.queue))

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
            self.addUser(f"User {i+1}")

        # Create friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append( (userID, friendID) )
        random.shuffle(possibleFriendships)
        first=True
        keys=[]
        for friendship in possibleFriendships[:20]:
            print(friendship)
            if first:
                self.friendships[friendship[0]]=[friendship[1]]
                keys.append(friendship[0])
                first=False
            else:
                if friendship[0] not in keys:
                    self.friendships[friendship[0]]=[friendship[1]]
                    keys.append(friendship[0])
                else:
                   self.friendships[friendship[0]].append(friendship[1])
                
    def bfs(self, starting_vertex, search_vertex):
            # Create an empty queue
            q = Queue()
            # Create an empty set of visited vertices
            visited = set()
            # Put the starting vertex in our Queue
            q.enqueue([starting_vertex])
            # While the queue is not empty....
            while q.size() > 0:
                path=q.dequeue()
                # Dequeue the first node from the queue
                v = path[-1]
                # If that node has not been visted...
                if v not in visited:
                    # Mark it as visited
                    visited.add(v)
                    if v == search_vertex:
                        return path
                    # Then, put all of it's children into the queue
                    for neighbor in self.friendships[v]:
                        new_path=list(path)
                        new_path.append(neighbor)
                        q.enqueue(new_path)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        print(f"user ID {userID}")
        visited = {}  # Note that this is a dictionary, not a set
        count=1
        for i in range (1,11):
            visited[i]=self.bfs(userID,i)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
