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
    def get_random_direction(self, room, coords):
        paths = []
        if room.n_to is None and coords not in self.avoid_list:
            paths.append("n")
        if room.e_to is None and coords not in self.avoid_list:
            paths.append("e")
        if room.s_to is None and coords not in self.avoid_list:
            paths.append("s")
        if room.w_to is None and coords not in self.avoid_list:
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
        x = 0
        y = 0

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        for i in range(0, numRooms):
            new_room = Room(f"Room {i}", f"You are standing in an empty room {i}.")
            self.rooms[i] = new_room
            if i == 0:
                valid_rooms.add(i)
                self.avoid_list.add((x, y))
            else:
                path = None

                while path is None:
                    connecting_room = valid_rooms.pop()
                    room_coords = (
                        self.rooms[connecting_room].x_coord,
                        self.rooms[connecting_room].y_coord,
                    )
                    path = self.get_random_direction(
                        self.rooms[connecting_room], room_coords
                    )
                    if path is not None:
                        valid_rooms.add(connecting_room)
                if path == "n":
                    new_room.y_coord += 1
                elif path == "s":
                    new_room.y_coord -= 1
                elif path == "e":
                    new_room.x_coord += 1
                elif path == "w":
                    new_room.x_coord -= 1
                room_coords = (new_room.x_coord, new_room.y_coord)
                self.rooms[connecting_room].connectRooms(path, new_room)
                self.avoid_list.add(room_coords)
                valid_rooms.add(i)

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        if len(self.avoid_list) == numRooms:
            print("World successfully created!")
        else:
            print("Something is wrong....")

        return self.rooms

