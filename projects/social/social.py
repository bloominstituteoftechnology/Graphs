from util import Queue
from random import randint


class User:
	def __init__(self, name):
		self.name = name


class SocialGraph:
	def __init__(self):
		self.last_id = 0
		self.users = {}
		self.friendships = {}

	def add_friendship(self, user_id, friend_id):
		"""
		Creates a bi-directional friendship
		"""
		if user_id == friend_id:
			# print("WARNING: You cannot be friends with yourself")
			return False  # added to break loop
		elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
			# print("WARNING: Friendship already exists")
			return False  # added to break loop
		else:
			self.friendships[user_id].add(friend_id)  # Adds edge between user and friend
			self.friendships[friend_id].add(user_id)  # Adds edge between friend and user
			# print(f'Friendship created between {user_id} and {friend_id}')
			return True  # added to break loop

	def add_user(self, name):
		"""
		Create a new user with a sequential integer ID
		"""
		self.last_id += 1  # automatically increment the ID to assign the new user
		self.users[self.last_id] = User(name)  # Creates a new user with new id with a name
		self.friendships[self.last_id] = set()  # Adds the new user to the friendships dict

	def populate_graph(self, num_users, avg_friendships):
		"""
		Takes a number of users and an average number of friendships
		as arguments

		Creates that number of users and a randomly distributed friendships
		between those users.

		The number of users must be greater than the average number of friendships.
		"""
		# Reset graph
		self.last_id = 0  # Set last id to 0
		self.users = {}  # Users is an empty dict
		self.friendships = {}  # Friendships is an empty dict that contains edges
		# !!!! IMPLEMENT ME

		# Add users
		# Takes in int and creates a user from the int - needs a name
		for i in range(num_users):  # num_users is an int, so we need to do the range of the int
			self.add_user(f'User {i + 1}')  # creates a new user with the name set to i + 1 because 0 is key error
		# for user in self.users:  # loop through users array
		# 	print(f'user {user}')  # print user name

		# Create friendships
		# We need to create random friendships between users
		# Goal number of friendships = users * avg_friendships
		# Actual friendships needs to be incremented and checked against goal friendships

		goal_friendships = (num_users * avg_friendships)  # This is the number of total friendships after creating them
		num_friendships = 0  # Current number of friendships
		total_users = len(self.users)  # Int value of total users for randint
		# print('Total Users:', total_users)
		while num_friendships < goal_friendships:  # While current FSs is less than goal FSs
			# print('num_friendships', num_friendships)
			# randint(a, b) returns N (a <= N <= b)
			# Take a user and a friend id
			current_user = randint(1, total_users)  # Grab current user randomly
			# print('current_user', current_user)
			current_friend = randint(1, total_users)  # Grand another user(friend) randomly
			# print('current_friend', current_friend)
			# Run add friendship and if it returns, create it
			# If returns, increase num_friendships by 2 (FRIENDSHIP IS A TWO-WAY STREET BECKY!)
			# Run this til line 65 is satisfied
			if self.add_friendship(current_user, current_friend):  # Run function on them
				num_friendships += 2  # Increase friendship by two because see line 79

	# print('self.friendships', self.friendships)

	def get_all_social_paths(self, user_id):
		"""
		Takes a user's user_id as an argument

		Returns a dictionary containing every user in that user's
		extended network with the shortest friendship path between them.

		The key is the friend's ID and the value is the path.
		"""
		visited = {}  # Note that this is a dictionary, not a set
		# I spent like an hour trying to use BFS/DFS here but the line above makes me thing it won't work
		# I also don't want to troubleshoot it because I want to go for a walk
		# So let's just pull logic from BFS/DFS and add it here
		# So I can go for a walk with my dog

		queue = Queue()  # Create a queue
		queue.enqueue([user_id])  # Add current user with a list
		while queue.size():  # While there is a queue
			path = queue.dequeue()  # Set path to queue list
			node = path[-1]  # Grab last item
			print('visited', visited)
			print('Queue:', list(queue.queue))
			if node not in visited:  # If we haven't been to where we are
				# print('what do i do here')  # Something is missing here
				print('1 path pre', path)
				# print('node', node)
				# We need to update it so that where we are is the path there
				# Because we already have the node
				# We are currently at the node, but we don't want the node
				# We want how we got there
				visited[node] = path
				# Hot ham it worked!
				for neighbor in self.friendships[node]:  # For each neighbor node
					print('2 loop path', path)
					new_path = list(path)
					print('3 loop neighbor', neighbor)
					new_path.append(neighbor)
					queue.enqueue(new_path)
					print('4 new_path', new_path)
		return visited


if __name__ == '__main__':
	sg = SocialGraph()
	sg.populate_graph(10, 2)
	print(sg.friendships)
	connections = sg.get_all_social_paths(1)
	print('connections', connections)
