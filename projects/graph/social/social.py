

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
        from itertools import combinations
        import random
        # Add users
        for i in range(numUsers):
            self.addUser(f'User{i}')

        # Create friendships

        allPossibleFrienships = list(combinations(range(1, numUsers+1), 2))
        random.shuffle(allPossibleFrienships)
        total = (numUsers * avgFriendships) / 2
        for i in range(int(total)):
            friends = allPossibleFrienships[i]
            self.addFriendship(friends[0], friends[1])
        
            
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for i in range(1, len(self.users) + 1):
            if len(self.friendships[i]) is not 0:
                visited[i] = self.bft_path(userID, i)  
        total = 0
        for path in visited:
            if len(visited[path]) is not 0:
                total += len(visited[path]) - 1
        print(total)
        return visited


    def bft_path(self, start, target):
        from queue import Queue
        if start in self.friendships:
            nextItems = Queue()
            visited = []
            path = []
            nextItems.put([start])
            while nextItems.empty() is not True:
                first = nextItems.get()
                if first[-1] not in visited:
                    path.append(first[-1])
                    if first[-1] == target:
                        path = first
                        return path
                    visited.append(first[-1])
                    for num in self.friendships[first[-1]]:
                        tempPath = path + [num]
                        nextItems.put(tempPath)
        else:
            return None
    
if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    connections = sg.getAllSocialPaths(1)
    print(connections)
'''
 Questions:
 1. numUsers * avg / 2 = timesCalled
    100 * 10 / 2 = timesCalled
    500 = timesCalled
 2. .5% . The average degree of seperation is around 190, changed depending on how the graph 
 is created.
'''