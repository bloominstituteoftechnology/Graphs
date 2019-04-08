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
        if direction == "north":
            self.north_to = connectingRoom
            connectingRoom.south_to = self
        elif direction == "south":
            self.south_to = connectingRoom
            connectingRoom.north_to = self
        elif direction == "east":
            self.east_to = connectingRoom
            connectingRoom.west_to = self
        elif direction == "west":
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

    # find an item by name method
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None 

    # get the current connected room in a certain direction
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.north_to
        elif direction == "s":
            return self.south_to
        elif direction == "e":
            return self.east_to
        elif direction == "w":
            return self.west_to
        else:
            return None