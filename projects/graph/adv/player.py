class Player:
    def __init__(self, name, startingRoom, startingItems=[]):
        self.name = name
        self.currentRoom = startingRoom
        self.items = startingItems
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")
    def look(self, direction=None):
        if direction is None:
            self.currentRoom.printRoomDescription(self)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                nextRoom.printRoomDescription(self)
            else:
                print("There is nothing there.")
    def printStatus(self):
        print(f"Your name is {self.name}")
    def printInventory(self):
        print("You are carrying:\n")
        for item in self.items:
            print(f"  {item.name} - {item.description}\n")
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
    def dropItem(self, itemName):
        itemToDrop = self.findItemByName(" ".join(itemName))
        if itemToDrop is not None:
            self.removeItem(itemToDrop)
            self.currentRoom.addItem(itemToDrop)
            itemToDrop.on_drop()
        else:
            print("You are not holding that item.")
    def findPathToItem(self, item):
        
        stack = [self.currentRoom]
        # previous_room = None
        history = {self.currentRoom.coordinates: [None, None]}

        while(len(stack) > 0):
            current_room = stack.pop()
            if(item in current_room.items):
                
                if current_room == self.currentRoom:
                    print("The treasure is underneath your nose!")
                else:
                    print(f"The treasure is in {current_room.name}")
                    print(f"Follow this path to find what you seek: \
                        \n {self._findPathFromDictionary(current_room.coordinates, history)}")
                return
            directions = current_room.getPossibleDirections(True)

            for direction in directions:
                neighbor = getattr(current_room, direction)

                if neighbor != current_room and neighbor.coordinates not in history:
                    stack.append(neighbor)
                    history[neighbor.coordinates] = [direction[0],current_room.coordinates]

        print("No treasure")

    def _findPathFromDictionary(self,room_coordinate,dictionary):
        rev_path = []

        coordinate = room_coordinate
        while coordinate:
            previous = dictionary[coordinate]
            rev_path.append(previous[0])
            coordinate = previous[1]
        rev_path.pop()
        rev_path.reverse()
        
        return ">".join(rev_path)


