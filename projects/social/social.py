import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """Creates a bi-directional friendship"""
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """Create a new user with a sequential integer ID"""
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """Takes a number of users and an average number of friendships as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships. """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"User {i}")
        # Create friendships
        # Generate all possible friendship combinations
        possible_friendships = [] # [(friend_id_1, friend_id-2)]
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.lastID+1):
                possible_friendships.append( (user_id, friend_id) )
        # randomize the above array
        print(f'possible_friendships before random>>>>{possible_friendships}')
        random.shuffle(possible_friendships)       
        print(f'possible_friendships after random>>>>>{possible_friendships}') 

        # pick out num_users * avg_friendships number of friend combos from possible_friendships
        for i in range(numUsers * avgFriendships //2):
            friendship = possible_friendships[i]
            self.addFriendship(friendship[0], friendship[1])



    def getAllSocialPaths(self, userID):
        """Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path."""
        queue = [ [userID]]
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        while len(queue) > 0:
            # check if queue still have vertices to visit
            path = queue.pop(0)
            current_vertex = path[-1]
            # have we seen this vertex before?
            if current_vertex not in visited:
                # Add the vertex to the visited set
                visited[current_vertex] = path
                # find the neighbors and add them to the queue
                for neighbor in self.friendships[current_vertex]:
                    # copy the path list
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    queue.append(path_copy)



        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(5, 2)
    print(f"Social Graph Friendships>>>>>>{sg.friendships}")
    connections = sg.getAllSocialPaths(1)
    print(f"All social connections(paths)>>>>>>>>{connections}")
