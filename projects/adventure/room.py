# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.get_exits_string()}\n"
    def __repr__(self):
        return self.name
    def print_room_description(self, player):
        print(str(self))
    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits
    def get_exits_string(self):
        return f"Exits: [{', '.join(self.get_exits())}]"
    def connect_rooms(self, direction, connecting_room):
        if direction == "n":
            self.n_to = connecting_room
            connecting_room.s_to = self
        elif direction == "s":
            self.s_to = connecting_room
            connecting_room.n_to = self
        elif direction == "e":
            self.e_to = connecting_room
            connecting_room.w_to = self
        elif direction == "w":
            self.w_to = connecting_room
            connecting_room.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None
    def get_room_in_direction(self, direction):
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
    def get_coords(self):
        return [self.x, self.y]

    def next_available_direction_to_the_right(self, direction):
        """
        Returns the exit to the right, i.e. following the right wall.
        If we entered from the east, will try north. If north doesn't
        exist, contine around counter-clockwise. If no other exits,
        return inverse direction (turn around).

        direction -- the direction we were going when entering this room
        """

        def invertDirection(dir):
            if dir == "n":
                return "s"
            if dir == "s":
                return "n"
            if dir == "e":
                return "w"
            if dir == "w":
                return "e"

        camefrom = invertDirection(direction)
        if camefrom == "e":
            if self.n_to:
                return "n"
            elif self.w_to:
                return "w"
            elif self.s_to:
                return "s"
            else:
                return "e"
        elif camefrom == "n":
            if self.w_to:
                return "w"
            elif self.s_to:
                return "s"
            elif self.e_to:
                return "e"
            else:
                return "n"
        elif camefrom == "w":
            if self.s_to:
                return "s"
            elif self.e_to:
                return "e"
            elif self.n_to:
                return "n"
            else:
                return "w"
        elif camefrom == "s":
            if self.e_to:
                return "e"
            elif self.n_to:
                return "n"
            elif self.w_to:
                return "w"
            else:
                return "s"
