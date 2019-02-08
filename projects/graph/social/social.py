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
       
        # Add users
        for i in range(0, numUsers):
            self.addUser(f'User {i}')
           
        # print(f' Users: {self.users.values}')
        # print(f'Friendships: {self.friendships}')
        
        # random.shuffle(random_friendships)
        # for i in range(0, math.floor(numUsers * avgFriendships / 2)):
        #     random_friendships.append
        # print(random_friendships)

        # average = ()
        # # Create friendships
        totalFriendShips = (numUsers * avgFriendships) // 2

        possible_friendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1): 
                possible_friendships.append((userID, friendID))
        
        random.shuffle(possible_friendships)
        for i in range(0, totalFriendShips):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])
        # for friend in random_friendships:
        #     self.addFriendship(friend[0], friend[1])
        #     print(friend)
        #     # print(friend[0], friend[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()

        queue.enqueue([userID])
        
        while queue.size() > 0:
            path = queue.dequeue()
            new_user = path[-1]
            visited[new_user] = path
            if new_user not in visited:
                for i in self.friendships[new_user]:
                    if i not in visited:
                        new_path = list(path)
                        new_path.append(i)
                        queue.enqueue(new_path)
               
                

        
        
        print(f'Visited: {visited}')
           
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
