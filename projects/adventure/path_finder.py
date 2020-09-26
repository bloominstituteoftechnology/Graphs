from collections import deque, defaultdict
from random import randint

FLIP_DIRECTION = {
    'n' : 's',
    's' : 'n',
    'e' : 'w',
    'w' : 'e'
}
class Graph:
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
        # checks if all doors in room have been visited
        if '?' not in self.rooms[room].values():
            self.rooms[room]['check'] = True
        
    def check_complete(self):
        # check all rooms doors have been checked
        for room in self.rooms:
            if not self.rooms[room]['check']:
                return False
        
        if len(self.rooms) == 500:
            return True
        else:
            False

                

def path_finder(player):
    # initialize graph with players starting location
    starting_room = player.current_room.id
    exits =  player.current_room.get_exits()
    graph = Graph(starting_room, exits)

    stack = deque()
    stack.append(starting_room)

    path = []

    while len(stack) > 0:
        if graph.check_complete():
            return path

        curr_room = stack.pop()

        next_step = []
        # get current available list of exits to traverse next from graph
        for door, visited in graph.get_room(curr_room).items():
            print(graph.get_room(curr_room).items())
            if door != 'check' and visited == '?':
                next_step.append(door)
        
        
        # choose a random direction if possible
        if next_step:
            door = randint(0, len(next_step)-1)
            path.append(next_step[door])
        # if no possible direction, dead-end, go back to previous room
        else:
            go_back = FLIP_DIRECTION[path[-1]]
            path.append(go_back)

        # update player position
        player.travel(path[-1])
        new_room = player.current_room.id
        exits = player.current_room.get_exits()

        # update graph with new room info
        graph.next_room(new_room, path[-1] , exits)

        # update stack with new room
        stack.append(new_room)
        


        
        








