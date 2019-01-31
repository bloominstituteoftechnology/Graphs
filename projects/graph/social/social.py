from itertools import combinations
import random
import time
import sys
sys.path.append('../') 
from src.graph import Queue
# # sys.path.append(f'{os.getcwd()}/graph')
# # from graph import Queue


# use to see function's runtime
start_time = time.time()
# Run function

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
        # !!!! IMPLEMENT ME

        # Random randit way # O(n):
        # Add user
        for i in range(numUsers):
            self.addUser(f'User {i}')
        # Create friendships
        target_friendships = (numUsers * avgFriendships) // 2
        num_created = 0
        num_warnings = 0
        while num_created < target_friendships:
            friendship = (random.randint(1, numUsers), random.randint(1, numUsers))
            if self.addFriendship(friendship[0], friendship[1]):
                num_created += 1
            else:
                num_warnings += 1   
        
        # # Itertools combinations way # O(n choose k) => O(n^2):
        # # runtime: less than 0.00 seconds
        # # Add users
        # for i in range(numUsers):
        #     self.addUser({f'User {i}'}) 
        # # Create friendships
        # possible_friendships = list(combinations(range(1, numUsers+1), avgFriendships))
        # random.shuffle(possible_friendships)
        # total_friendships = (avgFriendships * numUsers)//2
        # actual_friendships = possible_friendships[:total_friendships]
        # for friendship in actual_friendships:
        #     self.addFriendship(friendship[0], friendship[1])

        # # Two for loops way # O(n^2):
        # # runtime: less than 0.0 seconds
        # # Add users
        # for i in range(numUsers):
        #     self.addUser(f"User {i}")
        #  # Create friendships	        
        # possible_friendships = []
        # for i in range(1, numUsers + 1):
        #     for j in range(1, numUsers + 1):
        #         if i != j and ((i, j) and (j, i)) not in possible_friendships:
        #             possible_friendships.append((i, j))
        # random.shuffle(possible_friendships)
        # total = int((avgFriendships * numUsers) / 2)
        # actual_friendships = possible_friendships[:total]
        # for friends in actual_friendships:
        #     self.addFriendship(friends[0], friends[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # create queue
        q = Queue()
        # enqueue starting vertex
        q.enqueue([userID])
        # while queue is not empty
        while q.size() > 0:
            # path is the first duplicate path from the queue
            path = q.dequeue()
            # new_userID is the last index from the path
            new_userID = path[-1]
            if new_userID not in visited:
                visited[new_userID] = path
            # enqueue all of its friendID that have not been visited
            for friendID in self.friendships[new_userID]:
                if friendID not in visited:
                    # creates duplicate list
                    duplicate_path = list(path)
                    # adds child(ren) to duplicate path
                    duplicate_path.append(friendID)
                    # add duplicate list to queue
                    q.enqueue(duplicate_path)
        return visited

        


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

end_time = time.time()
print(f'runtime: {end_time - start_time} seconds')

# totals = {}
# total_friendships = 0
# for key in sg.friendships:
#     totals[key] = len(sg.friendships[key])
#     total_friendships += totals[key]

# # Hint for Stretch:
# connections = {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}

# total = 0
# for user in connections:
#     length += len(connections[user]) - 1
#     if length >= 0:
#         total += length
# total/len(connections)