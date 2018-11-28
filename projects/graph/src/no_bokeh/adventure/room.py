class Room:
	def __init__(self, name, desciption):
		self.name = name
		self.desciption = desciption
		self.items = []
		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None

	def room_direction(self, direction):
		if direction == 'n':
			return self.n_to
		elif direction == "s":
			return self.s_to
		elif direction == "e":
			return self.e_to
		elif direction == "w":
			return self.w_to
		else:
			return None

	def getExits(self):
		exits = []
		if self.n_to is not None:
			exits.append("north")
		if self.s_to is not None:
			exits.append("south")
		if self.w_to is not None:
			exits.append("west")
		if self.e_to is not None:
			exits.append("east")

		if len(exits) == 1:
			print(exits[0])
		else:
			print(",".join(exits))

	def __str__(self):
		return str(f"\n{self.name}, {self.desciption}")