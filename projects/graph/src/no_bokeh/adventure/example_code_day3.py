import random


# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
   def __init__(self, name, description):
       self.name = name
       self.description = description
       self.n_to = None
       self.s_to = None
       self.e_to = None
       self.w_to = None
       self.items = []
   def __str__(self):
       return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getItemsString()}\n{self.getExits()}\n"
   def printRoomDescription(self, player):
       print(str(self))
   def getExits(self):
       exits = []
       if self.n_to is not None:
           exits.append("n")
       if self.s_to is not None:
           exits.append("s")
       if self.w_to is not None:
           exits.append("w")
       if self.e_to is not None:
           exits.append("e")
       return f"Exits: [{', '.join(exits)}]"
   def getItemsString(self):
       if len(self.items) > 0:
           return f"The room contains: {', '.join([item.name for item in self.items])}"
       else:
           return "The room is empty"
   def connectRooms(self, direction, connectingRoom):
       if direction == "n":
           self.n_to = connectingRoom
           connectingRoom.s_to = self
       elif direction == "s":
           self.s_to = connectingRoom
           connectingRoom.n_to = self
       elif direction == "e":
           self.e_to = connectingRoom
           connectingRoom.w_to = self
       elif direction == "w":
           self.w_to = connectingRoom
           connectingRoom.e_to = self
       else:
           print("INVALID ROOM CONNECTION")
           return None
   def getRoomInDirection(self, direction):
       if direction == "n":
           return self.n_to
       elif direction == "s":
           return self.s_to
       elif direction == "e":
           return self.e_to
       elif direction == "w":
           return self.w_to
       else:
           return None
   def addItem(self, item):
       self.items.append(item)
   def removeItem(self, item):
       self.items.remove(item)
   def findItemByName(self, name):
       for item in self.items:
           if item.name.lower() == name.lower():
               return item
       return None

class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
    def getRandomDirection(self, room):
        dirs = []
        if room.n_to is None:
            dirs.append("n")
        if room.s_to is None:
            dirs.append("s")
        if room.w_to is None:
            dirs.append("w")
        if room.e_to is None:
            dirs.append("e")
        random.shuffle(dirs)
        if len(dirs) > 0:
            return dirs[0]
        else:
            return None

    def generateDefaultRooms(self):
        self.rooms = {
            'outside':  Room("Outside Cave Entrance",
                             "North of you, the cave mount beckons"),

            'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east."""),

            'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm."""),

            'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air."""),

            'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south."""),
        }
        self.rooms['outside'].connectRooms("n", self.rooms['foyer'])
        self.rooms['foyer'].connectRooms("n", self.rooms['overlook'])
        self.rooms['foyer'].connectRooms("e", self.rooms['narrow'])
        self.rooms['narrow'].connectRooms("n", self.rooms['treasure'])
        self.startingRoom = self.rooms['outside']

    def _updateCoordinates(self, coords, dir):
        new_coords = list(coords)
        if dir == "n":
            new_coords[1] += 1
        if dir == "s":
            new_coords[1] -= 1
        if dir == "e":
            new_coords[0] += 1
        if dir == "w":
            new_coords[0] -= 1

    ####
    # MODIFY THIS CODE
    ####
    def generateRooms(self, numRooms):
        self.rooms = {}

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # Create n rooms
        for i in range(0, numRooms):
            # Create n rooms.
            new_room = Room(f"Room {i}", "You are standing in an empty room.")
            self.rooms[i] = new_room
            # If it's not the first room....
            if i > 0:
                # ...connect to the previous room in a random direction
                random_dir = self.getRandomDirection(self.rooms[i-1])
                if random_dir is not None:
                    self.rooms[i-1].connectRooms(random_dir, new_room)

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        return self.rooms