import string
import random
from itertools import combinations
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

    def bfs(self, starting_vertex, target): 
        visited_bfs = []
        queue = deque()
        queue.append([starting_vertex])
        visited = {}
        # avg = 0
        
        while queue:     
            path = queue.popleft()
            last_node = path[-1:][0]
            if last_node not in visited_bfs:
                visited[last_node] = path
                # avg += (len(path) - 1)
                # print(last_node, path)
                if last_node == target:
                    return path
                visited_bfs.append(last_node)
                for v in self.friendships[last_node]:
                    new_list = list(path)
                    new_list.append(v)
                    queue.append(new_list)
        # print('Avg', avg)
        return visited

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
        for i in range(numUsers):
            self.addUser(f'User {i}')        

        # Create friendship pairs  
        # len = friends(friends - 1)/2                              O(n^2)
        possible_friendships = list(combinations(range(1, numUsers+1), 2))

        random.shuffle(possible_friendships)        # O(n)

        T = int(numUsers/2 * avgFriendships) # total friendship needed O(1)

        actual_friendships = possible_friendships[:T]      # O(1)

        # c=0
        for friendship in actual_friendships:               # O(n) 
            # c += 1
            self.addFriendship(friendship[0], friendship[1])
        # print(c, 'C')



        

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # visited = self.bfs(userID, self.users[1])

        return self.bfs(userID, self.users[1])


        # !! When there are 100 users with 10 friends each, addFriendship must be called 500 times. 
        # !! (100 users / 2) * (10 friends / 1 user) => 500 friendships formed
        # !! The 2 is needed since the friendships are bi-directional

        # !! When there are 1000 users with an average of 5 friends:
        # !! 100% of users are in a user's extended social network
        # !! (with such a large number there were no empty sets.)
        # !! On average they are 3.2 degrees of separation from each other. Most are 4 degrees apart with some a little closer.

        # !! Stretch: Instead of creating one average for the numbers of  friends provide different averages for different population groups. 
        # !! Higher average number of contacts for people who are: outgoing, travel frequently, live in larger cities, involved in many social clubs,etc. And a lower average for the inverse.




if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2) # 30/10
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    # print('*' * 10)
    # sg2 = SocialGraph()
    # sg2.populateGraph(100, 10) # >200/100
    # # print(sg2.friendships)
    # connections2 = sg2.getAllSocialPaths(1)
    # print(connections2)
    # print('*' * 10)
    # sg3 = SocialGraph()
    # sg3.populateGraph(1000, 10)
    # # print(sg2.friendships)
    # connections3 = sg3.getAllSocialPaths(1) # >3000/1000
    # print(connections3)