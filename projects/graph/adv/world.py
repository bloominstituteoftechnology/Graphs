from room import Room
from item import Treasure
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

    def findItem(self, item):
        start = 0
        queue = [self.rooms[0]['room']]
        print (self.rooms)
        visited = []
        # directions = [self.n_to, self.e_to, self.s_to, self.w_to]
        while queue:
            current_room = queue[0]
            if current_room.n_to and current_room.n_to not in queue and current_room.n_to not in visited: queue.append(current_room.n_to)
            if current_room.e_to and current_room.e_to not in queue and current_room.e_to not in visited: queue.append(current_room.e_to)
            if current_room.s_to and current_room.s_to not in queue and current_room.s_to not in visited: queue.append(current_room.s_to)
            if current_room.w_to and current_room.w_to not in queue and current_room.w_to not in visited: queue.append(current_room.w_to)
            if item in current_room.items:
                print ('queue:', queue)
                print ('visited:', visited)
                return "You found it!"
            else:
                visited.append(queue.pop(0))
        return 'Not here'



    ####
    # MODIFY THIS CODE
    ####
    def generateRooms(self, numRooms):
        self.rooms = {}  # {i: {'room': Room, 'coord': coordinate} }

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        # Create n rooms
        coordinate = [0,0]
        occupied_coord = set()

        for i in range(0, numRooms):
            occupied_coord.add(str(coordinate))
            self.rooms[i] = { 'room': Room(f"Room {i}", "You are standing in an empty room."), 'coord': coordinate.copy() }
            while str(coordinate) in occupied_coord:
                coordinate[round(random.random())] += 1 if round(random.random()) else -1
                # print ('coordinate:', coordinate)
        
        # print ('Rooms:', self.rooms)
        # self.rooms = {}  # {i: {'room': Room, 'coord': [0,3]} }

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
chest = Treasure('Treasure Chest - [chest]' , """An old pirate relic, overflowing with 
    bullions and gems""", 'chest',  100)

n = 20

world.generateRooms(n)

rand_room = round(random.random()*n-1)
world.rooms[rand_room]['room'].addItem(chest)
print ('Room:', world.rooms[rand_room]['room'])
print ('Items:', world.rooms[rand_room]['room'].items)

print (world.findItem(chest))

