from room import Room

import sys
sys.path.insert(0, '../src')
from graph import Graph

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
        self.rooms = {}
        graph = Graph()

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        self.rooms[0] = Room(f"Room 0", "You are standing in an empty room.")
        graph.add_vertex(0)

        # Create n rooms
        for i in range(1, numRooms):
            new_room = Room(f"Room {i}", "You are standing in an empty room.")
            graph.add_vertex(i)
            self.rooms[i] = new_room
            dir = self.rooms[i - 1].get_valid_random_dir()
            if dir is None:
                print('dir was none')
            self.rooms[i - 1].connectRooms(dir, self.rooms[i])
            graph.add_edge(i - 1, i)

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        all_nodes_connected = self.check_bft(graph, numRooms)

        if all_nodes_connected is True:
            return self.rooms
        else:
            print('Not all nodes connected')

    def check_bft(self, graph, numRooms):
        traversal_list = graph.bft(0)
        if len(traversal_list) is numRooms:
            return True
        else:
            return False




