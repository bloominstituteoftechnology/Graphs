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

    def next_room(self, room, direction, exits):
        # update the door traveled through in previous room 
        self.rooms[self.previous_room][direction] = room

        # populate room if not in graph
        if room not in self.rooms:
            self.rooms[room] = {ex:'?' for ex in exits}

        # update visited doors in current room
        flip = FLIP_DIRECTION[direction]
        self.rooms[room][flip] = self.previous_room

        # set previous_room to the current one
        self.previous_room = room

    def get_room(self, room):
        return self.rooms[room]

    def size(self):
        return len(self.rooms)
        
    def check_complete(self):
        # check all rooms doors have been checked
        for room in self.rooms:
            if '?' in self.rooms[room].values():
                return False
        
        if len(self.rooms) == 500:
            return True
        else:
            False
    
    def __repr__(self):
        return f'-------\n  Rooms\n ------\n{self.rooms}\n----------'

                
PATH = []
def path_finder(player):

    # initialize graph with players starting location
    starting_room = player.current_room.id
    exits =  player.current_room.get_exits()
    graph = Graph(starting_room, exits)

    stack = deque()
    start = exits[randint(0,len(exits)-1)]
    stack.append(start)

    while len(stack) > 0:        
        direction = stack.pop()
        PATH.append(direction)
        
        #print(f'Path -- {PATH}')
        
        # send player in new direction and get room info
        player.travel(direction)
        curr_room = player.current_room.id
        exits = player.current_room.get_exits()

        # update graph with new room info
        graph.next_room(curr_room, direction , exits)
        
        debug(curr_room, graph)

        # check if graph completed with last addition
        if graph.check_complete():
            
            #print(f'---------\nPath in checkout\n--------\n{PATH} ')
            
            return PATH

        # find next step to take and add to stack
        step = next_step(curr_room, graph, player)

        if step:
            stack.append(step)


def next_step(room, graph, player):
    '''
    Takes exits and filters for unexplored(?) exits
    Then will randomly selct one of those exits to return as a step
    If there is no step to take from passed in exits, run unxeplored 
    function to find a room with next step
    '''
    room_data = graph.get_room(room)

    # check for unexplored doors in current room
    for direction, door in room_data.items():
        if door == "?":   
            return direction

    # if all doors explored, search for a room with unexplored doors
    return unexplored_path(room, graph, player)

def unexplored(room, graph):
    '''
    If there are no exits that have been unexplored, perform
    bfs to find next available room to traverse to
    '''
    queue = deque()
    queue.append([room])
    visited = set()

    while len(queue) > 0:
        curr_path = queue.popleft()
        curr_room = curr_path[-1]
        visited.add(curr_room)

        # check if we found an unexplored room
        if curr_room == "?":
            return curr_path[:-1]

        room_data = graph.get_room(curr_room)
        
        for neighbor in room_data.values():
            if neighbor not in visited:
                new_path = curr_path.copy()
                new_path.append(neighbor)
                queue.append(new_path)

    return []

def unexplored_path(start, graph, player):
    '''
    Use the rooms provided by unexplored function to
    map to an actaul path through the rooms. Append that
    path to main path and return the final step to append
    to stack in main function
    '''
    rooms = unexplored(start, graph)
    path = []

    for i in range(len(rooms) -1):
        for direction, neighbor in graph.get_room(rooms[i]).items():
            # check if a neighbor is the next room in path and add direction
            if i+1 < len(rooms) and neighbor == rooms[i+1]:
                path.append(direction)

    # if path is none then no unexplored rooms
    if len(path) > 0:
        # last step needs to be explored
        next_step = path.pop()

        # for all other steps, move player into correct position to explore
        for step in path:
            player.travel(step)

        # update main path with steps taken
        PATH.extend(path)

        return next_step
    
    return []
    
def debug (curr_room, graph):
    size = graph.size()

    if size > 485:
        print(f'Room:{curr_room} -- {graph.get_room(curr_room)}')
    
    if size > 490:
        print(graph)
