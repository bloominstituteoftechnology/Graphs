from room import Room
import random


class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}

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

    ####
    # MODIFY THIS CODE
    ####
    
    def get_random_direction(self, room):
        paths = []
        if room.n_to is None:
            paths.append('n')
        if room.e_to is None:
            paths.append('e')
        if room.s_to is None:
            paths.append('s')
        if room.w_to is None:
            paths.append('w')
        random.shuffle(paths)
        if len(paths) > 0:
            return paths[0]
        else:
            return None

    def generateRooms(self, numRooms):
        self.rooms = {}
        self.x_counter = 0
        self.y_counter = 0
        self.avoid_list = set()

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # Create n rooms
        for i in range(0, numRooms):
            # Create n rooms.
            self.rooms[i] = Room(f"Room {i}", f"You are standing in an empty room {i}.")
            if i > 0:
                path = self.get_random_direction(self.rooms[i - 1])
                if path is not None:
                    if path == 'n':
                        self.y_counter += 1
                    elif path == 's':
                        self.y_counter -= 1
                    elif path == 'e':
                        self.x_counter += 1
                    elif path == 'w':
                        self.x_counter -= 1

                    if (self.x_counter, self.y_counter) not in self.avoid_list:
                        self.rooms[i - 1]. connectRooms(path, self.rooms[i])
                        self.avoid_list.add((self.x_counter, self.y_counter))
                        print(path, (self.x_counter, self.y_counter), self.avoid_list)
                    else:
                        print(
                            "COLLISION", 
                            path, 
                            (self.x_counter, self.y_counter), 
                            self.avoid_list
                        )

        # Hard-code a single room connection.
        # You should replace this with procedural connection code.
        if numRooms > 1:
            self.rooms[0].connectRooms("n", self.rooms[1])

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        return self.rooms





