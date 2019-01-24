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

    def findTreasure(self):
        queue = []
        visited = []
        shortest_path = []
        queue.append(self.currentRoom)

        while len(queue) > 0:
            found = queue.pop(0)

            if any(x for x in found.items if x.name == "Treasure"):
                print(f"---Treasure discovered in {found.name}---")
                for room in visited:
                    shortest_path.append(room.name)
                break

            if found not in visited:
                visited.append(found)
                found.n_to and queue.append(found.n_to)
                found.e_to and queue.append(found.e_to)
                found.s_to and queue.append(found.s_to)
                found.w_to and queue.append(found.w_to)

        print(f"shortest_path: {shortest_path}")
        return shortest_path
