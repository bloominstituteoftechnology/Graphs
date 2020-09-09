#!/usr/bin/env

import random
import secrets

from util import Queue


class User:
	def __init__(self, name):
		self.name = name


class SocialGraph:
	def __init__(self):
		self.last_id = -1
		self.users = {}
		self.friendships = {}

	def add_friendship(self, user_id, friend_id):
		"""
		Creates a bi-directional friendship
		"""
		if user_id == friend_id:
			print("WARNING: You cannot be friends with yourself")
		elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
			print("WARNING: Friendship already exists")
		else:
			self.friendships[user_id].add(friend_id)
			self.friendships[friend_id].add(user_id)

	def add_user(self, name):
		"""
		Create a new user with a sequential integer ID
		"""
		self.last_id += 1  # automatically increment the ID to assign the new user
		self.users[self.last_id] = User(name)
		self.friendships[self.last_id] = set()

	def populate_graph(self, num_users, avg_friendships):
		"""
		Takes a number of users and an average number of friendships
		as arguments

		Creates that number of users and a randomly distributed friendships
		between those users.

		The number of users must be greater than the average number of friendships.
		"""
		# Reset graph
		self.__init__()

		for i in range(num_users):
			name = secrets.token_urlsafe(8)
			self.add_user(name)
		# print(self.users)

		for user in self.users:
			to_add_count = random.randint(
				0,
				avg_friendships * 2
			) - len(self.friendships[user])
			for i in range(to_add_count):

				# Try ten times to generate a friend before giving up
				max_tries = 10
				for i in range(max_tries):
					friend = random.randint(0, self.last_id)
					if friend not in self.friendships[user] and friend != user:
						self.add_friendship(user, friend)
						break

	def get_all_social_paths(self, user_id):
		"""
		Takes a user's user_id as an argument

		Returns a dictionary containing every user in that user's
		extended network with the shortest friendship path between them.

		The key is the friend's ID and the value is the path.
		"""
		visited = {}
		to_visit = Queue()
		to_visit.enqueue([user_id])
		while to_visit.size():
			current_path = to_visit.dequeue()
			if current_path[-1] in visited:
				continue
			else:
				visited[current_path[-1]] = current_path
				for vertex in self.friendships[current_path[-1]]:
					to_visit.enqueue(current_path + [vertex])
		return visited


if __name__ == '__main__':
	sg = SocialGraph()
	sg.populate_graph(10, 2)
	print(sg.friendships)
	connections = sg.get_all_social_paths(1)
	print(connections)
	sg.populate_graph(1000, 5)
	averages = []
	esn_counts = []
	for user in sg.users:
		connections = sg.get_all_social_paths(user)
		distances = [len(path) for path in connections.values()]
		averages.append(sum(distances) / len(distances))
		esn_counts.append(len(connections))
		print(averages[-1])
	print('Average members of extended network: ' + str(sum(esn_counts) / len(esn_counts)))
	print('Average degrees of separation: ' + str(sum(averages) / len(averages)))




