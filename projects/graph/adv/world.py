from room import Room
import random


class World:
  def __init__(self):
    self.startingRoom = None
    self.rooms = {}
  
  def getRandomDirection(self,room):
    dirs = []
    if room.n_to == None:
        dirs.append("n")
    if room.s_to == None:
        dirs.append("s")
    if room.e_to == None:
        dirs.append("e")
    if room.w_to == None:
        dirs.append("w")

    random.shuffle(dirs)
    return dirs[0]
  
  def generateDefaultRooms(self):
    self.rooms = {
      'outside':  Room("Outside Cave Entrance",
               "North of you, the cave mount beckons"),

      'foyer':  Room("Foyer", """Dim light filters in from the south. Dusty
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

  ####
  # MODIFY THIS CODE
  ####
  def generateRooms(self, numRooms):
    self.rooms = {}

    if numRooms < 1:
      print("Must create at least 1 room")
      return None

    previous = None
    # Create n rooms
    for i in range(0, numRooms):

      new_room = Room(f"Room {i}", "You are standing in an empty room.")
      if i == 0:
        print(f"{i} FirstRoom")
        # sets first room coordinate to 0,0 and store in rooms
        new_room.x = 0
        new_room.y = 0
        self.rooms[0] = {0: new_room}
        # since rooms is dict, we need easy way to access previously created room
      else:
        # gets random direction from previous room and sets coordinate of new room accordingly
        direction = self.getRandomDirection(previous)
        if direction == "n":
          new_room.x = previous.x
          new_room.y = previous.y - 1
        elif direction == "s":
          new_room.x = previous.x
          new_room.y = previous.y + 1  
        elif direction == "w":
          new_room.x = previous.x - 1
          new_room.y = previous.y
        elif direction == "s":
          new_room.x = previous.x + 1
          new_room.y = previous.y
        print(f"{i}, {direction}, p: ({previous.x},{previous.y}), n: ({new_room.x},{new_room.y})")
        previous.connectRooms(direction, new_room)
        
        if new_room.x not in self.rooms:
          self.rooms[new_room.x] = {}
        self.rooms[new_room.x][new_room.y] = new_room
      previous = new_room
          









    # Hard-code a single room connection.
    # You should replace this with procedural connection code.
    if numRooms > 1:
      self.rooms[0].connectRooms("n", self.rooms[1])

    # Set the starting room to the first room. Change this if you want a new starting room.
    self.startingRoom = self.rooms[0]

    return self.rooms





