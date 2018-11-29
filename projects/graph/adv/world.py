from room import Room
from item import Item
import random
import queue as queue

class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.occupied = set()

    def getRandomDirection(self, room, coords):
        dirs = []
        if room.n_to is None and self._checkCoordinates(coords, 'n'):
            dirs.append('n')
        if room.s_to is None and self._checkCoordinates(coords, 's'):
            dirs.append('s')
        if room.e_to is None and self._checkCoordinates(coords, 'e'):
            dirs.append('e')
        if room.w_to is None and self._checkCoordinates(coords, 'w'):
            dirs.append('w')
        random.shuffle(dirs)
        if len(dirs) > 0:
            return dirs[0]
        else:
            return None

    def _updateCoordinates(self, coords, direction):
        new_coords = list(coords)
        if direction == 'n':
            new_coords[1] += 1
        if direction == 's':
            new_coords[1] -= 1
        if direction == 'e':
            new_coords[0] += 1
        if direction == 'w':
            new_coords[0] -= 1
        return new_coords
    
    def _checkCoordinates(self, coords, direction):
        return str(self._updateCoordinates(coords, direction)) not in self.occupied

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

        xy = [0,0]

        self.occupied = set()

        validRooms = set()

        # Create n rooms
        for i in range(0, numRooms):
            # Create n rooms.
            # create a new room
            new_room = Room(f"Room {i}", "You are standing in an empty room.")
            # index the new room in our rooms list
            self.rooms[i] = new_room
            if i == 0:
                validRooms.add(i)
                self.occupied.add(str(xy))
            # if not starting room
            else:
                random_dir = None
            
                while random_dir is None:
                    connectingRoom = validRooms.pop()
                    xy = self.rooms[connectingRoom].xy
                    random_dir = self.getRandomDirection(self.rooms[connectingRoom], xy)
                    if random_dir is not None:
                        validRooms.add(connectingRoom)

                xy = self._updateCoordinates(xy, random_dir)
                self.rooms[connectingRoom].connectRooms(random_dir, new_room)
                self.occupied.add(str(xy))
                new_room.xy = xy
                validRooms.add(i)

        # # Hard-code a single room connection.
        # # You should replace this with procedural connection code.
        # if numRooms > 1:
        #     self.rooms[0].connectRooms("n", self.rooms[1])

        # Set the starting room to the first room. Change this if you want a new starting room.
        self.startingRoom = self.rooms[0]

        # Add treasure to a random room
        treasure = Item('Treasure', 'A golden glove with radiant jewels!')
        random_room = random.randint(0, numRooms + 1)
        self.rooms[random_room].addItem(treasure)

        if len(self.occupied) == numRooms:
            print('World successfully created!')
        else:
            print('Something went horribly, horribly wrong.')

        return self.rooms

    def traverseRooms(self, room):
        # Dept First Traversal
        stack = [self.rooms[room]]
        visited = []
        while len(stack) > 0:
            current = stack.pop()
            visited.append(current)

            paths = [current.n_to, current.s_to, current.e_to, current.w_to]

            for path in paths:
                if path and path not in visited:
                    stack.append(path)

        for v in visited:
            print(f'{v.name} => ', end='', flush=True)
            for item in v.items:
                if item.name == 'Treasure':
                    print(f'The Treasure is in {v.name}.')
        print('\n')
        return visited

    def bfSearch(self, root):
        # Breadth first traversal

        visited = []
        storage = queue.Queue()
        storage.put(self.rooms[root])

        while not storage.empty():
            current = storage.get()

            if current not in visited:
                visited.append(current)
            
            for item in current.items:
                if item.name == 'Treasure':
                    for v in visited:
                        print(f'{v.name} => ', end='')
                    
                    print('Treasure')
                    return visited
            
            paths = [current.n_to, current.s_to, current.w_to, current.e_to]

            for path in paths:
                if path not in visited and path is not None:
                    storage.put(path)
        
        for v in visited:
            print(f'{v.name} => ', end='')
        return visited

    def printMap(self):
        coordinates = [[int(i) for i in x[1:-1].split(', ')] for x in self.occupied]
        xMax = xMin = yMax = yMin = 0

        # look over the coordinates and find the max values for x and y
        # these will be the constraints of our map
        for c in coordinates:
            if c[0] > xMax:
                xMax =c[0]
            if c[0] < xMin:
                xMin = c[0]
            if c[1] > yMax:
                yMax = c[1]
            if c[1] < yMin:
                yMin = c[1]

        row = [' '] * (1 + yMax - yMin)
        grid = []
        for i in range(0, 1 + xMax - xMin):
            grid.append(list(row))
        for c in coordinates:
            if c[0] == 0 and c[1] == 0:
                grid[c[0] - xMin][c[1] - yMin] = 'S'
            else:
                grid[c[0] - xMin][c[1] - yMin] = '0'
        gridString = ''
        for row in grid:
            for room in row:
                gridString += room
            gridString += '\n'
        print(gridString)

