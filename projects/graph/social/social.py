from itertools import combinations
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
        
        #Creates a bi-directional friendship
        
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        
        #Create a new user with a sequential integer ID
        
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        
        # Takes a number of users and an average number of friendships
        # as arguments
        # Creates that number of users and a randomly distributed friendships
        # between those users.
        # The number of users must be greater than the average number of friendships.
        
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add numUsers
        for i in range(numUsers):
            self.addUser(f"User: {i}")

        # Create friendships
        #itertools uses nested for loop under hood so this is inefficient at n^2
        possible_friendships = list(combinations(range(1, numUsers+1), 2))
        random.shuffle(possible_friendships)
        total_friendships = (len(possible_friendships) * avgFriendships) // 2  #need len b/c pos friends is a list
        actual_friendships = possible_friendships[:total_friendships]
        for friendship in actual_friendships:
            self.addFriendship(friendship[0], friendship[1])
        #could also practice shuffling with fisher-yates

        #more efficient refactor that is O(n)
        # total_friendships = (possible_friendships * avgFriendships) // 2
        # num_created = 0
        # num_warnings = 0
        # while num_created < total_friendships:
        #     friendship = (random.randint(1, numUsers), random.randint(1, numUsers))
        #     if self.addFriendship(friendship[0], friendship[1]):
        #         num_created += 1
        #     else: 
        #         num_warnings += 1
        # print("linear warning: {num_warnings}")

    def getAllSocialPaths(self, userID):
        # Takes a user's userID as an argument
        # Returns a dictionary containing every user in that user's
        # extended network with the shortest friendship path between them.
        # The key is the friend's ID and the value is the path.
        
        visited = {}  # Note that this is a dictionary, not a set
        if self.friendships[userID]:
            #userID is target, i is starting_vertex
            for i in range(1, len(self.users) + 1):
                visited[i] = self.social_paths_bfs(i, userID)
        return visited
    
    #bfs returns shortest path v dfs
    def social_paths_bfs(self, starting_vertex, target):
        q = deque()
        visited = []
        q.append([starting_vertex])  #list v set??
        while q:
            social_path = q.pop()
            last_vertex = social_path[-1:]
            if last_vertex not in visited:
                if last_vertex == target:
                    return social_path
                #print(last_vertex, social_path)
                visited.append(last_vertex)
            for child in self.friendships[last_vertex]:
                duplicate_path = list(social_path)
                duplicate_path.append(child)
                q.append(duplicate_path)


if __name__ == '__main__':
    # num_users = 10
    # num_friendships = 9
    # sg = SocialGraph()
    # start_time = time.time()
    # sg.populateGraph(num_users, num_friendships)
    # end_time = time.time()
    # print (f"Quadratic runtime: {end_time - start_time} seconds")
    # start_time = time.time()
    # sg.populateGraphLinear(num_users, num_friendships)
    # end_time = time.time()
    # print (f"Linear runtime: {end_time - start_time} seconds")
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

#thurs lecture
#https://www.youtube.com/watch?v=FL9MN3TA_VQ

#3. Questions
#1. To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why?
# 100 users with 10 friends each would equal 1000 connections, but since connections are bidirectional you would 
# only have to call addFriendship 500 times.
#2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a 
# particular user’s extended social network? What is the average degree of separation between a user and those in 
# his/her extended network?
# 