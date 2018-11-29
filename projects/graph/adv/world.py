import random
from room import Room
from item import Item

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
        self.coords_list = []
        graph = Graph()

        if numRooms < 1:
            print("Must create at least 1 room")
            return None

        self.rooms[0] = Room(f"Room 0", "You are standing in an empty room.")
        graph.add_vertex(0)
        self.rooms[0].coord = [0, 0]
        self.coords_list.append([0, 0])

        # Create n rooms
        i = 1
        while i < numRooms:
            dir = self.rooms[i - 1].get_valid_random_dir()
            new_coord = None

            while dir is not None:
                new_coord = self._try_add_coord(dir)
                if new_coord is not None:
                    break
                else:
                    self.rooms[i - 1].valid_dirs.remove(dir)
                    dir = self.rooms[i - 1].get_valid_random_dir()

            if dir is None:
                curr_coord = self.rooms[i - 1].coord
                prev_coord = self.rooms[i - 2].coord
                if curr_coord[0] > prev_coord[0]:
                    self.rooms[i - 2].valid_dirs.remove("e")
                    self.coords_list.pop()
                elif curr_coord[0] < prev_coord[0]:
                    self.rooms[i - 2].valid_dirs.remove("w")
                    self.coords_list.pop()
                elif curr_coord[1] > prev_coord[1]:
                    self.rooms[i - 2].valid_dirs.remove("n")
                    self.coords_list.pop()
                elif curr_coord[1] < prev_coord[1]:
                    self.rooms[i - 2].valid_dirs.remove("s")
                    self.coords_list.pop()
                i -= 1
                continue

            new_room = Room(f"Room {i}", "You are standing in an empty room.")
            graph.add_vertex(i)
            self.rooms[i] = new_room
            self.rooms[i].coord = new_coord
            self.rooms[i - 1].connectRooms(dir, self.rooms[i])
            graph.add_edge(i - 1, i)
            i += 1

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        # Connect all adjacent rooms to one another
        self._connect_all_nodes(graph)

        # Add treasure to random room
        random_room = random.randint(1, 100)
        treasure = Item("Treasure", "This is a treasure")
        self.rooms[random_room].addItem(treasure)

        all_nodes_connected = self._check_bft_and_lengths(graph, numRooms)

        if all_nodes_connected is True:
            return self.rooms
        else:
            print('NOT ALL NODES CONNECTED PROPERLY')

    def _connect_all_nodes(self, graph):
        for first_room in self.rooms:
            first_room_x = self.rooms[first_room].coord[0]
            first_room_y = self.rooms[first_room].coord[1]
            for second_room in self.rooms:
                second_room_x = self.rooms[second_room].coord[0]
                second_room_y = self.rooms[second_room].coord[1]
                if first_room_x == second_room_x and first_room_y == second_room_y + 1:
                    if "s" in self.rooms[first_room].valid_dirs:
                        self.rooms[first_room].valid_dirs.remove("s")
                        self.rooms[first_room].connectRooms("s", self.rooms[second_room])
                        graph.add_edge(first_room, second_room)
                elif first_room_x == second_room_x and first_room_y == second_room_y - 1:
                    if "n" in self.rooms[first_room].valid_dirs:
                        self.rooms[first_room].valid_dirs.remove("n")
                        self.rooms[first_room].connectRooms("n", self.rooms[second_room])
                        graph.add_edge(first_room, second_room)
                elif first_room_y == second_room_y and first_room_x == second_room_x + 1:
                    if "w" in self.rooms[first_room].valid_dirs:
                        self.rooms[first_room].valid_dirs.remove("w")
                        self.rooms[first_room].connectRooms("w", self.rooms[second_room])
                        graph.add_edge(first_room, second_room)
                elif first_room_y == second_room_y and first_room_x == second_room_x - 1:
                    if "e" in self.rooms[first_room].valid_dirs:
                        self.rooms[first_room].valid_dirs.remove("e")
                        self.rooms[first_room].connectRooms("e", self.rooms[second_room])
                        graph.add_edge(first_room, second_room)

    def _try_add_coord(self, dir):
        last_coord = self.coords_list[-1]
        if dir is "n":
            new_coord = [last_coord[0], last_coord[1] + 1]
        elif dir is "s":
            new_coord = [last_coord[0], last_coord[1] - 1]
        elif dir is "w":
            new_coord = [last_coord[0] - 1, last_coord[1]]
        elif dir is "e":
            new_coord = [last_coord[0] + 1, last_coord[1]]
        if new_coord in self.coords_list:
            return None
        else:
            self.coords_list.append(new_coord)
            return new_coord

    def _check_bft_and_lengths(self, graph, numRooms):
        traversal_list = graph.bft(0)
        traversal_list_len = len(traversal_list)
        coords_list_len = len(self.coords_list)
        if traversal_list_len is numRooms and traversal_list_len is coords_list_len:
            return True
        else:
            return False

    def printMap(self):
        coordinates = list(self.coords_list)
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
