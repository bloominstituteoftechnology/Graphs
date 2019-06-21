class Player:
    def __init__(self, name, startingRoom):
        self.name = name
        self.currentRoom = startingRoom
    def travel(self, direction, showRooms = False):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(f"Direction: {direction}")
            if (showRooms):
                nextRoom.printRoomDescription(self)
        else:
            print(f"Else Direction: {direction}")
            print(self.currentRoom.getExits())
            print("You cannot move in that direction.")
