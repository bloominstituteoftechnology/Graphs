from room import Room
from item import Item
import random


class World:
  def __init__(self):
    self.startingRoom = None
    self.rooms = {}
    self.treasure = None
  
  def _getRandomDirection(self,room):
    dirs = [] 
    if room.n_to == None:
        dirs.append("n")
    if room.s_to == None:
        dirs.append("s")
    if room.e_to == None:
        dirs.append("e")
    if room.w_to == None:
        dirs.append("w")

    if len(dirs) < 1:
      return None

    random.shuffle(dirs)
    return dirs
  
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

  # Drops treasure in a random room
  def dropTreasure(self):
    # create item
    treasure = Item("Treasure", "Cobbler's Boot: The legendary boot that the town Cobbler used to single handedly drive away the Roman legion.")
    self.treasure = treasure
    # creates list of all keys to rooms, shuffle and select random room to put boot.
    keys = list(self.rooms.keys())
    random.shuffle(keys)
    room = self.rooms[keys.pop()]

    room.addItem(treasure)
    print(room.name, room.getItemsString())

  def generateRooms(self, numRooms):
    self.rooms = {}

    if numRooms < 1:
      print("Must create at least 1 room")
      return None

    # previous = None
    # Create n rooms
    stack = []
    for i in range(0, numRooms):

      new_room = Room(f"Room {i}", "You are standing in an empty room.")
      if i == 0:
        # print(f"{i} FirstRoom")
        # sets first room coordinate to 0,0 and store in rooms
        new_room.coordinates = (0,0)
        self.rooms[(0,0)] = new_room
        # since rooms is dict, we need easy way to access previously created room
      else:
        # gets random direction from previous room and sets coordinate of new room accordingly
        isCoordinateAvailable = False
        while(not isCoordinateAvailable):
          directions = self._getRandomDirection(previous)
          # returns list where [direction, x coordinate, y coordinate]
          coordinates = self._findAvailableCoordinate(directions,previous)
          if coordinates:
            new_room.coordinates = (coordinates[1],coordinates[2])
            previous.connectRooms(coordinates[0], new_room)
            isCoordinateAvailable = True
          else:
            previous = stack.pop()
        
        self.rooms[new_room.coordinates] = new_room
      previous = new_room
      stack.append(new_room)
          

    # Hard-code a single room connection.
    # You should replace this with procedural connection code.
   
    # Set the starting room to the first room. Change this if you want a new starting room.
    self.startingRoom = self.rooms[(0,0)]

    return self.rooms
  
  # finds available coordinate from list of directions as [direction,x,y] else returns None
  def _findAvailableCoordinate(self,directions,previous):
    
    while directions:
      direction = directions.pop()
      if direction == "n":
        possible_x = previous.coordinates[0]
        possible_y = previous.coordinates[1] - 1
      elif direction == "s":
        possible_x = previous.coordinates[0]
        possible_y = previous.coordinates[1] + 1  
      elif direction == "w":
        possible_x = previous.coordinates[0] - 1
        possible_y = previous.coordinates[1]
      elif direction == "e":
        possible_x = previous.coordinates[0] + 1
        possible_y = previous.coordinates[1]
      
      if (possible_x, possible_y) not in self.rooms:
        return [direction,possible_x,possible_y]
      

    return None




