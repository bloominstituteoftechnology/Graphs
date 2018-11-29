from room import Room
import random


class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.occupied = set()
    def getRandomDirection(self, room, coords):
        """
        Select a random direction from all valid connections.
        This checks if the connection is unnoccupied and if the
        adjacent grid is also unoccupied.
        """
        dirs = []
        if room.n_to is None and self._checkCoordinates(coords, "n"):
            dirs.append("n")
        if room.s_to is None and self._checkCoordinates(coords, "s"):
            dirs.append("s")
        if room.w_to is None and self._checkCoordinates(coords, "w"):
            dirs.append("w")
        if room.e_to is None and self._checkCoordinates(coords, "e"):
            dirs.append("e")
        random.shuffle(dirs)
        if len(dirs) > 0:
            return dirs[0]
        else:
            return None
    def generateDefaultRooms(self):
        self.rooms = {
            'outside':  Room("Outside Cave Entrance",
                             "North of you, the cave mount beckons"),

            'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
        passages run north and east."""),

            'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm."""),

            'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
        to north. The smell of gold permeates the air."""),

            'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south."""),
        }
        self.rooms['outside'].connectRooms("n", self.rooms['foyer'])
        self.rooms['foyer'].connectRooms("n", self.rooms['overlook'])
        self.rooms['foyer'].connectRooms("e", self.rooms['narrow'])
        self.rooms['narrow'].connectRooms("n", self.rooms['treasure'])
        self.startingRoom = self.rooms['outside']

    def _updateCoordinates(self, coords, direction):
        """
        Increment xy coordinates in one direction
        """
        new_coords = list(coords)
        if direction == "n":
            new_coords[1] += 1
        if direction == "s":
            new_coords[1] -= 1
        if direction == "e":
            new_coords[0] += 1
        if direction == "w":
            new_coords[0] -= 1
        return new_coords

    def _checkCoordinates(self, coords, direction):
        """
        Check if the grid in an adjoining direction is unoccupied
        """
        return str(self._updateCoordinates(coords, direction)) not in self.occupied
    ####
    # MODIFY THIS CODE
    ####
    def generateRooms(self, numRooms):
        """
        Generate a random graph of rooms
        """
        self.rooms = {}

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # The coordinates of our room. We start from (0,0)
        xy = [0,0]

        # Keep track of which grid spots are occupied
        self.occupied = set()

        # Create a set that will hold the IDs of rooms with valid connections available
        validRooms = set()

        # Create n rooms
        for i in range(0, numRooms):
            # Create a room
            new_room = Room(f"Room {i}", "You are standing in an empty room.")
            self.rooms[i] = new_room
            if i == 0:
                # Our first room is always valid
                validRooms.add(i)
                self.occupied.add(str(xy))
            else:
                # If it's not the first room....
                # ...connect to the previous room in a random direction
                random_dir = None

                # In case we run into a room with no valid connections, keep looping
                # until we find a room with valid connections.
                # Note that there will ALWAYS be a valid room available
                while random_dir is None:
                    # Get a room that we think is valid
                    connectingRoom = validRooms.pop()
                    # Get the coordinates of that room
                    xy = self.rooms[connectingRoom].xy
                    # See if we can get a random direction from that room
                    random_dir = self.getRandomDirection(self.rooms[connectingRoom], xy)
                    # If our room is valid (i.e. not None) then we put it back in our
                    # set of valid rooms.
                    if random_dir is not None:
                        validRooms.add(connectingRoom)
                    # If it's NOT valid, then we don't put it back into validRooms
                    # and we try again with a different room.

                # We have a valid direction, so update the room and make the connection
                xy = self._updateCoordinates(xy, random_dir)
                self.rooms[connectingRoom].connectRooms(random_dir, new_room)
                self.occupied.add(str(xy))
                new_room.xy = xy
                validRooms.add(i)

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        if len(self.occupied) == numRooms:
            print("World successfully created!")
        else:
            print("Something is wrong....")

        return self.rooms
    def printMap(self):
        coordinates = [[int(i) for i in x[1:-1].split(", ")] for x in self.occupied]
        xMax = xMin = yMax = yMin = 0
        for c in coordinates:
            if c[0] > xMax:
                xMax = c[0]
            if c[0] < xMin:
                xMin = c[0]
            if c[1] > yMax:
                yMax = c[1]
            if c[1] < yMin:
                yMin = c[1]
        row = [" "] * (1 + yMax - yMin)
        grid = []
        for i in range(0, 1 + xMax - xMin):
            grid.append(list(row))
        for c in coordinates:
            if c[0] == 0 and c[1] == 0:
                grid[c[0] - xMin][c[1] - yMin] = "S"
            else:
                grid[c[0] - xMin][c[1] - yMin] = "0"
        gridString = ""
        for row in grid:
            for room in row:
                gridString += room
            gridString += "\n"
        print (gridString)