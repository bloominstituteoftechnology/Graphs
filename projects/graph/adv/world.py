# from room import Room
# # working on this// glitch out 

# class World:
#     def __init__(self):
#         self.startingRoom = None
#         self.rooms = {}

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

#     ####
#     # MODIFY THIS CODE
#     ####
#     def generateRooms(self, numRooms):
#         self.rooms = {}

#         if numRooms < 1:
#             print("Must create at least 1 room")
#             return None

#         # Create n rooms
#         for i in range(0, numRooms):
#             # Create n rooms.
#             self.rooms[i] = Room(f"Room {i}", "You are standing in an empty room.")

#         # Hard-code a single room connection.
#         # You should replace this with procedural connection code.
#         if numRooms > 1:
#             self.rooms[0].connectRooms("n", self.rooms[1])

#         # Set the starting room to the first room. Change this if you want a new starting room.
#         self.startingRoom = self.rooms[0]

#         return self.rooms



from room import Room
import random


class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}

    
    def randomDirection(self, room):
        dirs = []
         
        if room.n_to is None: 
            dirs.append('n')
        if room.s_to is None: 
            dirs.append('s')
        if room.e_to is None: 
            dirs.append('e')
        if room.w_to is None: 
            dirs.append('w')
        random.shuffle(dirs)
        return dirs[0]   

    def updateCoordinates(self, coords, dir): 
        if dir == "n":
            coords[0] += 1
        if dir == "s":
            coords[0] -= 1
        if dir == "e":
            coords[1] += 1
        if dir == "w":
            coords[1] -=1 
        updated_coords = coords
        return updated_coords    
       
 
    ####
    # MODIFY THIS CODE
    ####
    def generateRooms(self, numRooms):
        self.rooms = {}

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        occupied = set()
        xy = [0,0]

        # Create n rooms
        # for i in range(0, numRooms):
        #     if i == 0:
        #         new_room = Room(f"Room {i}", "You are alone in an empty room look around for clues.", xy)
            
        #         self.rooms[i] = new_room
            
        #     if i > 0:
                 

        #         random_dir = self.randomDirection(self.rooms[i-1])
        #         new_coords = str(self.updateCoordinates(xy, random_dir))
        #         new_room = Room(f"Room {i}", "You are standing in an empty room pondering of your life.", new_coords)
            
        #         self.rooms[i] = new_room
        #         if random_dir is not None and new_coords not in occupied:
        #             self.rooms[i-1].connectRooms(random_dir, new_room)
        #             occupied.add(str(new_coords))
            
        #     for i in occupied:
        #         for j in occupied:
        #             count = 0
        #             if i == j:
        #                 count+=1
        #                 if count > 1:
        #                     print(f"{i} equaled {j} {count} times")
        # print(f'start {occupied}')

        # Hard-code a single room connection.
        # You should replace this with procedural connection code.
        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        return self.rooms



