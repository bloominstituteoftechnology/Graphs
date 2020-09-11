from room import Room
import random
import math

class World:
    def __init__(self):
        self.starting_room = None
        self.rooms = {}
        self.room_grid = []
        self.grid_size = 0
    def load_graph(self, room_graph):
        num_rooms = len(room_graph)
        rooms = [None] * num_rooms
        grid_size = 1
        for i in range(0, num_rooms):
            x = room_graph[i][0][0]
            grid_size = max(grid_size, room_graph[i][0][0], room_graph[i][0][1])
            self.rooms[i] = Room(f"Room {i}", f"({room_graph[i][0][0]},{room_graph[i][0][1]})",i, room_graph[i][0][0], room_graph[i][0][1])
        self.room_grid = []
        grid_size += 1
        self.grid_size = grid_size
        for i in range(0, grid_size):
            self.room_grid.append([None] * grid_size)
        for room_id in room_graph:
            room = self.rooms[room_id]
            self.room_grid[room.x][room.y] = room
            if 'n' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms('n', self.rooms[room_graph[room_id][1]['n']])
            if 's' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms('s', self.rooms[room_graph[room_id][1]['s']])
            if 'e' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms('e', self.rooms[room_graph[room_id][1]['e']])
            if 'w' in room_graph[room_id][1]:
                self.rooms[room_id].connect_rooms('w', self.rooms[room_graph[room_id][1]['w']])
        self.starting_room = self.rooms[0]

    def print_rooms(self):
        rotated_room_grid = []
        for i in range(0, len(self.room_grid)):
            rotated_room_grid.append([None] * len(self.room_grid))
        for i in range(len(self.room_grid)):
            for j in range(len(self.room_grid[0])):
                rotated_room_grid[len(self.room_grid[0]) - j - 1][i] = self.room_grid[i][j]
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






















    """
    # visited[] array to make nodes visited  
    # src is starting node for DFS traversal  
    # prev_len is sum of cable length till  
    # current node max_len is pointer which  
    # stores the maximum length of cable 
    # value after DFS traversal  
    def longDFS(graph, src, prev_len,  
            max_len, visited): 
        
        # Mark the src node visited  
        visited[src] = 1
    
        # curr_len is for length of cable  
        # from src city to its adjacent city  
        curr_len = 0
    
        # Adjacent is pair type which stores  
        # destination city and cable length  
        adjacent = None
    
        # Traverse all adjacent  
        for i in range(len(graph[src])): 
            
            # Adjacent element  
            adjacent = graph[src][i]  
    
            # If node or city is not visited  
            if (not visited[adjacent[0]]): 
                
                # Total length of cable from 
                # src city to its adjacent  
                curr_len = prev_len + adjacent[1]  
    
                # Call DFS for adjacent city  
                DFS(graph, adjacent[0], curr_len,  
                                max_len, visited) 
    
            # If total cable length till  
            # now greater than previous  
            # length then update it  
            if (max_len[0] < curr_len):  
                max_len[0] = curr_len  
    
            # make curr_len = 0 for next adjacent  
            curr_len = 0
    
    # n is number of cities or nodes in  
    # graph cable_lines is total cable_lines   
    # among the cities or edges in graph  
    def longestCable(graph, n): 
        
        # maximum length of cable among 
        # the connected cities  
        max_len = [-999999999999]  
    
        # call DFS for each city to find  
        # maximum length of cable 
        for i in range(1, n + 1): 
            
            # initialize visited array with 0  
            visited = [False] * (n + 1)  
    
            # Call DFS for src vertex i  
            DFS(graph, i, 0, max_len, visited) 
    
        return max_len[0] 
    """