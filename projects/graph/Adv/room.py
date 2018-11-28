# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.north_to = None
        self.south_to = None
        self.east_to = None
        self.west_to = None
        self.items = []

   def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getItemsString()}\n"
   
    def printRoomDescription(self, player):
        print(str(self))

    def getItemsString(self):
        if len(self.items) > 0:
            return f"The room contains: {', '.join([item.name for item in self.items])}"
        else:
            return "The room is empty"
   
    # connect room method
    def connectRooms(self, direction, connectingRoom):
        if direction == "n":
            self.north_to = connectingRoom
            connectingRoom.south_to = self
        elif direction == "s":
            self.south_to = connectingRoom
            connectingRoom.north_to = self
        elif direction == "e":
            self.east_to = connectingRoom
            connectingRoom.west_to = self
        elif direction == "w":
            self.west_to = connectingRoom
            connectingRoom.east_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None

    # Add item
    def addItem(self, item):
        self.items.append(item)
   
    # remove item
    def removeItem(self, item):
        self.items.remove(item)
