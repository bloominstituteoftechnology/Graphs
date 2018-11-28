from room import Room
import random

class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
    # checks if room is empty
    def getRandomDirection(self, room):
        dirs = []
        # if there is no room to the north
        # then adding a room to the north is an option
        if room.n_to is None:
            dirs.append("n")
        # if there is no room to the south
        # then adding a room to the south is an option
        if room.s_to is None:
            dirs.append("s")
        # if there is no room to the west
        # then adding a room to the west is an option    
        if room.w_to is None:
            dirs.append("w")
        # if there is no room to the east
        # then adding a room to the east is an option
        if room.e_to is None:
            dirs.append("e")
        # changes/shuffles the order of the dirs array
        # that has the possible directions you can connect to
        random.shuffle(dirs)
        # if you have options to chose from in the dirs array
        if len(dirs) > 0:
            # return the first option in the array
            return dirs[0]
        else:
            # else return that you have no options
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

    ####
    # MODIFY THIS CODE
    ####
    def generateRooms(self, numRooms):
        self.rooms = {}

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # Create n rooms
        for i in range(0, numRooms):
            # Create n rooms.
            self.rooms[i] = Room(f"Room {i}", "You are standing in an empty room.")

        # Hard-code a single room connection.
        # You should replace this with procedural connection code.
        if numRooms > 1:
            self.rooms[0].connectRooms("n", self.rooms[1])

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        return self.rooms




