from room import Room
import random
import math

class World:
  def __init__(self):
    self.startingRoom = None
    self.rooms = {}
    self.roomGrid = []
    self.gridSize = 0

  # Example: 
  # roomGraph={0: [(3, 5), {'n': 1}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}]}
  
  def loadGraph(self, roomGraph):
    numRooms = len(roomGraph) # 3
    rooms = [None] * numRooms # [None, None, None]
    gridSize = 1

    for i in range(0, numRooms):
      x = roomGraph[i][0][0]
      gridSize = max(gridSize, roomGraph[i][0][0], roomGraph[i][0][1])
      self.rooms[i] = Room(f"Room {i}", f"({roomGraph[i][0][0]},{roomGraph[i][0][1]})", i, roomGraph[i][0][0], roomGraph[i][0][1])

      # 1st Iteration 
        # x = roomGraph[0][0][0] = 3
        # gridSize = max(1, 3, 5) = 5
        # self.rooms[0] = Room(f"Room {0}", f"(3, 5)", 0, 3, 5)
      
      # 2nd Iteration
        # x = roomGraph[1][0][0] = 3
        # gridSize = max(5, 3, 6) = 6
        # self.rooms[1] = Room(f"Room {1}", f"(3, 6)", 1, 3, 6)

      # Third Iteration
        # x = roomGraph[2][0][0] = 3
        # gridSize = max(6, 3, 7) = 7
        # self.rooms[2] = Room(f"Room {2}", f"(3, 7)", 2, 3, 7)

    self.roomGrid = []
    gridSize += 1 # 8
    self.gridSize = gridSize # 8

    for i in range(0, gridSize):
      self.roomGrid.append([None] * gridSize)
      # After 8 Iterations - roomGrid - [
      # [None, None, None, None, None, None, None, None],
      # [None, None, None, None, None, None, None, None],
      # [None, None, None, None, None, None, None, None],
      # [None, None, None, None, None, None, None, None],
      # [None, None, None, None, None, None, None, None],
      # [None, None, None, None, None, None, None, None],
      # [None, None, None, None, None, None, None, None],
      # [None, None, None, None, None, None, None, None]]
    for roomID in roomGraph:
      room = self.rooms[roomID] 
      # 1st Iteration - self.rooms[0]
      # Snd Iteration - self.rooms[1]
      self.roomGrid[room.x][room.y] = room
      # 1st Iteration
      # self.roomGrid[3][5] = Room(0)
      # roomGraph[0][1] = {'n': 1}
      # self.rooms[0].connectRooms('n', Room(1))

      # 2nd Iteration
      # self.roomGrid[3][6] = Room(1)
      # roomGraph[1][1] = {'s': 0, 'n': 2}
      # self.room[1].connectRooms('s', Room(0))
      # self.room[1].connectRooms('n', Room(2))

      # 3rd Iteration
      # self.roomGrid[3][7] = Room(2)
      # roomGraph[2][1] = {'s': 1}
      # self.room[2].connectRooms('s', Room(1))
  
      if 'n' in roomGraph[roomID][1]:
        self.rooms[roomID].connectRooms('n', self.rooms[roomGraph[roomID][1]['n']])
      if 's' in roomGraph[roomID][1]:
        self.rooms[roomID].connectRooms('s', self.rooms[roomGraph[roomID][1]['s']])
      if 'e' in roomGraph[roomID][1]:
        self.rooms[roomID].connectRooms('e', self.rooms[roomGraph[roomID][1]['e']])
      if 'w' in roomGraph[roomID][1]:
        self.rooms[roomID].connectRooms('w', self.rooms[roomGraph[roomID][1]['w']])
    
    # After 3 Iterations
    # roomGrid = [
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, Room(0), Room(1), Room(2)],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None]]

    self.startingRoom = self.rooms[0] # Room(0)

  def printRooms(self):
    rotatedRoomGrid = []

    for i in range(0, len(self.roomGrid)):
      rotatedRoomGrid.append([None] * len(self.roomGrid))
       # After 8 Iterations
       # rotatedRoomGrid = [
       # [None, None, None, None, None, None, None, None],
       # [None, None, None, None, None, None, None, None],
       # [None, None, None, None, None, None, None, None],
       # [None, None, None, None, None, None, None, None],
       # [None, None, None, None, None, None, None, None],
       # [None, None, None, None, None, None, None, None],
       # [None, None, None, None, None, None, None, None],
       # [None, None, None, None, None, None, None, None]]
    for i in range(len(self.roomGrid)):
      for j in range(len(self.roomGrid[0])):
        rotatedRoomGrid[len(self.roomGrid[0]) - j - 1][i] = self.roomGrid[i][j]
        # 4th Iteration - the fourth row in roomGrid only has rooms
          # rotatedRoomGrid[7][0] = self.roomGrid[3][0]
          # rotatedRoomGrid[6][0] = self.roomGrid[3][1]
          # rotatedRoomGrid[5][0] = self.roomGrid[3][2]
          # rotatedRoomGrid[4][0] = self.roomGrid[3][3]
          # rotatedRoomGrid[3][0] = self.roomGrid[3][4]
          # rotatedRoomGrid[2][0] = self.roomGrid[3][5]
          # rotatedRoomGrid[1][0] = self.roomGrid[3][6]
          # rotatedRoomGrid[0][0] = self.roomGrid[3][7]

    # After 8 Iterations
    # rotatedRoomGrid = [
    # [Room(2), None, None, None, None, None, None, None],
    # [Room(1), None, None, None, None, None, None, None],
    # [Room(0), None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None],
    # [None, None, None, None, None, None, None, None]]

    print("#####")
    str = ""
    
    for row in rotatedRoomGrid:
      allNull = True
      # Only row 1, 2, and 3 has rooms
      for room in row:
        if room is not None:
          allNull = False
          break

      if allNull:
        continue
      
      # PRINT NORTH CONNECTION ROW
      str += "#"

      for room in row:
        if room is not None and room.n_to is not None:
          str += "  |  "
        else:
          str += "     "
      
      str += "#\n"

      # PRINT ROOM ROW
      str += "#"

      for room in row:
        if room is not None and room.w_to is not None:
          str += "-"
        else:
          str += " "
        
        if room is not None:
          str += f"{room.id}".zfill(3)
        else:
          str += "   "
        
        if room is not None and room.e_to is not None:
          str += "-"
        else:
          str += " "
        
      str += "#\n"
        
      # PRINT SOUTH CONNECTION ROW
      str += "#"

      for room in row:
        if room is not None and room.s_to is not None:
          str += "  |  "
        else:
          str += "     "

      str += "#\n"

    print(str)
    print("#####")