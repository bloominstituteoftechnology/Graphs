
# class World:
#     def __init__(self):
#         self.startingRoom = None
#         self.rooms = {}
#         self.occupied = set()

#     def generateRooms(self, numRooms):
#         self.rooms = {}

#     def getRandomDirection(self, room, coords):
#         dirs = []
#         if room.n_to is None and self._checkCoordinates(coords, "n"):
#             dirs.append("n")
#         if room.s_to is None and self._checkCoordinates(coords, "s"):
#             dirs.append("s")
#         if room.w_to is None and self._checkCoordinates(coords, "w"):
#             dirs.append("w")
#         if room.e_to is None and self._checkCoordinates(coords, "e"):
#             dirs.append("e")
#         random.shuffle(dirs)
#         if len(dirs) > 0:
#             return dirs[0]
#         else:
#             return None

#     def generateDefaultRooms(self):
#         self.rooms = {
#             'outside':  Room("Outside Cave Entrance",
#                              "North of you, the cave mount beckons"),

#             'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
#         passages run north and east."""),

#             'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
#         into the darkness. Ahead to the north, a light flickers in
#         the distance, but there is no way across the chasm."""),

#             'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
#         to north. The smell of gold permeates the air."""),

#             'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
#         chamber! Sadly, it has already been completely emptied by
#         earlier adventurers. The only exit is to the south."""),
#         }
#         self.rooms['outside'].connectRooms("n", self.rooms['foyer'])
#         self.rooms['foyer'].connectRooms("n", self.rooms['overlook'])
#         self.rooms['foyer'].connectRooms("e", self.rooms['narrow'])
#         self.rooms['narrow'].connectRooms("n", self.rooms['treasure'])
#         self.startingRoom = self.rooms['outside']

#     def _updateCoordinates(self, coords, dir):
#         new_coords = list(coords)
#         if dir == "n":
#             new_coords[1] += 1
#         if dir == "s":
#             new_coords[1] -= 1
#         if dir == "e":
#             new_coords[0] += 1
#         if dir == "w":
#             new_coords[0] -= 1

#     def _checkCoordinates(self, coords, direction):
#         """
#         Check if the grid in an adjoining direction is unoccupied
#         """
#         return str(self._updateCoordinates(coords, direction)) not in self.occupied

#     def createRandomRooms(self, numRooms):
#         self.rooms = {}

#         if numRooms < 1:
#             print("Must create at least 1 room")
#             return None

#         # Create n rooms
#         for i in range(0, numRooms):
#             # Create n rooms.
#             new_room = Room(
#                 f"Room {i}", "You are standing in an empty room with {i}.")
#             self.rooms[i] = new_room
#             # If it's not the first room....
#             if i > 0:
#                 # ...connect to the previous room in a random direction
#                 random_dir = self.getRandomDirection(self.rooms[i-1])
#                 if random_dir is not None:
#                     self.rooms[i-1].connectRooms(random_dir, new_room)

#         # Set the starting room to the first room. Change this if you want a new starting room.
#         self.startingRoom = self.rooms[0]

#         return self.rooms

#     ####
#     # MODIFY THIS CODE
#     ####
#     def generateRooms(self, numRooms):
#         """
#         Generate a random graph of rooms
#         """
#         self.rooms = {}

#         if numRooms < 1:
#             print("Must create at least 1 room")
#             return None
# # The coordinates of our room. We start from (0,0)
#         xy = [0, 0]

#         # Keep track of which grid spots are occupied
#         self.occupied = set()
#         # Create a set that will hold the IDs of rooms with valid connections available
#         validRooms = set()

#         # Create n rooms
#         for i in range(0, numRooms):
#             # Create n rooms.
#             new_room = Room(f"Room {i}", "You are standing in an empty room.")
#             self.rooms[i] = new_room
#             # If it's not the first room....
#             if i == 0:
#                 # ...connect to the previous room in a random direction
#                 random_dir = self.getRandomDirection(self.rooms[i-1])
#                 if random_dir is not None:
#                     self.rooms[i-1].connectRooms(random_dir, new_room)

#         # Set the starting room to the first room. Change this if you want a new starting room.
#         self.startingRoom = self.rooms[0]

#         return self.rooms

#     def traverseRooms(self, room):
#         stack = [self.rooms[room]]
#         visited = []
#         while len(stack) > 0:
#             current = stack.pop()
#             visited.append(current)

#             paths = [current.n_to, current.s_to, current.e_to, current.w_to]

#             for path in paths:
#                 if path and path not in visited:
#                     stack.append(path)

#         for v in visited:
#             print(f'{v.name} => ', end='', flush=True)
#         print('\n')
#         return visited
