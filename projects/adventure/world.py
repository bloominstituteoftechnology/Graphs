from room import Room
import random
import math

class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.roomGrid = []
        self.gridSize = 0
    def loadGraph(self, roomGraph):
        numRooms = len(roomGraph)
        rooms = [None] * numRooms
        gridSize = 1
        for i in range(0, numRooms):
            x = roomGraph[i][0][0]
            gridSize = max(gridSize, roomGraph[i][0][0], roomGraph[i][0][1])
            self.rooms[i] = Room(f"Room {i}", f"({roomGraph[i][0][0]},{roomGraph[i][0][1]})",i, roomGraph[i][0][0], roomGraph[i][0][1])
        self.roomGrid = []
        gridSize += 1
        self.gridSize = gridSize
        for i in range(0, gridSize):
            self.roomGrid.append([None] * gridSize)
        for roomID in roomGraph:
            room = self.rooms[roomID]
            self.roomGrid[room.x][room.y] = room
            if 'n' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms('n', self.rooms[roomGraph[roomID][1]['n']])
            if 's' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms('s', self.rooms[roomGraph[roomID][1]['s']])
            if 'e' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms('e', self.rooms[roomGraph[roomID][1]['e']])
            if 'w' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms('w', self.rooms[roomGraph[roomID][1]['w']])
        self.startingRoom = self.rooms[0]



