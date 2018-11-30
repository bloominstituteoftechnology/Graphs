from room import Room
import random


class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.avoid_list = set()

    def generateDefaultRooms(self):
        self.rooms = {
            "outside": Room(
                "Outside Cave Entrance", "North of you, the cave mount beckons"
            ),
            "foyer": Room(
                "Foyer",
                """Dim light filters in from the south. Dusty
        passages run north and east.""",
            ),
            "overlook": Room(
                "Grand Overlook",
                """A steep cliff appears before you, falling
        into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""",
            ),
            "narrow": Room(
                "Narrow Passage",
                """The narrow passage bends here from west
        to north. The smell of gold permeates the air.""",
            ),
            "treasure": Room(
                "Treasure Chamber",
                """You've found the long-lost treasure
        chamber! Sadly, it has already been completely emptied by
        earlier adventurers. The only exit is to the south.""",
            ),
        }
        self.rooms["outside"].connectRooms("n", self.rooms["foyer"])
        self.rooms["foyer"].connectRooms("n", self.rooms["overlook"])
        self.rooms["foyer"].connectRooms("e", self.rooms["narrow"])
        self.rooms["narrow"].connectRooms("n", self.rooms["treasure"])
        self.startingRoom = self.rooms["outside"]

    ####
    # MODIFY THIS CODE
    ####
    def update_coordinates(self, coords, direction):
        new_coords = list(coords)
        if direction == "n":
            new_coords[1] += 1
        if direction == "e":
            new_coords[0] += 1
        if direction == "s":
            new_coords[1] -= 1
        if direction == "w":
            new_coords[0] -= 1
        return new_coords

    def check_coordinates(self, coords, direction):
        return str(self.update_coordinates(coords, direction)) not in self.avoid_list

    def get_random_direction(self, room, coords):
        paths = []
        if self.check_coordinates(coords, "n"):
            paths.append("n")
        if self.check_coordinates(coords, "e"):
            paths.append("e")
        if self.check_coordinates(coords, "s"):
            paths.append("s")
        if self.check_coordinates(coords, "w"):
            paths.append("w")
        random.shuffle(paths)
        if len(paths) > 0:
            return paths[0]
        else:
            return None

    def generateRooms(self, numRooms):
        self.rooms = {}
        self.avoid_list = set()
        valid_rooms = set()
        coords = [0, 0]

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        for i in range(0, numRooms):
            new_room = Room(f"Room {i}", f"Standing in Room {i}")
            self.rooms[i] = new_room

            if i == 0:
                valid_rooms.add(i)
                self.avoid_list.add(str(coords))

            else:
                random_path = None

                while random_path is None:
                    previous_room = valid_rooms.pop()
                    coords = self.rooms[previous_room].coords
                    random_path = self.get_random_direction(
                        self.rooms[previous_room], coords
                    )

                    if random_path is not None:
                        valid_rooms.add(previous_room)

                coords = self.update_coordinates(coords, random_path)
                self.rooms[previous_room].connectRooms(random_path, new_room)
                self.avoid_list.add(str(coords))
                new_room.coords = coords
                valid_rooms.add(i)

        self.startingRoom = self.rooms[0]
        return self.rooms

