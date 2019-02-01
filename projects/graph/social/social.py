import random
import itertools

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

        # Check input
        if int(numUsers) <= int(avgFriendships):
            print('WARNING: Number of users must be greater than average number of friendships.')

        # Add users
        else:
            for i in range(1, numUsers + 1):
                self.addUser(i)

            for user in self.users:
                for i in range(random.randint(1, avgFriendships)):
                    randomFriend = random.randint(1, numUsers)
                    if len(self.friendships[randomFriend]) < avgFriendships:
                        self.addFriendship(user, random.randint(1, numUsers))

            # possibleCombinations = list(itertools.combinations(list(self.users), 2))

            # random.shuffle(possibleCombinations)

            # for i in range(0, numUsers * avgFriendships):
            #     self.addFriendship(possibleCombinations[i][0], possibleCombinations[i][1])


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        
        # Keep track of vertices to be visited
        queue = [userID]

        # Keep track of the paths need to reach vertices
        paths = {userID:[userID]}

        while len(queue) > 0:
            
            # Add all edges of given vertex to queue
            for i in self.friendships[queue[0]]:

                # If vertex has not been visited, cache its path
                if i not in paths:
                    paths[i] = list(paths[queue[0]])
                    paths[i].append(i)
                    queue.append(i)

                    # If vertex matches target, return target
                    # if i == target:
                    #     return paths[i]

            # Remove last item checked
            queue.pop(0)
        
        # Return a message if target was not found
        return paths


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    print('')
    connections = sg.getAllSocialPaths(1)
    print(connections)

