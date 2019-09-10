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

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        self.queue = Queue()

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

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
        all_friendships = avgFriendships * numUsers
        fs_combo = []
        # !!!! IMPLEMENT ME

        # Add users
        created = 0
        collisions = 0
        for user in range(numUsers):
            self.addUser(user)
        # use random.randint(1, numUsers)
        while created < all_friendships:
            first_friend = random.randint(1, numUsers)
            second_friend = random.randint(1, numUsers)
            attempt = self.addFriendship(first_friend, second_friend)
            if attempt == True:
                created += 1
            else: collisions += 1
        # for userID in self.users:
        #     for friendID in range(userID + 1, self.lastID + 1):
        #         if userID != friendID:
        #             fs_combo.append((userID, friendID))
        # print(fs_combo)
        # random.shuffle(fs_combo)
        # to_make = int(all_friendships / 2)
        # print('to make:', to_make)
        # made_friends = fs_combo[0:to_make]
        # Create friendships
            # make combinations
            # shuffle combinations
            # take n friendships
            # avgFriendships = totalFriendships/numUsers
        # for fs in made_friends:
        #     first_friend = fs[0]
        #     second_friend = fs[1]
        #     self.addFriendship(first_friend, second_friend)
    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # self.friendships[userID]
        visited = {}  # Note that this is a dictionary, not a set
        queue = self.queue
        vert = [userID]
        queue.enqueue(vert)
        while queue.size():
            vert = queue.dequeue()
            node = vert[-1]
            if node not in visited:
                visited[node] = vert
                for friend in self.friendships[node]:
                    path_copy = vert[:]
                    path_copy.append(friend)
                    queue.enqueue(path_copy)
        # !!!! IMPLEMENT ME
        self.queue = Queue()
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(100, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
