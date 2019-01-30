import random
from collections import deque


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
        elif (friendID in self.friendships[userID] or
              userID in self.friendships[friendID]):
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

        The number of users must be greater than the
        average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i}")
        # create list of every possible friendship
        possible_friendships = []
        # a range of all user ids from 1 to 10
        for i in range(1, self.lastID + 1):
            for j in range(1, self.lastID + 1):
                if i < j and i != j:
                    possible_friendships.append((i, j))

        # shuffle all possible friendships
        random.shuffle(possible_friendships)
        # slice off
        sliced = round((numUsers * avgFriendships) / 2)
        sliced_friendships = possible_friendships[:sliced]
        # Create friendships
        for friendship in sliced_friendships:
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        if self.friendships[userID]:
            for i in range(1, self.lastID + 1):
                visited[i] = self.bfs(userID, i)

            return visited
        else:
            return 'No friends'

    # Breadth First Search
    def bfs(self, starting_vert, target_vert):
        queue = deque()
        visited = set()
        queue.append([starting_vert])
        while queue:
            # -> dequeue a list from queue
            dequeued_list = queue.popleft()
            path_end = dequeued_list[-1]
            # -> mark it as visited
            if path_end not in visited:
                # check if target vert == last item in list
                if path_end == target_vert:
                    return dequeued_list
                visited.add(path_end)
                # -> enqueue all of it's children
                for vert in self.friendships[path_end]:
                    path_copy = list(dequeued_list)
                    path_copy.append(vert)
                    queue.append(path_copy)


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
