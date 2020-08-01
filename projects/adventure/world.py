from room import Room


class World:
    def __init__(self):
        self.starting_room = None
        self.rooms = {}
        self.room_grid = []
        self.grid_size = 0

    def load_graph(self, room_graph):
        num_rooms = len(room_graph)
        grid_size = 1
        for i in range(0, num_rooms):
            x = room_graph[i][0][0]
            y = room_graph[i][0][1]
            grid_size = max(grid_size, x, y)
            self.rooms[i] = Room(f"Room {i}", f"({x}, {y})", i, x, y)
        self.room_grid = []
        grid_size += 1
        self.grid_size = grid_size
        for i in range(0, grid_size):
            self.room_grid.append([None] * grid_size)
        for room_id in room_graph:
            room = self.rooms[room_id]
            exits = room_graph[room_id][1]
            self.room_grid[room.x][room.y] = room
            if 'n' in exits:
                room.connect_rooms('n', self.rooms[exits['n']])
            if 's' in exits:
                room.connect_rooms('s', self.rooms[exits['s']])
            if 'e' in exits:
                room.connect_rooms('e', self.rooms[exits['e']])
            if 'w' in exits:
                room.connect_rooms('w', self.rooms[exits['w']])
        self.starting_room = self.rooms[0]

    def print_rooms(self):
        rotated_room_grid = []
        for i in range(0, len(self.room_grid)):
            rotated_room_grid.append([None] * len(self.room_grid))
        for i in range(len(self.room_grid)):
            for j in range(len(self.room_grid[0])):
                current = self.room_grid[i][j]
                rotated_room_grid[len(self.room_grid[0]) - j - 1][i] = current
        print("#####")
        str = ""
        for row in rotated_room_grid:
            all_null = True
            for room in row:
                if room is not None:
                    all_null = False
                    break
            if all_null:
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
