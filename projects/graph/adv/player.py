class Player:
    def __init__(self, name, startingRoom, startingItems=[]):
        self.name = name
        self.currentRoom = startingRoom
        self.items = startingItems
        def printStatus(self):
            print(f"Your are {self.name}")
            def printInventory(self):
                print("this is everything in your stash:\n")
                for item in self.items:
                    print(f"  {item.name} - {item.description}\n")
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            nextRoom.printRoomDescription(self)
        else:
            print("Yeah, thats a wall, or water, or whatever you can't go that way.")
    def look(self, direction=None):
        if direction is None:
            self.currentRoom.printRoomDescription(self)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                nextRoom.printRoomDescription(self)
            else:
                print("ummm, nothing there.")
    def dropItem(self, itemName):
        itemToDrop = self.findItemByName(" ".join(itemName))
        if itemToDrop is not None:
            self.removeItem(itemToDrop)
            self.currentRoom.addItem(itemToDrop)
            itemToDrop.on_drop()
        else:
            print("Come on dude, your not even holding that.")
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
            return item
            return None
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
