from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Global variables
player_starting_room = player.current_room
stack = Stack()
queue = Queue()
visited = {}
bfs_visited = {}
path_taken = []
first = True
path = []


def travel_path_player(path):
    for x in path:
        player.travel(x)
        path_taken.append(x)

def get_oposite_direction():
    if path_taken[-1] == 'n':
        return 's'
    elif path_taken[-1] == 's':
        return 'n'
    elif path_taken[-1] == 'e':
        return 'w'
    elif path_taken[-1] == 'w':
        return 'e'

def get_oposite_direction_bfs():
    if path[-1] == 'n':
        return 's'
    elif path[-1] == 's':
        return 'n'
    elif path[-1] == 'e':
        return 'w'
    elif path[-1] == 'w':
        return 'e'

def get_random_course(room):
    # get random direction to start traversing
    random_array = room.get_exits()
    random.shuffle(random_array)
    going_to = room.get_room_in_direction(random_array[-1])
    
    return (going_to, random_array[-1])

def deal_with_room_exits(room):
    exits = room.get_exits()

    # checking if were not at the end of a path
    exits_string ='nswe'
    if len(exits) > 1:
        for x in exits_string:
            if x not in exits:
                visited[room][x][0] = None
                visited[room][x][1] = None


        # remove the direction in which we just came from so that we don't repeat ourselves
        exits.remove(get_oposite_direction())

        # add it to the dictionary for the previous direction as the previous room
        visited[room][get_oposite_direction()][0] = room.get_room_in_direction(get_oposite_direction())
        visited[room][get_oposite_direction()][1] = visited[room][get_oposite_direction()][0].id

        # loop through the exits until finding an unexplored path
        for x in exits:
            if visited[room][x][0] == '?':
                return (False, x)

    else:
        for x in exits_string:
            if x not in exits:
                visited[room][x][0] = None
        return(True, exits[0])

def get_all_room_exits(room):
    return room.get_exits()


def get_room_status(room):
    for exits in visited[room]:
        if visited[room][exits][0] == '?':
            return True
    
    return False


def traverseWorld():
    # creating dict entry for starting room
    visited[player_starting_room] = {'n': ['?',''], 's': ['?',''], 'w': ['?',''], 'e' : ['?','']}

    # get random room to start traversing
    starting_route = get_random_course(player_starting_room)

    # get the next room and move the player there
    going_to_room = starting_route[0]

    # get the direction were going and append it to the path
    direction_to = starting_route[1]
    visited[player_starting_room][direction_to][0] = going_to_room
    visited[player_starting_room][direction_to][1] = going_to_room.id
    path_taken.append(direction_to)
    player.travel(direction_to)

    # while traversing:
    result = traverse_path(player.current_room)
    return result

def traverse_path(room):
    stack.push(room)
    while stack.size() > 0:
        current_room = stack.pop()

        # PROBLEM HERE using the get_room_status() and also going to the wrong room as well as filling in the dictionary
        if current_room not in visited or get_room_status(current_room):
            if current_room not in visited: 
                visited[current_room] = {'n': ['?',''], 's': ['?',''], 'w': ['?',''], 'e' : ['?','']}
            # get all the exits and check if we've reached the end of a path
            exits = deal_with_room_exits(current_room)
            # if we have not reached the end of our path do this
            if exits[0] == False:
                # add that direction to the path 
                path_taken.append(exits[1])
                # move your player if it's a place he has not yet been
                player.travel(exits[1])

                # add the room to the dictionaries direction
                visited[current_room][exits[1]][0] = player.current_room
                visited[current_room][exits[1]][1] = player.current_room.id

                # add the room to the stack
                stack.push(player.current_room)
                
            # if we have reached the end do this
            else:
                # reached the end of the path
                # add that direction to the path 
                path_taken.append(exits[1])
                # move your player
                print(player.current_room.id)
                player.travel(exits[1])
                print(player.current_room.id)

                # need to add it to the dictionary here
                visited[current_room][exits[1]][0] = player.current_room
                visited[current_room][exits[1]][1] = visited[current_room][exits[1]][0].id
                print(player.current_room.id)

                # we need to do bfs to find an unexplored room
                find_unexplored_room(player.current_room)


            # NEED TO QUEUE UP THE EXITS ===0   E-R0=Q-EWFOPOASDJFPOADSJIOPJFP
    # ok = path_taken.remove(path_taken[-1])
    print(path_taken)
    print("")
    return path_taken

def find_unexplored_room(room):
    if len(path) > 0:
        path = []
    first = True
    bfs_visited[room] = []
    queue.enqueue(room)
    while queue.size() > 0:
        current_location = queue.dequeue()
        if current_location not in bfs_visited:
            bfs_visited[current_location] = []

        # I think we need to check the room given to see if it has unexplored paths
        exits = get_all_room_exits(current_location)
        if first:
            first = False
            exits.remove(get_oposite_direction())
        else:
            exits.remove(get_oposite_direction_bfs())
        

        for direction in visited[current_location]:
            if visited[current_location][direction][0] == '?':
                visited[current_location][direction][0] = current_location.get_room_in_direction(direction)
                visited[current_location][direction][1] = visited[current_location][direction][0].id  
                path.append(direction)
                bfs_visited[current_location].append(direction)
                stack.stack = []
                stack.push(current_location.get_room_in_direction(direction))
                travel_path_player(path)
                return

        # if we reach this point we did not find an unexplored path in the current room 
        # 
        # so we need to queue up one of the rooms other than the direction it just came from to look in to find another room  
        for x in exits:
            if x not in bfs_visited[current_location]:
                queue.enqueue(current_location.get_room_in_direction(x))
                path.append(x)
                bfs_visited[current_location].append(x)
                break
        


        # if we reach this point and we still did not find any '?' we have explored all paths and we need to return the path explored





       # FIX-me we need the player to travel to the newly discovered room with 

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = traverseWorld()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

print(traversal_path)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
