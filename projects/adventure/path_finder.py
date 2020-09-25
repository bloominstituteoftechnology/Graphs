from collections import deque, defaultdict
from random import randint

class Graph:
    FLIP_DIRECTION = {
        'n' : 's'
        's' : 'n'
        'e' : 'w'
        'w' : 'e'
    }
    def __init__(self, starting_room, exits):
        self.rooms = {}
        self.rooms[starting_room] = {ex:'?' for ex in exits}
        self.previous_room = starting_room

        # add check to confirm all doors visited
        self.rooms[starting_room]['check'] = False

    def next_room(self, room, direction, exits):
        # update the door traveled through in previous room 
        self.rooms[self.previous_room][direction] = room

        # populate room if not in graph
        if room not in self.rooms:
            self.rooms[room] = {ex:'?' for ex in exits}
            self.rooms[room]['check'] = False

        # update visited doors in current room and check if all visited
        flip = FLIP_DIRECTION[direction]
        self.rooms[room][flip] = self.previous_room
        self.check_doors(room)

        # set previous_room to the current one
        self.previous_room = room

    def get_room(self, room):
        return self.rooms[room]

    def get_size(self):
        return len(self.rooms)

    def check_doors(self, room):
        if '?' not in self.rooms[room].values():
            self.rooms[room]['check'] = True
        
    def check_complete(self):
        # check all rooms doors have been checked
        for room in self.rooms:
            if not room['check']:
                return False
        
        return True if len(self.rooms) == 500

    def go_back(self):
        return previous

                

def path_finder(player):
    # initialize graph with players starting location
    starting_room = player.current_room.id
    exits =  player.current_room.get_exits()
    graph = Graph(starting_room, exits)

    queue = deque()

    # we can start with first exit in list
    queue.append([exits[0]])

    while len(queue) > 0:
        curr_path = queue.popleft()
        direction = curr_path[-1]

        # send player in that direction and get room info
        player.travel(direction)
        curr_room = player.current_room.id
        curr_exits = player.current_room.get_exits

        #update graph with new room info
        graph.next_room(curr_room, direction, curr_exits)
        
        # get current available list of exits to traverse next from graph
        for ex, visited in graph.get_room().items():
            if ex != 'check' and visited == '?':
                new_path = curr_path.copy
                new_path.append(ex)
                queue.append(new_path)
        








