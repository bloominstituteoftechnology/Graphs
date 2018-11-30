class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


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

    def findTreasure(self, startRoom):
        q = Queue()
        visited = set()
        q.enqueue(([], startRoom))
        while q.size() > 0:
            path_and_room = q.dequeue()
            room = path_and_room[1]
            if room not in visited:
                if len(room.items) > 0:
                    for item in room.items:
                        if item.name == "Treasure":
                            return path_and_room[0]
                visited.add(room)
                if room.n_to is not None:
                    new_path = list(path_and_room[0])
                    new_path.append("n")
                    q.enqueue((new_path, room.n_to))
                if room.s_to is not None:
                    new_path = list(path_and_room[0])
                    new_path.append("s")
                    q.enqueue((new_path, room.s_to))
                if room.e_to is not None:
                    new_path = list(path_and_room[0])
                    new_path.append("e")
                    q.enqueue((new_path, room.e_to))
                if room.w_to is not None:
                    new_path = list(path_and_room[0])
                    new_path.append("w")
                    q.enqueue((new_path, room.w_to))
        return None
