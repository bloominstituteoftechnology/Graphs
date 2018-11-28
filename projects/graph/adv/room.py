# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
   def __init__(self, name, description, id=None, coordinates=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        # if id == None:
        #     id = -1
        self.id = id
        if coordinates == None:
            coordinates = (0, 0)
        self.coordinates = coordinates

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