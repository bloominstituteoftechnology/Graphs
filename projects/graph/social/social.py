import itertools
from random import shuffle
from queue import Queue

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
        !! Users start from 1!
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
        for i in range(numUsers):
            self.addUser(i)

        # Add friendships
        possible_friendships = list(itertools.combinations(range(1, numUsers + 1), avgFriendships)) # range(1, numUsers + 1) bc first user added has lastID = 0
        shuffle(possible_friendships)
        friendships_needed = avgFriendships * numUsers
        actual_friendships = possible_friendships[:friendships_needed]

        for friendship in actual_friendships:
            self.addFriendship(friendship[0], friendship[1])

    def bfs(self, user, target_friend):
        paths = Queue()
        paths.enqueue([user]) 
        visited = set() 

        while paths.len() > 0:
            cur_path = paths.dequeue()
            cur_friend = cur_path[-1]
            visited.add(cur_friend)

            if cur_friend is target_friend:
                return cur_path
            else:
                for friend in self.friendships[cur_friend]:
                    if friend is not None:
                        if not friend in visited:
                            new_path = list(cur_path)
                            new_path.append(friend)
                            paths.enqueue(new_path)

        return None


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        all_paths = {4:[1, 3, 4]}
        """
        all_paths = {}  # Note that this is a dictionary, not a set
        
        for friend in self.friendships[userID]:
            path = self.bfs(userID, friend)

            if path is not None:
                all_paths[friend] = path

        return all_paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(f'connections: {connections}')
