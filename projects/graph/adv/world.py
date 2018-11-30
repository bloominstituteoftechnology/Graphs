from room import Room
import random
from item import Item

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
    
    def random_treasure_drop(self, item):
        room_list = list(self.rooms.values())
        random.shuffle(room_list)
        room_list[0].addItem(item)
        return room_list[0]

    def find_path_to_item(self, target_item):
        queue = [[self.startingRoom]]
        visited = []
        # helper method to check if room is not in the visited list, add to the list, and to the end of the path argument then add the appended path to the end of queue
        def add_room_if_new(path, room):
            if room not in visited:
                new_path = list(path)
                new_path.append(room)
                queue.append(new_path)
                visited.append(room)
        while len(queue) > 0:
            # if current_room has the target_item, return current_path
            current_path = queue.pop(0)
          
            temp_list = []
            for room in current_path:
                coord_list = list(room.xy)
                #print(coord_list)
                temp_list.append(coord_list)         
            print("Current path coordinates: ", temp_list)
            
            current_room = current_path[-1]
            if target_item in current_room.items:
                return current_path
          
            if current_room not in visited:
                if current_room.n_to is not None:
                    add_room_if_new(current_path, current_room.n_to)
                if current_room.s_to is not None:
                    add_room_if_new(current_path, current_room.s_to)
                if current_room.w_to is not None:
                    add_room_if_new(current_path, current_room.w_to)
                if current_room.e_to is not None:
                    add_room_if_new(current_path, current_room.e_to)
                
        return None
# from room import Room
# import random

# class World:
#     def __init__(self):
#         self.startingRoom = None
#         self.rooms = {}
#         self.avail_rm_dir = []
#         self.rm_coords = []

#     def getRandomRoom(self):
#         if len(self.avail_rm_dir) > 0:
#             random_rooms = list(self.rooms.values())
#             random.shuffle(random_rooms)
#             # print(random_rooms[0].coordinates)
#             return random_rooms[0]
#         else: 
#             return None

#     def getRandomDirection(self):
#         random_room = self.getRandomRoom()
#         available_dir = []
#         if random_room.n_to is None:
#             available_dir.append("n")
#         if random_room.s_to is None:
#             available_dir.append("s")
#         if random_room.w_to is None:
#             available_dir.append("w")
#         if random_room.e_to is None:
#             available_dir.append("e")
#         random.shuffle(available_dir)
#         # print(random_room.coordinates, available_dir)
#         if len(available_dir) > 0:
#             # print(random_room.coordinates, available_dir[0])
#             return (random_room, available_dir[0])
#         else:
#             return None
    
#     # check if the randomly-picked available room and direction allows connection to the new room without overlaping any existing rooms
#     def checkNewRoomCoords(self, random_room, direction):
#         potential_coord = tuple()
#         random_room_x_coord = random_room.coordinates[0]  
#         random_room_y_coord = random_room.coordinates[1] 
#         # using the available direction, determine the potential coordinates of the new room  
#         if direction == 'n':
#             potential_coord = (random_room_x_coord, random_room_y_coord + 1)
#         if direction == 's':
#             potential_coord = (random_room_x_coord, random_room_y_coord - 1)
#         if direction == 'e':
#             potential_coord = (random_room_x_coord + 1, random_room_y_coord)
#         if direction == 'w':
#             potential_coord = (random_room_x_coord - 1, random_room_y_coord)
#         # determine if potential coordinates had already existed
#         if potential_coord not in self.rm_coords:
#             return potential_coord
#         else:
#             return None
            

#     def generateDefaultRooms(self):
#         self.rooms = {
#             'outside':  Room("Outside Cave Entrance",
#                              "North of you, the cave mount beckons"),

#             'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
#         passages run north and east."""),

#             'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
#         into the darkness. Ahead to the north, a light flickers in
#         the distance, but there is no way across the chasm."""),

#             'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
#         to north. The smell of gold permeates the air."""),

#             'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
#         chamber! Sadly, it has already been completely emptied by
#         earlier adventurers. The only exit is to the south."""),
#         }
#         self.rooms['outside'].connectRooms("n", self.rooms['foyer'])
#         self.rooms['foyer'].connectRooms("n", self.rooms['overlook'])
#         self.rooms['foyer'].connectRooms("e", self.rooms['narrow'])
#         self.rooms['narrow'].connectRooms("n", self.rooms['treasure'])
#         self.startingRoom = self.rooms['outside']

#     def _updateCoordinates(self, coords, dir):
#         new_coords = list(coords)
#         if dir == "n":
#             new_coords[1] += 1
#         if dir == "s":
#             new_coords[1] -= 1
#         if dir == "e":
#             new_coords[0] += 1
#         if dir == "w":
#             new_coords[0] -= 1

#     ####
#     # MODIFY THIS CODE
#     ####
#     def createRandomRooms(self, numRooms):
#         self.rooms = {}

#         if numRooms < 1:
#             print("Must create at least 1 room")
#             return None

#         # Create n rooms
#         for i in range(0, numRooms):
#             # Create n rooms.
#             new_room = Room(f"Room {i}", "You are standing in an empty room.", i, (0,0))
            
#             self.rooms[i] = new_room
#             # if first room, add new room's available directions to avail_rm_dirs
#             if i == 0:
#                 # self.startingRoom = new_room
#                 self.avail_rm_dir.append((new_room, "n"))
#                 self.avail_rm_dir.append((new_room, "s"))
#                 self.avail_rm_dir.append((new_room, "e"))
#                 self.avail_rm_dir.append((new_room, "w"))
#             # If it's not the first room....
#             if i > 0:
#                 potential_coord = None
                
#                 while potential_coord == None :
#                     # find a random room and random direction that can potentially connect to the new room
#                     random_rm_tuple = self.getRandomDirection()
#                     if random_rm_tuple:
#                         random_rm = random_rm_tuple[0]
#                         random_rm_dir = random_rm_tuple[1]
#                         # determine the potential coordinates derived from the random_rm_tuple
#                         potential_coord = self.checkNewRoomCoords(random_rm, random_rm_dir)
#                         new_room.coordinates = potential_coord
#                 # connect random_rm and the new room    
#                 self.rooms[random_rm.id].connectRooms(random_rm_dir, new_room)
#                 # remove random_rm_tuple from the avail_rm_dir list
#                 for rm_dir_tuple in self.avail_rm_dir:
#                     if rm_dir_tuple[0].coordinates == random_rm.coordinates:
#                         self.avail_rm_dir.remove(random_rm_tuple)
#                         break
#                 # print(self.avail_rm_dir)
#                 if new_room.n_to is None:
#                     self.avail_rm_dir.append((new_room, "n"))
#                 if new_room.s_to is None:
#                     self.avail_rm_dir.append((new_room, "s"))
#                 if new_room.w_to is None:
#                     self.avail_rm_dir.append((new_room, "w"))
#                 if new_room.e_to is None:
#                     self.avail_rm_dir.append((new_room, "e")) 
#             self.rm_coords.append(new_room.coordinates)
#             print(new_room.coordinates)
                    

#         # Set the starting room to the first room. Change this if you want a new starting room.
#         self.startingRoom = self.rooms[0]

#         return self.rooms   


