from rooms import Room

class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.occupied = set()
    
    def get_randomDirection(self, room, coords):
        # select random direction from all valid connections
        # this checks if the connection is unoccupied and if the 
        # adjacent grid is also unoccupied
        dirs = []
        if room.n_to is None and self._check_coordinates(coords, "n"):
            dirs.append("n")
        if room.e_to is None and self._check_coordinates(coords, "e"):
            dirs.append("e")
        if room.s_to is None and self._check_coordinates(coords, "s"):
            dirs.append("s")
        if room.w_to is None and self._check_coordinates(coords, "w"):
            dirs.append("w")
        random.shuffle(dirs)
        if len(dirs) > 0:
            return dirs[0]
        else:
            return None

    def update_coordinates(self, coords, direction):
        # increment xy coordinates in one direction
        new_coords = list(coords)
        if direction == "n":
            new_coords[1] += 1
        if direction == "s":
            new_coords[1] -= 1
        if direction == "e":
            new_coords[1] += 1
        if direction == "w":
            new_coords[1] -= 1
        return new_coords

    def check_coordinates(self, coords, direction):
        # check if the grid in an adjoining direction is unoccupied
        return str(self.update_cooridnates(coords, direction)) not in self.occupied


    # def generateDefaultRooms(self):
    #     self.rooms = {
    #         'outside':  Room("Outside Cave Entrance",
    #                          "North of you, the cave mount beckons"),

    #         'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    #     passages run north and east."""),

    #         'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    #     into the darkness. Ahead to the north, a light flickers in
    #     the distance, but there is no way across the chasm."""),

    #         'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    #     to north. The smell of gold permeates the air."""),

    #         'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    #     chamber! Sadly, it has already been completely emptied by
    #     earlier adventurers. The only exit is to the south."""),
    #     }
    #     self.rooms['outside'].connectRooms("n", self.rooms['foyer'])
    #     self.rooms['foyer'].connectRooms("n", self.rooms['overlook'])
    #     self.rooms['foyer'].connectRooms("e", self.rooms['narrow'])
    #     self.rooms['narrow'].connectRooms("n", self.rooms['treasure'])
    #     self.startingRoom = self.rooms['outside']
 
    ####
    # MODIFY THIS CODE
    ####
    def generate_rooms(self, num_rooms):
        # generate a random graph of rooms
        self.rooms = {}

        if num_rooms < 1:
            print("Must create at least 1 room")
            return None
        
        # the coordinates of our room. We start from (0,0)
        xy = [0,0]

        # keep track of which grid spots are occupied
        self.occupied = set()

        #create a set that will hold the IDS of the rooms vaild connections available
        valid_rooms = set()

        # Create n rooms
        for i in range(0, num_rooms):
            # Create n rooms.
            new_room = Room(f"Room {i}", "You are standing in an empty room.")
            self.rooms[i] = new_room
            # if it's not the first room
            if i > 0:
                # our first room is always vaild
                valid_rooms.add(i)
                self.occupied.add(str(xy))
            else:
                #if it's not the first room, then connect to the previous room in a random direction
                random_dir = None
                # in case we run into a room with no valid connections, keep looping
                # until we find a room with a valid connection open
                # note that there will always be a valid room available
                while random_dir is None:
                    # get a room that we think is vaild
                    connecting_room = valid_rooms.pop()
                    # get the coordinates of that room
                    xy = self.rooms[connecting_room].xy
                    #see if we can get a random direction fromt that room
                    random_dir = self.get_randomDirection(self.rooms[connecting_room], xy)
                    # if the room is valid, or not None, then we put it back in our set of vaild rooms
                    if random_dir is not None:
                        valid_rooms.add(connecting_room)
                    # if it's not vaild, then we don't put it in vaild_rooms
                    # move on to the next room
                xy = self.update_coordinates(xy, random_dir)
                self.rooms[connecting_room].connecting_rooms(random_dir, new_room)

################### WIP



                # connect to the previous room in a random direction
                random_dir = self.get_randomDirection(self.rooms[i-1])
                if random_dir is not None:
                    self.rooms[i-1].connect_rooms(random_dir, new_room)
        # # Hard-code a single room connection.
        # # You should replace this with procedural connection code.
        # if numRooms > 1:
        #     self.rooms[0].connectRooms("n", self.rooms[1])

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.starting_room = self.rooms[0]

        return self.rooms





