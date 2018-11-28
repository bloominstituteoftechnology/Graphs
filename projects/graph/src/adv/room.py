# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.light = True
        self.monsters = []
    def __str__(self):
        monsters_alive = [monster for monster in self.monsters if not monster.killed]
        if len(monsters_alive) > 0:
            return f"\n\n{self.name}\n  {self.description}\n\n There is a {''.join([monster.name for monster in self.monsters])} blocking the way!"
        return f"\n\n{self.name}\n  {self.description}\n\n{self.getItems()}"
    def getItems(self):
        return f"This room contains: {', '.join([item.name for item in self.items])}"
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
    def findItembyName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
    def addMonster(self, monster):
        self.monsters.append(monster)
    def findMonsterbyName(self, name):
        for monster in self.monsters:
            if monster.name.lower() == name.lower():
                return monster
        return None
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