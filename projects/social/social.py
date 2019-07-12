import random

class User:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self)
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

        Creates that number of users and randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # O(n)
        for userID in range(numUsers):
            self.addUser(f"User {userID+1}")
        print(self.users)

        # Create friendships
        # O(n^2)) looping thru nested array
        possible_friendships = [] #it becomes an array of objects
        for userID in range(1, self.lastID + 1): #for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1): #why we do +1? user 1 will always be plus 1 , and you can't be friends with user 1 / recurssive problem
                possible_friendships.append( (userID, friendID) )

        # O(n)
        random.shuffle(possible_friendships)

        # O(?)/ slice: take all possible friendships/ fisseyetes
        #we are trying to create certain kind of possible friendships
        friendships_to_create = numUsers * avgFriendships // 2
        for friendship in possible_friendships[:friendships_to_create]:
            self.addFriendship(friendship[0], friendship[1])


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
          # Note that this is a dictionary, not a set
        # Why using set ? not dictionary // BFT traversal = enqueue the starting node
        visited = {}
        queue.enqueue([userID])
        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visited:
                visited[verted] = path
                for neighbor in self.frienships[vertex]:
                    path_copy = path.copy() #list(path)
                    path_copy.append(neighbor)
                    queue.enqueu(path_copy)
        return visited
    


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
