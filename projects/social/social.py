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
        #create an empty queue
        q = Queue()
        #create a visited set to keep track
        visited_set = set()
        #create a dictionary to store path
        path = {}
        #get the values/friendships stored with each user
        all_friendships = self.friendships[userID]
        print(f'{all_friendships}')
        #userID is the starting vertex
        #friendship vertex is the target
        #enqueue a path that starts at the starting node into the q
        q.enqueue([userID])
        #while the queue is not empty...
        while q.size() > 0:
            for each_friendship in self.friendship[userID]:
                #add the friendship to our path dictionary
                visited.update({each_friendship:[]})
                print(visited)
                #dequeue the first path from the array
                path = q.dequeue()
                #grab the last vertex of the path
                v = path[-1]
                #check if v is the target
                if v == each_friendship:
                    
                    #if v is the target And the length of the path is less than the one currently in the dictionary:
                    if len(path) < len(visited[each_friendship]):
                        #update the path in the dictionary
                        visited.update(each_friendship = path)
                #check if in visited
                if v not in visited_set:
                    #add the vertex to Visited
                    visited_set.add(v)
                    #Then enqueue each path to each of its neighbors in the q
                    path_copy = path.copy()
                    path_copy.append(v)
                    q.enqueue(path_copy)
                    print(visited_set)
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

        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
