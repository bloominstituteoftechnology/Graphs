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

''' Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4 
'''

''' Remember these steps:
1. What is the problem asking for? Translate it into graph terminology that you have learned this week.
2. Build your graph.
3. Run graph operations to return what's asked for. '''

small_islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

big_islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

def island_counter(islands):
	# create a visited matrix
	visited = []
	for i in range(len(islands)):
		visited.append([False] * len(islands[0]))
	# Walk through each cell/position in the matrix
	island_count = 0
	for x in range(len(islands[0])):
		# If that cell/position has not been visited...
		for y in range(len(islands)):
			if not visited[y][x]:
			# If the cell is a 1... 
				if islands[y][x] == 1:
					# Do a DFT and mark each as visited
					visited = dft(x, y, islands, visited) # DEFINE DFT
					# Then increment our island counter by one
					island_count += 1

	return island_count

def dft(x, y, islands, visited):
	# Create an empty Stack
  stack = Stack()
	# Push the starting cell to the stack
  stack.push((x, y))
	  # While the Stack is not empty
  while stack.size() > 0:
			# Pop the first location
    v = stack.pop()
    x = v[0]
    y = v[1]
    if not visited[y][x]:
				# Mark it as visited (print it and add it to the visited list)
      visited[y][x] = True
        # Then push each of its neighbors onto the Stack
      for neighbor in get_neighbors((x, y), islands): #NEED TO DEFINE GET NEIGHBORS
        stack.push(neighbor)
  return visited

def get_neighbors(vertex, graph_matrix):
    x = vertex[0]
    y = vertex[1]
    neighbors = []
    # Check north
    if y > 0 and graph_matrix[y - 1][x] == 1:
        neighbors.append((x, y - 1))
    # Check south
    if y < len(graph_matrix) - 1 and graph_matrix[y + 1][x] == 1:
        neighbors.append((x, y+1))
    # Check east
    if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x + 1] == 1:
        neighbors.append((x + 1, y))
    # Check west
    if x > 0 and graph_matrix[y][x - 1] == 1:
        neighbors.append((x - 1, y))
    return neighbors


# print(island_counter(small_islands))
# print(island_counter(big_islands))

# # Adjacency List
# {
#   0 : 1, 5
#   1 : 6
#   2 : 1, 3
# }

# # Adjacency Matrix
# [[0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,], [0,1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,], [0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]]

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

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"User {i}")
        # Generate all possible friendship combinations
        possibleFriendships = []
        # Avoid duplicates by ensuring the first number is always smaller than the second number
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID,friendID))
        # Shuffle the possible frienships (use Fisher-Yates)
        random.shuffle(possibleFriendships)
        # Create friendships for the first X pairs of the list
        # X = Friendships_needed
        # Friendships_needed = numusers * (avgFriendships // 2)
        # Need to divide by 2 since each addFriendship() creates 2 friendships
        for i in range(numUsers * (avgFriendships // 2)):
            friendships = possibleFriendships[i]
            self.addFriendship(friendships[0], friendships[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

				# Create an empty Queue
        queue = Queue()
				# Create an empty Visited dictionary
        visited = {}
				# Add a PATH TO the starting vertex to the Queue
        queue.enqueue([userID])
				# While the queue is not empty...
        while queue.size() > 0:
				  # Dequeue the first PATH
          path = queue.dequeue()
					# Grab the last vertex from the path
          v = path[-1]
					# If it has not been visited...
          if v not in visited:
					  # When we reach an unvisited user, append the path to the visited dictionary
            visited[v] = path
						# Then enqueue PATHS TO each of its neighbors in the queue
            for neighbor in self.friendships[v]:
              path_copy = path.copy()
              path_copy.append(neighbor)
              queue.enqueue(path_copy)
			  # return visited
        return visited


sg = SocialGraph()
sg.populateGraph(10, 2)
print(sg.friendships)
connections = sg.getAllSocialPaths(8)
print(connections)

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    connections = sg.getAllSocialPaths(1)
    print(f"Users in extended social network: {len(connections) - 1}")
    total_social_paths = 0
    for user_id in connections:
        total_social_paths += len(connections[user_id])
    print(f"Avg length of social path: {total_social_paths / len(connections)}")