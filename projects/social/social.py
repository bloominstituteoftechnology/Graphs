import random
import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue, Stack

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

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

        # Add users
        # call addUser() until our number of users is numUsers
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create random friendships
        # totalFriendships = avgFriendships * numUsers
        # Generate a list of all possible friendships
        possibleFriendships = []
        # Avoid dups by ensuring the first ID is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append( (userID, friendID) )

        # Shuffle the list
        random.shuffle(possibleFriendships)
        # print("random friendships:")
        # print(possibleFriendships)

        # Slice off totalFriendships from the front, create friendships
        totalFriendships = avgFriendships * numUsers // 2
        # print(f"Friendships to create: {totalFriendships}\n")
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.addFriendship( friendship[0], friendship[1] )




    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        graph = Graph()
        connections = []
        q = Queue()
        
        for i in range(1, len(sg.friendships) + 1):
            if sg.friendships[i] != set():
                #popping off each item and getting ALL connections
                while len(sg.friendships[i]) > 0:
                    friend = sg.friendships[i].pop()
                    connections.append((i, friend))
        
        #building graph
        for d in range(1,11):
            graph.add_vertex(d)

        #making connections
        for pair in connections:
            graph.add_edge(pair[0],pair[1])
        print(graph.vertices)

        visited = {}
 
        for i in range(1,11):
            visited[i] = graph.bfs(userID,i)
        print(f'visited: {visited}')
  

        # for x in check_array: # for every instance in check array
        #     if x[1] == userID: #if the first item (the child) exists, then you will want to grab the parent and call recursion to climb up the tree
        #         visited[x[0]] = [x[1], x[0]]
        # print(visited)
        #     if x[1] in children: #if the parent node is a child (not a top node)
        #         print(f'passing in {x[1]}')
        #         return earliest_ancestor(ancestors,x[1]) #call recursion on that node
        #     else:
        #         return x[1] #if it is not a child, you have reached the top
        # return visited
       
        
        # print(q.size())
        # print(graph.vertices)
        # for i in range(1,11):
        #     print(i)
  
        # def recall(i=userID):
        #     print(i)
        #     if i < 11:
        #         q.enqueue([userID])
        #         visited = set()
        #         while q.size() > 0:
        #             path = q.dequeue()
        #             v = path[-1]
        #             # print(v)
                    
        #             if v == i:
        #                 set_visited[i] = path
        #                 print(set_visited)
        #                 i += 1
        #                 return recall(i)
                        
        #             visited.add(v)

        #             for neighbor in graph.vertices[v]:
        #                 path_copy = path.copy()
        #                 path_copy.append(neighbor)
        #                 q.enqueue(path_copy)
        #     else:
        #         return
        # recall()


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    # print("USERS:")
    # print(sg.users)
    # print("FRIENDSHIPS:")
    # print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)