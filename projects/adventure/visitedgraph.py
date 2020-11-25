from collections import deque
import random

class VisitedGraph:

    def __init__(self):
        self.rooms = {}
        self.room_count = 0

    def __len__(self):
        return self.room_count

    def __repr__(self):
        output = ''
        for room in self.rooms:
            roomcontents = ''
            for dir in self.rooms[room]:
                self.rooms[room][dir]
                roomcontents += f"{dir}{self.rooms[room][dir]}"
            output += f"{room}({roomcontents}) "
        return output
    
    def add_room(self, room_id, exits):
        """
        Add a room to the graph, with list of available exits, i.e. ['n', 's', 'e'].
        Exits start out as '?' until they are visited.
        """
        if not isinstance(room_id, int):
            print("WARNING: room_id should be an int")
            return
        if room_id in self.rooms:
            return
        
        dirs = {}
        for exit in exits:
            dirs[exit] = '?'

        self.rooms[room_id] = dirs
        self.room_count += 1

    def get_unexplored_exit_for_room(self, room_id):
        """
        Returns random unexplored exit from room
        """
        if not isinstance(room_id, int):
            print("WARNING: room_id should be an int")
            return
        if room_id not in self.rooms:
            print(f"WARNING: room {room_id} not in graph")
            return

        room_node = self.rooms[room_id]
        unexplored_rooms = []
        for exit in room_node:
            if room_node[exit] == '?':
                unexplored_rooms.append(exit)
        if unexplored_rooms:
            return random.choice(unexplored_rooms)
        else:
            return None

    def connect_rooms(self, room1_id, exit_direction_to, room2_id):
        """
        Marks rooms as connected (add an edge to the graph).

        Example usage:
        Room 1 has an east exit connecting to room 2
        connect_rooms(room1, 'e', room2)
        """
        if not isinstance(room1_id, int):
            print("WARNING: room_id should be an int")
            return
        if not isinstance(room2_id, int):
            print("WARNING: room_id should be an int")
            return
        if room1_id not in self.rooms:
            print(f"WARNING: room {room1_id} not in graph")
            return
        if room2_id not in self.rooms:
            print(f"WARNING: room {room2_id} not in graph")
            return
        if room1_id == room2_id:
            print(f"WARNING: room id's must be different")
        if exit_direction_to not in "nswe":
            print(f"WARNING: exit direction invalid")
            return

        room1node = self.rooms[room1_id]
        room1node[exit_direction_to] = room2_id

        room2node = self.rooms[room2_id]
        room2node[self.invertDirection(exit_direction_to)] = room1_id

    def invertDirection(self, dir):
            if dir == "n":
                return "s"
            if dir == "s":
                return "n"
            if dir == "e":
                return "w"
            if dir == "w":
                return "e"
