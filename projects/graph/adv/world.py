from room import Room
import random

class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        
    def getRandomDirection(self, room):
        dirs = []
        if room.n_to is None:
            dirs.append("n")
        if room.s_to is None:
            dirs.append("s")
        if room.w_to is None:
            dirs.append("w")
        if room.e_to is None:
            dirs.append("e") 
        random.shuffle(dirs)
        if len(dirs) > 0:
            return dirs[0]
        else:
            return None

    ####
    # MODIFY THIS CODE to generate a number of random rooms
    ####
    def generateRooms(self, numRooms):
        self.rooms = {}

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # Create n rooms
        for i in range(0, numRooms):
            # instantiate a new Room called new_room:
            new_room = Room(f"Room {i}", "You are standing in an empty room.")
            # put new_room in the world's self.rooms list
            self.rooms[i] = new_room

            if i > 0:
                # Call getRandomDirections on previous room to get it's direction
                random_dir = self.getRandomDirection(self.rooms[i-1])
                
                if random_dir is not None:
                    # Call connectRooms on previous room, passing in it's direction and the the new room
                    # e.g., if previous room has random_dir="n", place current room at e_to location from previous room
                    self.rooms[i-1].connectRooms(random_dir, new_room)
                # print(random_dir)
            print(self.rooms[i])
            print(f'To the North is Room {self.rooms[i].n_to}\nTo the East is Room {self.rooms[i].e_to}\nTo the South is Room {self.rooms[i].s_to}\nTo the West is Room {self.rooms[i].w_to}')

        # Hard-code a single room connection.
        # You should replace this with procedural connection code.
        # if numRooms > 1:
        #     self.rooms[0].connectRooms("n", self.rooms[1])

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        return self.rooms


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