from room import Room
import random

class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.avail_rm_dir = []
        self.rm_coords = []

    def getRandomRoom(self):
        if len(self.avail_rm_dir) > 0:
            random_rooms = list(self.rooms.values())
            random.shuffle(random_rooms)
            # print(random_rooms[0].coordinates)
            return random_rooms[0]
        else: 
            return None

    def getRandomDirection(self):
        random_room = self.getRandomRoom()
        available_dir = []
        if random_room.n_to is None:
            available_dir.append("n")
        if random_room.s_to is None:
            available_dir.append("s")
        if random_room.w_to is None:
            available_dir.append("w")
        if random_room.e_to is None:
            available_dir.append("e")
        random.shuffle(available_dir)
        # print(random_room.coordinates, available_dir)
        if len(available_dir) > 0:
            # print(random_room.coordinates, available_dir[0])
            return (random_room, available_dir[0])
        else:
            return None
    
    # check if the randomly-picked available room and direction allows connection to the new room without overlaping any existing rooms
    def checkNewRoomCoords(self, random_room, direction):
        potential_coord = tuple()
        random_room_x_coord = random_room.coordinates[0]  
        random_room_y_coord = random_room.coordinates[1] 
        # using the available direction, determine the potential coordinates of the new room  
        if direction == 'n':
            potential_coord = (random_room_x_coord, random_room_y_coord + 1)
        if direction == 's':
            potential_coord = (random_room_x_coord, random_room_y_coord - 1)
        if direction == 'e':
            potential_coord = (random_room_x_coord + 1, random_room_y_coord)
        if direction == 'w':
            potential_coord = (random_room_x_coord - 1, random_room_y_coord)
        # determine if potential coordinates had already existed
        if potential_coord not in self.rm_coords:
            return potential_coord
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

    def _updateCoordinates(self, coords, dir):
        new_coords = list(coords)
        if dir == "n":
            new_coords[1] += 1
        if dir == "s":
            new_coords[1] -= 1
        if dir == "e":
            new_coords[0] += 1
        if dir == "w":
            new_coords[0] -= 1

    ####
    # MODIFY THIS CODE
    ####
    def createRandomRooms(self, numRooms):
        self.rooms = {}

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # Create n rooms
        for i in range(0, numRooms):
            # Create n rooms.
            new_room = Room(f"Room {i}", "You are standing in an empty room.", i, (0,0))
            
            self.rooms[i] = new_room
            # if first room, add new room's available directions to avail_rm_dirs
            if i == 0:
                # self.startingRoom = new_room
                self.avail_rm_dir.append((new_room, "n"))
                self.avail_rm_dir.append((new_room, "s"))
                self.avail_rm_dir.append((new_room, "e"))
                self.avail_rm_dir.append((new_room, "w"))
            # If it's not the first room....
            if i > 0:
                potential_coord = None
                
                while potential_coord == None :
                    # find a random room and random direction that can potentially connect to the new room
                    random_rm_tuple = self.getRandomDirection()
                    if random_rm_tuple:
                        random_rm = random_rm_tuple[0]
                        random_rm_dir = random_rm_tuple[1]
                        # determine the potential coordinates derived from the random_rm_tuple
                        potential_coord = self.checkNewRoomCoords(random_rm, random_rm_dir)
                        new_room.coordinates = potential_coord
                # connect random_rm and the new room    
                self.rooms[random_rm.id].connectRooms(random_rm_dir, new_room)
                # remove random_rm_tuple from the avail_rm_dir list
                for rm_dir_tuple in self.avail_rm_dir:
                    if rm_dir_tuple[0].coordinates == random_rm.coordinates:
                        self.avail_rm_dir.remove(random_rm_tuple)
                        break
                # print(self.avail_rm_dir)
                if new_room.n_to is None:
                    self.avail_rm_dir.append((new_room, "n"))
                if new_room.s_to is None:
                    self.avail_rm_dir.append((new_room, "s"))
                if new_room.w_to is None:
                    self.avail_rm_dir.append((new_room, "w"))
                if new_room.e_to is None:
                    self.avail_rm_dir.append((new_room, "e")) 
            self.rm_coords.append(new_room.coordinates)
            print(new_room.coordinates)
                    

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        return self.rooms   