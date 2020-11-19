import random
import queue

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

        for i in range(0, numUsers):
            self.addUser(i)

        total_friendships = numUsers * avgFriendships
        call_add_friendships = total_friendships // 2

        user_ids = range(1, numUsers + 1)

        friends = []
        for user in user_ids:
            for i in range(user + 1, numUsers + 1):
                friends.append((user, i))

        # print("friends",friends)
        random.shuffle(friends)

        # print("shuffle_friends", friends)
        friends_to_make = friends[:call_add_friendships]

        for f in friends_to_make:
            self.addFriendship(f[0], f[1])


        # Create friendships

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """

        q = queue.Queue()
        visited = {}  # Note that this is a dictionary, not a set
        q.put([userID])
        # !!!! IMPLEMENT ME

        while not q.empty():
            current_path = q.get()
            user_or_friend = current_path[-1]

            if user_or_friend not in visited:
                visited[user_or_friend] = current_path

                edges = self.friendships[user_or_friend]

                for e in edges:
                    path_copy = current_path[:]
                    path_copy.append(e)
                    q.put(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
