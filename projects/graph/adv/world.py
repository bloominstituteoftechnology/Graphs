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
    def generateRooms(self, numRooms):
        self.rooms = {}  # {i: [room, coordinate]}

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # Create n rooms
        coordinate = [0,0]
        occupied_coord = []
        for i in range(0, numRooms):
            occupied_coord.append(str(coordinate))
            self.rooms[i] = { 'room': Room(f"Room {i}", "You are standing in an empty room."), 'coord': coordinate.copy() }
            while str(coordinate) in occupied_coord:
                coordinate[round(random.random())] += 1 if round(random.random()) else -1

        for room_id in self.rooms:
            for c_room_id in self.rooms:
                if self.rooms[room_id]['coord'][1]-self.rooms[c_room_id]['coord'][1] == 0:  #if on the same  y axis
                    if self.rooms[room_id]['coord'][0]-self.rooms[c_room_id]['coord'][0] == 1:  #to the east 643703
                        self.rooms[room_id]['room'].connectRooms('w', self.rooms[c_room_id]['room'])

                    elif self.rooms[room_id]['coord'][0]-self.rooms[c_room_id]['coord'][0] == -1:  #to the west 643703
                        self.rooms[room_id]['room'].connectRooms('e', self.rooms[c_room_id]['room'])

                elif  self.rooms[room_id]['coord'][0]-self.rooms[c_room_id]['coord'][0] == 0: #if on the same x axis
                    if self.rooms[room_id]['coord'][1]-self.rooms[c_room_id]['coord'][1] == 1:  #to the south 643703
                        self.rooms[room_id]['room'].connectRooms('s', self.rooms[c_room_id]['room'])

                    elif self.rooms[room_id]['coord'][1]-self.rooms[c_room_id]['coord'][1] == -1:  #to the north 643703
                        self.rooms[room_id]['room'].connectRooms('n', self.rooms[c_room_id]['room'])

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        return self.rooms


world = World()

world.generateRooms(10)








